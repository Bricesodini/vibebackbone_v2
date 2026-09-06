"""Read-only comparison and transfer measurements over explicitly selected local inputs."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import stat
import subprocess
import sys


class InputError(ValueError):
    pass


def read_json(path):
    try:
        raw = Path(path).read_bytes()
        value = json.loads(raw)
    except (OSError, ValueError) as exc:
        raise InputError(f'cannot read JSON input: {path}: {exc}') from exc
    return value, hashlib.sha256(raw).hexdigest()


def exact_path(value):
    if (not isinstance(value, str) or not value or '\\' in value or '\x00' in value
            or any(part in ('', '.', '..') for part in value.split('/'))
            or value.startswith('/') or any(c in value for c in '*?[]')):
        raise InputError(f'expected explicit normalized relative path: {value!r}')
    try:
        os.fsencode(value)
    except UnicodeEncodeError as exc:
        raise InputError(f'path is not encodable on this filesystem: {value!r}') from exc
    return value


def root_path(path):
    try:
        root = Path(path).resolve(strict=True)
    except (OSError, RuntimeError) as exc:
        raise InputError(f'root unavailable: {path}') from exc
    if not root.is_dir():
        raise InputError(f'root is not a directory: {path}')
    return root


def snapshot(root, relative):
    """Open each component without following symlinks; hash a regular file only."""
    parts = exact_path(relative).split('/')
    opened = []
    try:
        fd = os.open(root, os.O_RDONLY | os.O_DIRECTORY)
        opened.append(fd)
        for index, part in enumerate(parts):
            meta = os.stat(part, dir_fd=fd, follow_symlinks=False)
            if stat.S_ISLNK(meta.st_mode):
                return {'status': 'refused_symlink'}
            if index != len(parts) - 1:
                if not stat.S_ISDIR(meta.st_mode):
                    return {'status': 'not_directory'}
                fd = os.open(part, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=fd)
                opened.append(fd)
                continue
            if not stat.S_ISREG(meta.st_mode):
                return {'status': 'not_regular_file'}
            file_fd = os.open(part, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK, dir_fd=fd)
            opened.append(file_fd)
            before = os.fstat(file_fd)
            if not stat.S_ISREG(before.st_mode):
                return {'status': 'not_regular_file'}
            digest = hashlib.sha256()
            count = 0
            while block := os.read(file_fd, 1024 * 1024):
                digest.update(block)
                count += len(block)
            after = os.fstat(file_fd)
            current = os.stat(part, dir_fd=fd, follow_symlinks=False)
            signature = lambda st: (st.st_dev, st.st_ino, st.st_size, st.st_mtime_ns, st.st_ctime_ns)
            if signature(before) != signature(after) or signature(after) != signature(current) or count != after.st_size:
                return {'status': 'changed_during_read'}
            return {'status': 'present', 'size': count, 'sha256': digest.hexdigest()}
    except FileNotFoundError:
        return {'status': 'absent'}
    except OSError as exc:
        return {'status': 'io_unavailable', 'errno': exc.errno}
    finally:
        for fd in reversed(opened):
            os.close(fd)


def request_input(value):
    if not isinstance(value, dict) or set(value) - {'paths', 'references', 'git_refs'}:
        raise InputError('request must contain only paths, references, git_refs')
    paths = value.get('paths', [])
    references = value.get('references', [])
    refs = value.get('git_refs', [])
    if not all(isinstance(v, list) for v in [paths, references, refs]):
        raise InputError('request fields must be lists')
    paths = [exact_path(p) for p in paths]
    if len(set(paths)) != len(paths):
        raise InputError('duplicate paths')
    names = set()
    for reference in references:
        if not isinstance(reference, dict) or set(reference) != {'name', 'candidates'}:
            raise InputError('reference needs name and candidates')
        name = reference['name']
        if not isinstance(name, str) or not name.strip() or name in names:
            raise InputError('reference names must be unique nonempty strings')
        names.add(name)
        candidates = reference['candidates']
        if not isinstance(candidates, list) or not candidates:
            raise InputError('reference needs explicit candidate paths')
        candidates = [exact_path(p) for p in candidates]
        if len(set(candidates)) != len(candidates):
            raise InputError('duplicate reference candidates')
    if any(not isinstance(ref, str) or not ref or ref.startswith('-') or '\x00' in ref or '\n' in ref for ref in refs):
        raise InputError('Git refs must be nonempty explicit revision expressions')
    if len(set(refs)) != len(refs):
        raise InputError('duplicate Git refs')
    if not paths and not references and not refs:
        raise InputError('empty selection is not a successful check')
    return sorted(paths), sorted(references, key=lambda r: r['name']), sorted(refs)


def baseline_input(value, name):
    if not isinstance(value, dict) or set(value) != {'name', 'files'}:
        raise InputError('baseline needs exactly name and files')
    if not isinstance(name, str) or not name.strip() or value['name'] != name:
        raise InputError('baseline name missing or does not match requested name')
    if not isinstance(value['files'], dict):
        raise InputError('baseline files must be a mapping')
    for path, info in value['files'].items():
        exact_path(path)
        if (not isinstance(info, dict) or set(info) != {'size', 'sha256'}
                or type(info['size']) is not int or info['size'] < 0
                or not isinstance(info['sha256'], str)
                or not re.fullmatch('[0-9a-f]{64}', info['sha256'])):
            raise InputError(f'invalid baseline digest/size for {path}')
    return value['files']


def compare_file(source, destination):
    a, b = source['status'], destination['status']
    if a not in ('present', 'absent') or b not in ('present', 'absent'):
        return 'unavailable'
    if a == 'absent' and b == 'absent':
        return 'absent_both'
    if a == 'absent':
        return 'absent_source'
    if b == 'absent':
        return 'absent_destination'
    return 'identical' if (source['size'], source['sha256']) == (destination['size'], destination['sha256']) else 'modified'


def envelope(operation, inputs):
    return {'operation': operation, 'inputs': inputs, 'files': [], 'references': [], 'git_refs': [],
            'limits': {'scope': 'explicit selections only', 'semantic_completeness': 'not_checked',
                       'approval': 'not_checked', 'historical_execution': 'not_proven',
                       'historical_receipt': 'not_proven', 'atomic_tree_snapshot': False,
                       'symlinks': 'all refused; internal links also refused'},
            'measurement_complete': True, 'selected_items_equal': True}


def conclude(result):
    rows = result['files'] + result['references'] + result['git_refs']
    incomplete = {'unavailable', 'git_unavailable'}
    result['measurement_complete'] = not any(row['status'] in incomplete for row in rows)
    result['selected_items_equal'] = bool(rows) and all(row['status'] == 'identical' for row in rows)
    result['exit_code'] = 2 if not result['measurement_complete'] else (0 if result['selected_items_equal'] else 1)
    return result


def compare(root, baseline, name, request, manifest_digest=None):
    paths, refs, git_refs = request_input(request)
    if refs or git_refs:
        raise InputError('baseline comparison accepts paths only; use inventory for references')
    files = baseline_input(baseline, name)
    root = root_path(root)
    result = envelope('compare', {'root': str(root), 'baseline_name': name,
                                 'baseline_manifest_sha256': manifest_digest,
                                 'baseline_kind': 'declared_digest_manifest'})
    for path in paths:
        actual = snapshot(root, path)
        recorded = files.get(path)
        if actual['status'] not in ('present', 'absent'):
            status = 'unavailable'
        elif recorded is None:
            status = 'not_in_baseline'
        elif actual['status'] == 'absent':
            status = 'absent_current'
        else:
            status = compare_file({'status': 'present', **recorded}, actual)
        result['files'].append({'path': path, 'status': status, 'baseline': recorded, 'current': actual})
    return conclude(result)


def resolve_reference(root, candidates):
    observations = {p: snapshot(root, p) for p in sorted(candidates)}
    if any(v['status'] not in ('present', 'absent') for v in observations.values()):
        return {'status': 'unavailable', 'candidates': observations}
    present = [p for p, v in observations.items() if v['status'] == 'present']
    if len(present) != 1:
        return {'status': 'ambiguous' if present else 'absent', 'candidates': observations}
    return {'status': 'resolved', 'path': present[0], 'file': observations[present[0]], 'candidates': observations}


def git_revision(root, reference):
    # Worktree .git indirections deliberately not supported by this first instrument.
    if not (root / '.git').is_dir() or (root / '.git').is_symlink():
        return {'status': 'git_unavailable', 'reason': 'local .git directory required'}
    env = {k: v for k, v in os.environ.items() if not k.startswith('GIT_')}
    env.update(GIT_CONFIG_NOSYSTEM='1', GIT_CONFIG_GLOBAL=os.devnull, GIT_OPTIONAL_LOCKS='0', GIT_TERMINAL_PROMPT='0')
    cmd = ['git', '--no-optional-locks', '-c', 'core.fsmonitor=false', '-C', str(root),
           'rev-parse', '--verify', '--end-of-options', reference + '^{commit}']
    try:
        answer = subprocess.run(cmd, env=env, capture_output=True, text=True, timeout=10)
    except (OSError, subprocess.TimeoutExpired):
        return {'status': 'git_unavailable', 'reason': 'Git command unavailable or timed out'}
    if answer.returncode:
        return {'status': 'git_unavailable', 'reason': 'commit reference unresolved'}
    commit = answer.stdout.strip()
    if not re.fullmatch('[0-9a-f]{40}|[0-9a-f]{64}', commit):
        return {'status': 'git_unavailable', 'reason': 'unexpected revision output'}
    return {'status': 'resolved', 'commit': commit}


def inventory(source, destination, request):
    paths, references, git_refs = request_input(request)
    source, destination = root_path(source), root_path(destination)
    result = envelope('inventory', {'source': str(source), 'destination': str(destination)})
    for path in paths:
        a, b = snapshot(source, path), snapshot(destination, path)
        result['files'].append({'path': path, 'status': compare_file(a, b), 'source': a, 'destination': b})
    for reference in references:
        a, b = (resolve_reference(root, reference['candidates']) for root in [source, destination])
        if 'unavailable' in (a['status'], b['status']):
            status = 'unavailable'
        elif 'ambiguous' in (a['status'], b['status']):
            status = 'ambiguous'
        elif a['status'] != 'resolved' or b['status'] != 'resolved':
            status = 'unresolved'
        elif a['path'] != b['path']:
            status = 'different_target'
        else:
            status = compare_file(a['file'], b['file'])
        result['references'].append({'name': reference['name'], 'status': status, 'source': a, 'destination': b})
    for reference in git_refs:
        a, b = git_revision(source, reference), git_revision(destination, reference)
        status = 'git_unavailable' if 'git_unavailable' in (a['status'], b['status']) else ('identical' if a['commit'] == b['commit'] else 'different_commit')
        result['git_refs'].append({'ref': reference, 'status': status, 'source': a, 'destination': b})
    return conclude(result)


def render(result):
    """Projection of the exact JSON result; no separate interpretation layer."""
    if 'error' in result:
        return 'ERROR: ' + result['error'] + '\n'
    lines = [result['operation'], 'inputs: ' + json.dumps(result['inputs'], sort_keys=True, ensure_ascii=False)]
    for group in ['files', 'references', 'git_refs']:
        for row in result[group]:
            lines.append(group + ': ' + json.dumps(row, sort_keys=True, ensure_ascii=False))
    lines += ['measurement_complete: ' + str(result['measurement_complete']),
              'selected_items_equal: ' + str(result['selected_items_equal']),
              'limits: ' + json.dumps(result['limits'], sort_keys=True)]
    return '\n'.join(lines) + '\n'


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='operation', required=True)
    for name in ['compare', 'inventory']:
        p = sub.add_parser(name)
        p.add_argument('--request', required=True)
        p.add_argument('--format', choices=['json', 'text'], default='json')
        if name == 'compare':
            p.add_argument('--root', required=True)
            p.add_argument('--baseline', required=True)
            p.add_argument('--baseline-name', required=True)
        else:
            p.add_argument('--source', required=True)
            p.add_argument('--destination', required=True)
    args = parser.parse_args(argv)
    try:
        request, request_hash = read_json(args.request)
        if args.operation == 'compare':
            baseline, baseline_hash = read_json(args.baseline)
            result = compare(args.root, baseline, args.baseline_name, request, baseline_hash)
        else:
            result = inventory(args.source, args.destination, request)
        result['inputs']['request_sha256'] = request_hash
    except (InputError, OSError) as exc:
        result = {'error': str(exc), 'exit_code': 2}
    sys.stdout.write(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2) + '\n' if args.format == 'json' else render(result))
    return result['exit_code']


if __name__ == '__main__':
    raise SystemExit(main())
