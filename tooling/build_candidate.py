"""Build a deterministic local archive from an explicit product-only source list."""
from pathlib import Path
import gzip,hashlib,io,json,tarfile
from check_boundary import source_files
ROOT=Path(__file__).resolve().parents[1]
VERSION='0.1.0-rc.5'
PAYLOAD=['vbb.py','continuity.py','agreement.md','README.md','profiles.md']
def build():
 product=ROOT/'product'
 manifest={'schema':1,'version':VERSION,'files':{n:hashlib.sha256((product/n).read_bytes()).hexdigest() for n in PAYLOAD}}
 (product/'bundle.json').write_text(json.dumps(manifest,indent=2,sort_keys=True)+'\n')
 sources=source_files(ROOT,json.loads((ROOT/'tooling/distribution.json').read_text()))
 assert {p.name for p in sources}==set(PAYLOAD)|{'bundle.json'}
 buf=io.BytesIO()
 with tarfile.open(fileobj=buf,mode='w',format=tarfile.USTAR_FORMAT) as tar:
  for p in sorted(sources):
   data=p.read_bytes();info=tarfile.TarInfo(f'vbb-{VERSION}/{p.name}');info.size=len(data);info.mode=0o644;info.mtime=0;tar.addfile(info,io.BytesIO(data))
 out=ROOT/'.backbone-dev/releases';out.mkdir(exist_ok=True)
 archive=out/f'vbb-{VERSION}.tar.gz';data=gzip.compress(buf.getvalue(),mtime=0)
 if archive.exists() and archive.read_bytes()!=data:raise RuntimeError('Existing candidate differs; choose a new candidate version, never overwrite evidence')
 archive.write_bytes(data)
 report={'version':VERSION,'archive':str(archive),'sha256':hashlib.sha256(archive.read_bytes()).hexdigest(),'files':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sources},'status':'candidate_pending_qualification'}
 (out/f'vbb-{VERSION}.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
if __name__=='__main__':build()
