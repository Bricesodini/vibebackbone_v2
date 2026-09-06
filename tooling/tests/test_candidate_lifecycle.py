"""Behavioral lifecycle tests on bytes extracted from the candidate archive."""
from pathlib import Path
import importlib.util,json,hashlib,shutil,tarfile,tempfile,unittest,os
from unittest.mock import patch
ROOT=Path(__file__).resolve().parents[2]
ARCHIVE=Path(os.environ.get('VBB_TEST_ARCHIVE',str(ROOT/'.backbone-dev/releases/vbb-0.1.0-rc.5.tar.gz')))

class Lifecycle(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory(prefix='vbb-lifecycle-');self.addCleanup(self.tmp.cleanup);self.base=Path(self.tmp.name)
        with tarfile.open(ARCHIVE) as tar:
            names=tar.getnames();self.assertEqual(len(names),6);prefix=Path(names[0]).parts[0]
            self.assertTrue(all(n.startswith(prefix+'/') and len(Path(n).parts)==2 for n in names))
            tar.extractall(self.base)
        self.source=self.base/prefix;spec=importlib.util.spec_from_file_location('candidate_lifecycle',self.source/'vbb.py');self.v=importlib.util.module_from_spec(spec);spec.loader.exec_module(self.v)
        self.project=self.base/'project';self.project.mkdir();(self.project/'memory').mkdir();(self.project/'memory/reprise.md').write_text('User memory remains readable.\n');(self.project/'data.csv').write_bytes(b'user,data\n')
    def install(self,**kw):return self.v.install(self.v.project_root(self.project),self.source,**kw)
    def snapshot(self):return {str(p.relative_to(self.project)):p.read_bytes() for p in self.project.rglob('*') if p.is_file() and not p.is_symlink()}
    def new_version(self):
        p=self.source/'README.md';p.write_text(p.read_text()+'\nAdditional version.\n');m=json.loads((self.source/'bundle.json').read_text());m['version']='0.1.0-rc.999';m['files']['README.md']=hashlib.sha256(p.read_bytes()).hexdigest();(self.source/'bundle.json').write_text(json.dumps(m))
    def measurement_cli(self, request, source=None):
        import subprocess, sys
        path=self.base/'selection.json';path.write_text(json.dumps(request))
        x=subprocess.run([sys.executable,'-B',str(self.source/'vbb.py'),'inventory','--source',str(source or self.project),'--destination',str(self.project),'--request',str(path)],capture_output=True,text=True)
        self.assertEqual(x.returncode,2,x.stderr);self.assertEqual(json.loads(x.stdout)['exit_code'],2);self.assertNotIn('Traceback',x.stderr)
    def test_measurement_unencodable_path_is_structured_error(self):
        self.measurement_cli({'paths':[chr(0xd800)]})
    def test_measurement_loop_root_is_structured_error(self):
        loop=self.base/'loop';loop.symlink_to('loop');self.measurement_cli({'paths':['memory/reprise.md']},loop)
    def test_crash_temporary_is_reported_and_preserved(self):
        self.install()
        # A subprocess exits without finally after creating the AGENTS temporary.
        import subprocess, sys
        script = "import importlib.util, os; from pathlib import Path; s=importlib.util.spec_from_file_location('v', %r); v=importlib.util.module_from_spec(s); s.loader.exec_module(v); v.os.replace=lambda *a: os._exit(77); v.atomic(Path(%r), b'user rules and pending VBB block')" % (str(self.source/'vbb.py'), str(self.project/'AGENTS.md'))
        x=subprocess.run([sys.executable,'-B','-c',script]);self.assertEqual(x.returncode,77)
        self.assertEqual(list(self.project.glob('.vbb-write-*')),[])
        leftovers=list((self.project/'.vbb').glob('.vbb-write-*'));self.assertEqual(len(leftovers),1)
        data=leftovers[0].read_bytes();self.assertIn(leftovers[0].name,self.v.inspect(self.project)['residues'])
        result=self.v.remove(self.project);self.assertEqual(result['state'],'retired_with_residues');self.assertIn('.vbb/'+leftovers[0].name,result['preserved']);self.assertEqual(leftovers[0].read_bytes(),data)
    def test_remove_final_empty_gap_can_repeat(self):
        self.install();real=Path.rmdir
        def fail(path):
            if path==self.project/'.vbb':raise OSError('interrupted after receipt unlink')
            return real(path)
        with patch.object(Path,'rmdir',fail):
            with self.assertRaises(OSError):self.v.remove(self.project)
        self.assertEqual(list((self.project/'.vbb').iterdir()),[])
        self.assertEqual(self.v.inspect(self.project)['state'],'empty')
        self.assertEqual(self.v.remove(self.project)['state'],'removed');self.assertFalse((self.project/'.vbb').exists())
    def test_new_install_repeat_remove_preserve_data(self):
        original=self.snapshot();self.install();snap=self.snapshot();self.install();self.assertEqual(snap,self.snapshot());self.assertEqual((self.project/'AGENTS.md').read_bytes().count(b'VBB:BEGIN'),1)
        self.assertEqual(self.v.remove(self.project)['state'],'removed');self.assertEqual(original,self.snapshot());self.assertEqual(self.v.remove(self.project)['state'],'absent')
    def test_existing_agents_bytes_and_later_user_addition(self):
        ap=self.project/'AGENTS.md';before='User rule sans newline: é'.encode();ap.write_bytes(before);self.install();ap.write_bytes(ap.read_bytes()+b'\nAnother user rule\n');self.v.remove(self.project);self.assertEqual(ap.read_bytes(),before+b'\nAnother user rule\n')
    def test_empty_existing_agents_stays(self):
        p=self.project/'AGENTS.md';p.touch();self.install();self.v.remove(self.project);self.assertEqual(p.read_bytes(),b'')
    def test_divergent_payload_update_refused_remove_preserves(self):
        self.install();p=self.project/'.vbb/agreement.md';p.write_text('User changed agreement');snap=self.snapshot();self.new_version()
        with self.assertRaises(self.v.Refusal):self.install(update=True)
        self.assertEqual(snap,self.snapshot());r=self.v.remove(self.project);self.assertEqual(r['state'],'retired_with_residues');self.assertEqual(p.read_text(),'User changed agreement');self.assertIn('.vbb/agreement.md',r['preserved']);self.assertEqual((self.project/'memory/reprise.md').read_text(),'User memory remains readable.\n')
    def test_divergent_agents_blocks_install_and_is_preserved(self):
        self.install();ap=self.project/'AGENTS.md';ap.write_bytes(ap.read_bytes().replace(b'Une demande triviale',b'Changed policy'))
        snap=self.snapshot()
        with self.assertRaises(self.v.Refusal):self.install()
        self.assertEqual(snap,self.snapshot());self.v.remove(self.project);self.assertEqual(ap.read_bytes(),snap['AGENTS.md'])
    def test_missing_owned_file_repaired(self):
        self.install();p=self.project/'.vbb/continuity.py';p.unlink();self.assertEqual(self.v.inspect(self.project)['files']['continuity.py'],'missing');self.install();self.assertEqual(p.read_bytes(),(self.source/'continuity.py').read_bytes())
    def test_update_explicit_and_removable(self):
        original=self.snapshot();self.install();self.new_version();snap=self.snapshot()
        with self.assertRaises(self.v.Refusal):self.install()
        self.assertEqual(snap,self.snapshot());r=self.install(update=True);self.assertEqual(r['version'],'0.1.0-rc.999');self.assertEqual((self.project/'.vbb/README.md').read_bytes(),(self.source/'README.md').read_bytes());self.v.remove(self.project);self.assertEqual(self.snapshot(),original)
    def test_interrupted_install_inspect_resume_same_bundle(self):
        real=self.v.atomic;calls=0
        def fail(path,data):
            nonlocal calls
            calls+=1
            if calls==3:raise OSError('simulated interruption')
            real(path,data)
        with patch.object(self.v,'atomic',side_effect=fail):
            with self.assertRaises(OSError):self.install()
        self.assertEqual(self.v.inspect(self.project)['state'],'pending');self.install();self.assertEqual(self.v.inspect(self.project)['state'],'installed');self.v.remove(self.project);self.assertFalse((self.project/'.vbb').exists())
    def test_interrupted_update_resume_and_other_bundle_refused(self):
        self.install();self.new_version();real=self.v.atomic
        def fail(path,data):
            if path.name=='bundle.json':raise OSError('interrupted update')
            real(path,data)
        with patch.object(self.v,'atomic',side_effect=fail):
            with self.assertRaises(OSError):self.install(update=True)
        self.assertEqual(self.v.inspect(self.project)['state'],'pending');self.install(update=True);self.assertEqual(self.v.inspect(self.project)['state'],'installed')
    def test_pending_different_bundle_refused_and_removable(self):
        real=self.v.atomic
        def fail(path,data):
            if path.name=='continuity.py':raise OSError('stop')
            real(path,data)
        with patch.object(self.v,'atomic',side_effect=fail):
            with self.assertRaises(OSError):self.install()
        self.new_version();snap=self.snapshot()
        with self.assertRaises(self.v.Refusal):self.install(update=True)
        self.assertEqual(snap,self.snapshot());self.assertEqual(self.v.remove(self.project)['state'],'removed')
    def test_unknown_files_preserved_on_remove(self):
        self.install();p=self.project/'.vbb/user-note.md';p.write_text('mine');r=self.v.remove(self.project);self.assertEqual(p.read_text(),'mine');self.assertIn('.vbb/user-note.md',r['preserved']);self.assertEqual(self.v.inspect(self.project)['state'],'retired')
    def test_foreign_directory_and_markers_refused(self):
        d=self.project/'.vbb';d.mkdir();(d/'user').write_text('mine');snap=self.snapshot()
        with self.assertRaises(self.v.Refusal):self.install()
        self.assertEqual(snap,self.snapshot());shutil.rmtree(d);(self.project/'AGENTS.md').write_bytes(self.v.BLOCK)
        with self.assertRaises(self.v.Refusal):self.install()
    def test_symlinks_preserved(self):
        target=self.base/'outside';target.write_text('outside');(self.project/'.vbb').symlink_to(self.base,target_is_directory=True)
        with self.assertRaises(self.v.Refusal):self.v.project_root(self.project)
        (self.project/'.vbb').unlink();self.install();p=self.project/'.vbb/agreement.md';p.unlink();p.symlink_to(target);self.v.remove(self.project);self.assertTrue(p.is_symlink());self.assertEqual(target.read_text(),'outside')
    def test_agents_symlink_refused_before_mutation(self):
        self.install();p=self.project/'AGENTS.md';p.unlink();target=self.base/'outside';target.write_text('outside');p.symlink_to(target)
        with self.assertRaises(self.v.Refusal):self.v.project_root(self.project)
        self.assertTrue((self.project/'.vbb/vbb.py').exists());self.assertEqual(target.read_text(),'outside')
    def test_corrupt_bundle_and_receipt_refused(self):
        (self.source/'README.md').write_text('tamper')
        with self.assertRaises(self.v.Refusal):self.install()
        self.assertFalse((self.project/'.vbb').exists())
    def test_receipt_escape_refused_without_deleting(self):
        self.install();p=self.project/'.vbb/receipt.json';v=json.loads(p.read_text());v['files']['../data.csv']=hashlib.sha256((self.project/'data.csv').read_bytes()).hexdigest();p.write_text(json.dumps(v));snap=self.snapshot()
        with self.assertRaises(self.v.Refusal):self.v.remove(self.project)
        self.assertEqual(snap,self.snapshot())
    def test_factory_and_descendant_refused(self):
        (self.project/'.backbone-dev').mkdir();child=self.project/'child';child.mkdir()
        for p in [self.project,child]:
            with self.assertRaises(self.v.Refusal):self.v.project_root(p)
        self.assertFalse((self.project/'.vbb').exists())

    def test_pending_install_with_existing_agents_can_be_removed(self):
        ap=self.project/'AGENTS.md';ap.write_bytes(b'Original user instructions\n');original=self.snapshot();real=self.v.atomic
        def fail(path,data):
            if path.name=='continuity.py':raise OSError('stop before AGENTS')
            real(path,data)
        with patch.object(self.v,'atomic',side_effect=fail):
            with self.assertRaises(OSError):self.install()
        self.assertEqual(self.v.remove(self.project)['state'],'removed');self.assertEqual(self.snapshot(),original)
    def test_remove_interrupted_after_agents_replace_can_repeat(self):
        ap=self.project/'AGENTS.md';ap.write_bytes(b'Original user instructions\n');original=self.snapshot();self.install();real=self.v.atomic
        def fail(path,data):
            real(path,data)
            if path.name=='AGENTS.md':raise OSError('crash after AGENTS replacement')
        with patch.object(self.v,'atomic',side_effect=fail):
            with self.assertRaises(OSError):self.v.remove(self.project)
        self.assertEqual(self.v.remove(self.project)['state'],'removed');self.assertEqual(self.snapshot(),original)
    def test_agents_permissions_preserved_through_cycle(self):
        import stat
        ap=self.project/'AGENTS.md';ap.write_text('group-readable rules');ap.chmod(0o640);self.install();self.assertEqual(stat.S_IMODE(ap.stat().st_mode),0o640);self.v.remove(self.project);self.assertEqual(stat.S_IMODE(ap.stat().st_mode),0o640)

if __name__=='__main__':unittest.main()
