"""Check fairness and integrity of completed trials, without calling a model."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RUNS = ROOT / '.backbone-dev/evaluations/l1/runs'

def sha(data):
    return hashlib.sha256(data).hexdigest()

if __name__ == '__main__':
    fixtures_path = ROOT / '.backbone-dev/corpus/development/missions.json'
    fixtures = json.loads(fixtures_path.read_text())
    checks = []
    for case, fixture in fixtures.items():
        pair = []
        test_changes = {}
        for variant in ['M0', 'VBB']:
            run = RUNS / f'{case}-{variant}'
            meta = json.loads((run/'meta.json').read_text())
            assert meta['fixture_sha256'] == sha(fixtures_path.read_bytes())
            assert meta['prompt_sha256'] == sha((run/'prompt.txt').read_bytes())
            assert meta['exit_code'] == 0
            for name, content in fixture['files'].items():
                assert meta['input_hashes'][name] == sha(content.encode())
            for name, digest in meta['output_hashes'].items():
                assert sha((run/'workspace'/name).read_bytes()) == digest, (run, name)
            test_changes[variant] = [name for name in fixture['files']
                if name.startswith('test_') and meta['input_hashes'][name] != meta['output_hashes'].get(name)]
            skill_files = {k:v for k,v in meta['input_hashes'].items() if k.startswith('.agents/')}
            if variant == 'M0':
                assert not skill_files
            else:
                for name, digest in skill_files.items():
                    assert meta['output_hashes'][name] == digest
            pair.append(meta)
        assert pair[0]['harness_version'] == pair[1]['harness_version']
        for flag in ['-m', '-c', '-s']:
            # The complete command, excluding cwd and output path, is compared below.
            assert flag in pair[0]['command'] and flag in pair[1]['command']
        def normalized(cmd):
            cmd = list(cmd)
            for flag in ['-C', '-o']:
                cmd[cmd.index(flag)+1] = '<path>'
            return cmd
        assert normalized(pair[0]['command']) == normalized(pair[1]['command'])
        native = (RUNS/f'{case}-M0/prompt.txt').read_text()
        vbb = (RUNS/f'{case}-VBB/prompt.txt').read_text()
        assert vbb.replace('\nUtilise $vbb-work dans .agents/skills/vbb-work/SKILL.md pour cette mission.', '') == native
        assert pair[0]['workspace'] != pair[1]['workspace']
        checks.append({'case':case,'common_inputs_and_settings_equal':True,
                       'archived_final_hashes_match':True,'changed_test_files':test_changes})
    for relative in ['.agents', '.vbb', '.pi', '.codex']:
        assert not (ROOT/relative).exists()
    result = {'checks':checks,'factory_discovery_paths_absent':True,
              'scope':'declared inputs and archived output bytes; not exhaustive native context attestation'}
    (RUNS.parent/'integrity.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
