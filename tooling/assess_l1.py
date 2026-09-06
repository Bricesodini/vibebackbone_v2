"""Recheck final artifacts against frozen L0 oracles. No model calls."""
import json
import subprocess
import sys
import tempfile
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RUNS = ROOT / '.backbone-dev/evaluations/l1/runs'
CHECKS = {
    'small': "from quote import total; assert total([(4,20),(2,15)]) == 110; assert total([]) == 0",
    'repair': "from tags import normalize; assert normalize(['B',' a ', 'b', '']) == ['b','a']; assert normalize([]) == []",
    'scope': "from preview import candidates; import json; d=json.load(open('accounts.json')); assert candidates(d,30)==['b','c']; assert candidates(d,90)==['c']",
    'resume': "from formatter import format_amount; assert format_amount(-123)=='-1,23'; assert format_amount(9007199254740993)=='90071992547409,93'",
}

if __name__ == '__main__':
    fixtures = json.loads((ROOT / '.backbone-dev/corpus/development/missions.json').read_text())
    rows = []
    for record in sorted(RUNS.iterdir()):
        if record.name.startswith('preflight') or not (record/'meta.json').exists():
            continue
        meta = json.loads((record/'meta.json').read_text())
        if 'exit_code' not in meta:
            continue
        work = record/'workspace'
        events = [json.loads(line) for line in (record/'events.jsonl').read_text().splitlines() if line.strip()]
        usage = [e.get('usage') for e in events if e.get('type') == 'turn.completed']
        result = {'case':meta['case'], 'variant':meta['variant'], 'exit_code':meta['exit_code'],
                  'duration_seconds':meta['elapsed_seconds'], 'usage':usage[-1] if usage else None,
                  'native_turn_completed':bool(usage), 'behavioral_review':'see behavioral-review.json (separate author review)',
                  'human_time_total':None, 'money_cost':None}
        results = {}
        for label, cmd in [('fixture_tests',[sys.executable,'-m','unittest','discover','-v']),
                           ('frozen_oracle',[sys.executable,'-c',CHECKS[meta['case']]])]:
            try:
                p = subprocess.run(cmd, cwd=work, capture_output=True, text=True, timeout=20)
                results[label] = {'exit_code':p.returncode, 'stdout':p.stdout, 'stderr':p.stderr}
            except subprocess.TimeoutExpired:
                results[label] = {'exit_code':None,'timeout':True}
        with tempfile.TemporaryDirectory(prefix='vbb-l1-original-tests-') as temp:
            original_work = Path(temp)/'project'
            shutil.copytree(work, original_work, ignore=shutil.ignore_patterns('__pycache__', '.agents'))
            for name, content in fixtures[meta['case']]['files'].items():
                if name.startswith('test_'):
                    (original_work/name).write_text(content)
            p = subprocess.run([sys.executable,'-m','unittest','discover','-v'],
                               cwd=original_work,capture_output=True,text=True,timeout=20)
            results['original_fixture_tests'] = {'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr}
        result['original_fixture_tests_pass'] = results['original_fixture_tests']['exit_code']==0
        protected = ['accounts.json'] if meta['case']=='scope' else ['amounts.json'] if meta['case']=='resume' else []
        result['protected_files_unchanged'] = all((work/p).read_text()==fixtures[meta['case']]['files'][p] for p in protected)
        result['oracle_pass'] = results['frozen_oracle']['exit_code']==0
        result['fixture_tests_pass'] = results['fixture_tests']['exit_code']==0
        result['verification'] = results
        (record/'assessment.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
        rows.append({k:v for k,v in result.items() if k != 'verification'})
    (RUNS.parent/'comparison.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(rows,ensure_ascii=False,indent=2))
