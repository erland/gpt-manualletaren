from pathlib import Path
import argparse,zipfile,subprocess,sys
ROOT=Path(__file__).resolve().parents[1]
def main():
 parser=argparse.ArgumentParser();parser.add_argument('--version',required=True); args=parser.parse_args()
 subprocess.run(['python3',str(ROOT/'scripts/validate_project.py')],check=True)
 subprocess.run([sys.executable,str(ROOT/'scripts/build_distributions.py'),'--version',args.version],check=True)
 out=ROOT.parent/f'manualletaren-project-v{args.version}.zip'
 with zipfile.ZipFile(out,'w',compression=zipfile.ZIP_DEFLATED) as z:
  for file in sorted(ROOT.rglob('*')):
   if file.is_file() and '__pycache__' not in file.parts and '.pyc' not in file.suffix: z.write(file,arcname=f'manualletaren/{file.relative_to(ROOT)}')
 with zipfile.ZipFile(out) as z: assert z.testzip() is None
 print(out)
if __name__=='__main__': main()
