"""Factory-only, one explicit native trial per invocation. Never distributed."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import platform
import shutil
import subprocess
import tempfile
import time

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / '.backbone-dev/evaluations/l1/runs'
CODEX = '/Applications/ChatGPT.app/Contents/Resources/codex'

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def snapshot(work):
    return {str(p.relative_to(work)): digest(p) for p in sorted(work.rglob('*'))
            if p.is_file() and '.git' not in p.parts and '__pycache__' not in p.parts}

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('case', choices=['small', 'repair', 'scope', 'resume'])
    parser.add_argument('variant', choices=['M0', 'VBB'])
    args = parser.parse_args()
    case = json.loads((ROOT / '.backbone-dev/corpus/development/missions.json').read_text())[args.case]
    record = OUT / f'{args.case}-{args.variant}'
    record.mkdir(parents=True, exist_ok=False)
    work = Path(tempfile.mkdtemp(prefix=f'vbb-l1-{args.case}-{args.variant}-')).resolve()
    for name, content in case['files'].items():
        p = work / name
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content)
    subprocess.run(['git', 'init', '-q', str(work)], check=True)
    if args.variant == 'VBB':
        shutil.copytree(ROOT / '.backbone-dev/evaluations/l1/candidate/vbb-work', work / '.agents/skills/vbb-work')
    prompt = case['prompt']
    if args.variant == 'VBB':
        prompt += '\nUtilise $vbb-work dans .agents/skills/vbb-work/SKILL.md pour cette mission.'
    prompt += '\nTravaille uniquement dans ce projet temporaire. N\'installe rien, ne contacte aucun service externe et ne lance aucun autre agent. Python standard est disponible. Les sources du projet suffisent.'
    (record / 'prompt.txt').write_text(prompt)
    initial = snapshot(work)
    cmd = [CODEX, 'exec', '--ignore-user-config', '--ephemeral', '--json',
           '-m', 'gpt-6-astra', '-c', 'model_reasoning_effort="low"',
           '-c', 'approval_policy="never"', '-s', 'workspace-write',
           '-C', str(work), '-o', str(record / 'final.txt'), '-']
    meta = {'case': args.case, 'variant': args.variant, 'workspace': str(work),
            'command': cmd, 'platform': platform.platform(),
            'harness_version': subprocess.check_output([CODEX, '--version'], text=True).strip(),
            'input_hashes': initial, 'prompt_sha256': digest(record / 'prompt.txt'),
            'fixture_sha256': digest(ROOT / '.backbone-dev/corpus/development/missions.json'),
            'started_at': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
            'human_time_total': None, 'money_cost': None}
    (record / 'meta.json').write_text(json.dumps(meta, indent=2)+'\n')
    start = time.monotonic()
    with (record / 'events.jsonl').open('w') as out, (record / 'stderr.txt').open('w') as err:
        proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=out, stderr=err,
                                cwd=work, start_new_session=True)
        try:
            proc.communicate(prompt.encode(), timeout=240)
        except subprocess.TimeoutExpired:
            import signal
            os.killpg(proc.pid, signal.SIGTERM)
            proc.wait(timeout=10)
            meta['timeout'] = True
    meta.update({'exit_code': proc.returncode, 'elapsed_seconds': round(time.monotonic()-start, 3),
                 'output_hashes': snapshot(work)})
    final_files = record / 'workspace'
    shutil.copytree(work, final_files, ignore=shutil.ignore_patterns('.git', '__pycache__'))
    (record / 'meta.json').write_text(json.dumps(meta, indent=2)+'\n')
    print(json.dumps({'record': str(record), 'exit_code': proc.returncode,
                      'seconds': meta['elapsed_seconds']}))
