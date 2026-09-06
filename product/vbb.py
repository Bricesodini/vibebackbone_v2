"""Vibe Backbone local candidate: scoped measurements and attributable file lifecycle.

No model execution, provider, scheduler or global configuration. Python 3.10+.
"""
import argparse
import base64
import hashlib
import json
import os
from pathlib import Path
import re
import stat
import sys
import tempfile

FILES = ('vbb.py', 'continuity.py', 'agreement.md', 'README.md', 'profiles.md')
BUNDLE = 'bundle.json'
RECEIPT = 'receipt.json'
BLOCK = b'<!-- VBB:BEGIN -->\nPour une mission avec reprise durable ou mesure de fichiers, lire [.vbb/agreement.md](.vbb/agreement.md). Une demande triviale reste native, sans document de memoire impose.\n<!-- VBB:END -->\n'


class Refusal(ValueError):
    pass


def sha(data):
    return hashlib.sha256(data).hexdigest()


def read_regular(path):
    if path.is_symlink() or not path.is_file():
        raise Refusal(f'not a regular owned file: {path.name}')
    return path.read_bytes()


def atomic(path, data):
    """One file at a time, with a journal written before payload changes."""
    if path.is_symlink():
        raise Refusal(f'symlink refused: {path.name}')
    # Keep crash leftovers inside the inspected managed directory, including
    # AGENTS replacements. Unknown temporaries are reported, never guessed owned.
    scratch = path.parent / '.vbb' if path.name == 'AGENTS.md' else path.parent
    fd, name = tempfile.mkstemp(prefix='.vbb-write-', dir=scratch)
    try:
        with os.fdopen(fd, 'wb') as f:
            if path.exists():
                old = path.stat()
                current = os.fstat(f.fileno())
                if (old.st_uid, old.st_gid) != (current.st_uid, current.st_gid):
                    os.fchown(f.fileno(), old.st_uid, old.st_gid)
                os.fchmod(f.fileno(), stat.S_IMODE(old.st_mode))
            f.write(data)
            f.flush()
            os.fsync(f.fileno())
        os.replace(name, path)
    finally:
        if os.path.exists(name):
            os.unlink(name)


def json_bytes(obj):
    return (json.dumps(obj, indent=2, ensure_ascii=False, sort_keys=True) + '\n').encode()


def project_root(value):
    root = Path(value).expanduser().resolve(strict=True)
    if not root.is_dir():
        raise Refusal('project must be an existing directory')
    if any((p / '.backbone-dev').exists() for p in (root, *root.parents)):
        raise Refusal('installation/lifecycle in the design factory is refused')
    own = Path(__file__).resolve().parent
    if root == own:
        raise Refusal('target must be a separate project')
    managed = root / '.vbb'
    if managed.is_symlink() or (managed.exists() and not managed.is_dir()):
        raise Refusal('.vbb must be a regular directory')
    if (root / 'AGENTS.md').is_symlink():
        raise Refusal('AGENTS.md symlink refused')
    return root


def load_bundle(source):
    source = Path(source).resolve(strict=True)
    raw = read_regular(source / BUNDLE)
    obj = json.loads(raw)
    if set(obj) != {'schema', 'version', 'files'} or obj['schema'] != 1:
        raise Refusal('invalid bundle schema')
    if not isinstance(obj['version'], str) or not re.fullmatch(r'[0-9]+\.[0-9]+\.[0-9]+(?:-rc\.[0-9]+)?', obj['version']):
        raise Refusal('invalid bundle version')
    if not isinstance(obj['files'], dict) or set(obj['files']) != set(FILES):
        raise Refusal('bundle must list exactly the supported payload files')
    payload = {}
    for name in FILES:
        data = read_regular(source / name)
        if obj['files'][name] != sha(data):
            raise Refusal(f'bundle digest mismatch: {name}')
        payload[name] = data
    payload[BUNDLE] = raw
    return obj, payload


def load_receipt(managed):
    obj = json.loads(read_regular(managed / RECEIPT))
    fields = {'schema', 'version', 'state', 'files', 'previous_files', 'agents_segment', 'agents_existed', 'agents_removed'}
    optional = {'agents_before_sha256', 'agents_removal'}
    if not fields <= set(obj) or set(obj) - fields - optional or obj['schema'] != 1 or obj['state'] not in {'pending', 'installed', 'retired'}:
        raise Refusal('invalid receipt; preserve files and inspect manually')
    for key in ['files', 'previous_files']:
        if not isinstance(obj[key], dict) or (key == 'files' and set(obj[key]) != set(FILES) | {BUNDLE}):
            raise Refusal('invalid receipt file set')
        if set(obj[key]) - (set(FILES) | {BUNDLE}):
            raise Refusal('receipt path outside owned file set')
        if any(not isinstance(h, str) or not re.fullmatch('[0-9a-f]{64}', h) for h in obj[key].values()):
            raise Refusal('invalid receipt digest')
    segment = base64.b64decode(obj['agents_segment'], validate=True)
    if segment not in (BLOCK, b'\n' + BLOCK) or type(obj['agents_existed']) is not bool or type(obj['agents_removed']) is not bool:
        raise Refusal('invalid AGENTS ownership record')
    before = obj.get('agents_before_sha256')
    if before is not None and (not isinstance(before, str) or not re.fullmatch('[0-9a-f]{64}', before)):
        raise Refusal('invalid initial AGENTS digest')
    target = obj.get('agents_removal')
    if target is not None and (not isinstance(target, dict) or set(target) != {'exists', 'sha256'} or type(target['exists']) is not bool or not isinstance(target['sha256'], str) or not re.fullmatch('[0-9a-f]{64}', target['sha256'])):
        raise Refusal('invalid AGENTS removal journal')
    return obj


def inspect(root):
    managed = root / '.vbb'
    if not managed.exists():
        return {'state': 'absent', 'files': {}, 'residues': []}
    if not any(managed.iterdir()):
        return {'state': 'empty', 'files': {}, 'residues': []}
    if not (managed / RECEIPT).exists():
        return {'state': 'unowned', 'files': {}, 'residues': sorted(p.name for p in managed.iterdir())}
    receipt = load_receipt(managed)
    states = {}
    for name, expected in receipt['files'].items():
        p = managed / name
        if p.is_symlink():
            states[name] = 'symlink_preserved'
        elif not p.exists():
            states[name] = 'missing'
        elif not p.is_file():
            states[name] = 'non_file_preserved'
        else:
            digest = sha(p.read_bytes())
            states[name] = 'equal' if digest == expected else ('previous' if digest == receipt['previous_files'].get(name) else 'divergent')
    ap = root / 'AGENTS.md'
    segment = base64.b64decode(receipt['agents_segment'])
    content = read_regular(ap) if ap.exists() else b''
    agents = 'removed' if receipt['agents_removed'] else ('equal' if content.count(segment) == 1 else 'divergent_or_missing')
    residues = sorted(p.name for p in managed.iterdir() if p.name not in receipt['files'] and p.name != RECEIPT)
    return {'state': receipt['state'], 'version': receipt['version'], 'files': states, 'agents_block': agents, 'residues': residues}


def install(root, source, update=False):
    manifest, payload = load_bundle(source)
    managed = root / '.vbb'
    desired = {n: sha(b) for n, b in payload.items()}
    ap = root / 'AGENTS.md'
    before = read_regular(ap) if ap.exists() else b''
    if managed.exists() and (managed / RECEIPT).exists():
        receipt = load_receipt(managed)
        if receipt['state'] == 'retired':
            raise Refusal('retired installation has residues; preserve/resolve them before reinstalling')
        segment = base64.b64decode(receipt['agents_segment'])
        if before.count(segment) != 1:
            # A pending initial install may not yet have written its AGENTS segment.
            if not (receipt['state'] == 'pending' and not receipt['previous_files'] and b'<!-- VBB:' not in before):
                raise Refusal('AGENTS block diverged; no overwrite')
        if receipt['files'] != desired and not update:
            raise Refusal('different bundle: use install --update with an explicit source')
        if receipt['state'] == 'pending' and receipt['files'] != desired:
            raise Refusal('finish the same pending bundle before another update')
        allowed = [receipt['files'], receipt['previous_files']]
        for name in desired:
            p = managed / name
            if p.exists() or p.is_symlink():
                current = sha(read_regular(p))
                if not any(mapping.get(name) == current for mapping in allowed):
                    raise Refusal(f'owned file diverged; no overwrite: {name}')
        previous = receipt['previous_files'] if receipt['state'] == 'pending' else receipt['files']
    else:
        if managed.exists() and any(managed.iterdir()):
            raise Refusal('existing .vbb is unowned; no overwrite')
        if b'<!-- VBB:' in before:
            raise Refusal('existing VBB marker has no valid receipt; no overwrite')
        segment = (b'\n' if before and not before.endswith(b'\n') else b'') + BLOCK
        receipt = {'schema': 1, 'version': manifest['version'], 'state': 'pending', 'files': desired, 'previous_files': {}, 'agents_segment': base64.b64encode(segment).decode(), 'agents_existed': ap.exists(), 'agents_removed': False, 'agents_before_sha256': sha(before), 'agents_removal': None}
        previous = {}
    # Entire preflight completed before any payload replacement.
    managed.mkdir(exist_ok=True)
    receipt.update(state='pending', version=manifest['version'], files=desired, previous_files=previous)
    atomic(managed / RECEIPT, json_bytes(receipt))
    for name, data in payload.items():
        p = managed / name
        if not p.exists() or read_regular(p) != data:
            atomic(p, data)
    if before.count(segment) == 0:
        atomic(ap, before + segment)
    receipt.update(state='installed', previous_files={})
    atomic(managed / RECEIPT, json_bytes(receipt))
    return inspect(root)


def remove(root):
    managed = root / '.vbb'
    if not managed.exists():
        return {'state': 'absent', 'preserved': []}
    if not any(managed.iterdir()):
        # Terminal gap after receipt unlink, or an empty pre-existing directory.
        # No file is attributed or removed in this case.
        managed.rmdir()
        return {'state': 'removed', 'preserved': []}
    receipt = load_receipt(managed)
    preserved = []
    for name, digest in receipt['files'].items():
        p = managed / name
        if p.is_symlink() or (p.exists() and not p.is_file()):
            preserved.append('.vbb/' + name)
        elif p.exists():
            if sha(p.read_bytes()) in {digest, receipt['previous_files'].get(name)}:
                p.unlink()
            else:
                preserved.append('.vbb/' + name)
    ap = root / 'AGENTS.md'
    if not receipt['agents_removed']:
        if not ap.exists():
            receipt['agents_removed'] = True
        else:
            segment = base64.b64decode(receipt['agents_segment'])
            content = read_regular(ap)
            target = receipt.get('agents_removal')
            if target and target['exists'] and sha(content) == target['sha256']:
                # The preceding process already replaced AGENTS before stopping.
                receipt['agents_removed'] = True
            elif receipt['state'] == 'pending' and not receipt['previous_files'] and sha(content) == receipt.get('agents_before_sha256'):
                # Initial installation stopped before writing any AGENTS segment.
                receipt['agents_removed'] = True
            elif content.count(segment) == 1:
                after = content.replace(segment, b'', 1)
                receipt['agents_removal'] = {'exists': bool(after) or receipt['agents_existed'], 'sha256': sha(after)}
                atomic(managed / RECEIPT, json_bytes(receipt))
                if not after and not receipt['agents_existed']:
                    ap.unlink()
                else:
                    atomic(ap, after)
                receipt['agents_removed'] = True
            else:
                preserved.append('AGENTS.md (divergent VBB block)')
    residues = [p.name for p in managed.iterdir() if p.name != RECEIPT]
    if not residues and receipt['agents_removed']:
        (managed / RECEIPT).unlink()
        managed.rmdir()
        return {'state': 'removed', 'preserved': []}
    receipt['state'] = 'retired'
    atomic(managed / RECEIPT, json_bytes(receipt))
    return {'state': 'retired_with_residues', 'preserved': sorted(set(preserved + ['.vbb/' + n for n in residues]))}


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    if argv and argv[0] in {'compare', 'inventory'}:
        sys.dont_write_bytecode = True
        import continuity
        return continuity.main(argv)
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='action', required=True)
    for name in ['install', 'inspect', 'remove']:
        p = sub.add_parser(name)
        p.add_argument('--project', required=True)
        if name == 'install':
            p.add_argument('--source', default=str(Path(__file__).resolve().parent))
            p.add_argument('--update', action='store_true')
    args = parser.parse_args(argv)
    try:
        root = project_root(args.project)
        result = install(root, args.source, args.update) if args.action == 'install' else (inspect(root) if args.action == 'inspect' else remove(root))
        print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
        return 1 if result.get('state') in {'retired_with_residues', 'unowned'} else 0
    except (OSError, ValueError, TypeError, KeyError) as exc:
        print(json.dumps({'error': str(exc), 'effects': 'inspect project; pending journal may describe partial effects; divergences are not overwritten'}, ensure_ascii=False))
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
