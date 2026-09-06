"""Verify exact local archive, original measurement oracles and real lifecycle CLI."""
from pathlib import Path
import contextlib,hashlib,importlib.util,io,json,shutil,subprocess,sys,tarfile,tempfile,unittest
ROOT=Path(__file__).resolve().parents[1];R=ROOT/'.backbone-dev/evaluations/candidate-rc5';ARCHIVE=ROOT/'.backbone-dev/releases/vbb-0.1.0-rc.5.tar.gz'
def save(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def load(name,p):
 spec=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(spec);sys.modules[name]=m;spec.loader.exec_module(m);return m
R.mkdir(exist_ok=True);tmp=Path(tempfile.mkdtemp(prefix='vbb-candidate-qualification-'))
with tarfile.open(ARCHIVE) as tar:
 members=tar.getmembers();assert all(m.isfile() and len(Path(m.name).parts)==2 and m.name.startswith('vbb-0.1.0-rc.5/') for m in members);tar.extractall(tmp)
source=tmp/'vbb-0.1.0-rc.5';bundle=json.loads((source/'bundle.json').read_text());assert all(hashlib.sha256((source/n).read_bytes()).hexdigest()==h for n,h in bundle['files'].items())
# Reuse existing independent B1–B6/T1–T6 acceptance cases against the extracted product module.
probe=load('continuity_probe',source/'continuity.py');cases=load('candidate_measurement_cases',ROOT/'.backbone-dev/experiments/deterministic-tools/test_probe.py');stream=io.StringIO();result=unittest.TextTestRunner(stream=stream,verbosity=2).run(unittest.defaultTestLoader.loadTestsFromModule(cases));(R/'measurement-tests.txt').write_text(stream.getvalue());assert result.wasSuccessful()
project=tmp/'project';project.mkdir();(project/'memory').mkdir();(project/'memory/ENTRY.md').write_text('Mandat utilisateur et sources conservés après retrait.\n');(project/'AGENTS.md').write_text('Instruction propre au projet.\n');original={str(p.relative_to(project)):p.read_bytes() for p in project.rglob('*') if p.is_file()}
steps=[]
def cli(args):
 x=subprocess.run([sys.executable,'-B',str(source/'vbb.py')]+args,cwd=project,capture_output=True,text=True);steps.append({'argv':args,'returncode':x.returncode,'stdout':x.stdout,'stderr':x.stderr});return x
assert cli(['install','--project',str(project)]).returncode==0
assert cli(['install','--project',str(project)]).returncode==0
assert cli(['inspect','--project',str(project)]).returncode==0
(project/'p.txt').write_text('abc');(project/'baseline.json').write_text(json.dumps({'name':'A','files':{'p.txt':{'size':3,'sha256':hashlib.sha256(b'abc').hexdigest()}}}));(project/'selection.json').write_text('{"paths":["p.txt"]}')
x=subprocess.run([sys.executable,'-B',str(project/'.vbb/vbb.py'),'compare','--root',str(project),'--baseline',str(project/'baseline.json'),'--baseline-name','A','--request',str(project/'selection.json')],capture_output=True,text=True);steps.append({'operation':'installed compare CLI','rc':x.returncode,'output':json.loads(x.stdout)});assert x.returncode==0
(project/'p.txt').write_text('abd');x=subprocess.run([sys.executable,'-B',str(project/'.vbb/vbb.py'),'compare','--root',str(project),'--baseline',str(project/'baseline.json'),'--baseline-name','A','--request',str(project/'selection.json')],capture_output=True,text=True);steps.append({'operation':'installed changed compare CLI','rc':x.returncode,'output':json.loads(x.stdout)});assert x.returncode==1
for n in ['p.txt','baseline.json','selection.json']:(project/n).unlink()
assert cli(['remove','--project',str(project)]).returncode==0
assert {str(p.relative_to(project)):p.read_bytes() for p in project.rglob('*') if p.is_file()}==original
assert cli(['remove','--project',str(project)]).returncode==0
# Same artifact exact bytes remain reproducible through the explicit source list.
for n,h in bundle['files'].items():assert hashlib.sha256((ROOT/'product'/n).read_bytes()).hexdigest()==h
save(R/'local-validation.json',{'archive_sha256':hashlib.sha256(ARCHIVE.read_bytes()).hexdigest(),'archive_members':[m.name for m in members],'measurement_tests_run':result.testsRun,'measurement_tests_pass':result.wasSuccessful(),'lifecycle_tests':'22 lifecycle tests plus 2 measurement CLI regressions, separately executed on same archive','real_cli_steps':steps,'memory_and_user_agents_after_removal_equal':True,'source_equals_archive':True,'qualification_workspace':str(tmp),'harness_qualification':'pending','release_candidate_qualified':False})
print(json.dumps({'measurement_tests':result.testsRun,'cli_roundtrip':'PASS','archive_sha256':hashlib.sha256(ARCHIVE.read_bytes()).hexdigest(),'harnesses':'pending'}))
