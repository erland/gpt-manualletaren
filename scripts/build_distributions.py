from pathlib import Path
import argparse, hashlib, io, json, zipfile
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'dist'
TARGETS=('chatgpt-chat','openai-plugin','claude-projects','claude-skills','opencode')
def put(z,name,data):
    z.writestr(name,data)
def build(version):
    OUT.mkdir(exist_ok=True)
    canonical=(ROOT/'src/canonical/instructions.md').read_text(encoding='utf-8')
    ref_files=['docs/IDENTIFICATION.md','docs/MANUAL-SEARCH.md','docs/RUNTIME-PARITY.md']
    refs={p:(ROOT/p).read_bytes() for p in ref_files}
    results=[]
    for target in TARGETS:
        path=OUT/f'manualletaren-{target}-v{version}.zip'
        with zipfile.ZipFile(path,'w',compression=zipfile.ZIP_DEFLATED) as z:
            readme=(f'# Manualletaren – {target}\n\nDistribution genererad från canonical instruktion. '
                    'Webbsökning, länkåtkomst och läsning av manual måste kontrolleras i faktisk host. '
                    'Denna distribution är EJ hostverifierad och EJ aktiverad.\n')
            put(z,'README.md',readme)
            if target=='chatgpt-chat':
                put(z,'START-HERE.md','# Starta här\n\nAnvänd instruktionen i instructions.md som assistentens beteende. Läs referenser vid behov. Verktyg måste testas i ChatGPT.\n')
                put(z,'instructions.md',canonical)
            elif target=='openai-plugin':
                put(z,'skills/manualletaren/SKILL.md','---\nname: manualletaren\ndescription: Hitta rätt användarmanual med säker produktidentifiering och källkontroll.\n---\n\n'+canonical)
            elif target=='claude-projects':
                put(z,'PROJECT-INSTRUCTIONS.md',canonical)
                put(z,'INSTALL.md','Lägg instruktionerna i Claude Projects och referenser som projektmaterial. Verifiera webbsökning och PDF-läsning.\n')
            elif target=='claude-skills':
                put(z,'manualletaren/SKILL.md','---\nname: manualletaren\ndescription: Find verified product manuals and disambiguate product variants.\n---\n\n'+canonical)
            elif target=='opencode':
                put(z,'.opencode/skills/manualletaren/SKILL.md','---\nname: manualletaren\ndescription: Leta upp produktmanualer med källstöd och modellverifiering.\n---\n\n'+canonical)
                put(z,'INSTALL.md','Aktivera kompatibla webbsök-/fetchverktyg i OpenCode. PDF-innehåll måste kunna läsas för verifieringsstatus.\n')
            for name, content in refs.items():
                folder='manualletaren/references' if target=='claude-skills' else ('.opencode/skills/manualletaren/references' if target=='opencode' else ('skills/manualletaren/references' if target=='openai-plugin' else 'references'))
                put(z,f'{folder}/{Path(name).name}',content)
            put(z,'COMPATIBILITY.json',json.dumps({'runtime':target,'host_verified':False,'activated':False,'required_host_capabilities':['web_search','source_access','manual_content_read'],'canonical_sha256':hashlib.sha256(canonical.encode()).hexdigest()},ensure_ascii=False,indent=2))
        with zipfile.ZipFile(path) as z:
            assert z.testzip() is None
            assert not any(n.endswith('mcp.json') for n in z.namelist())
        results.append({'runtime':target,'file':path.name,'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'status':'packaged_not_host_verified'})
    (OUT/'manifest.json').write_text(json.dumps({'version':version,'distributions':results},indent=2,ensure_ascii=False)+'\n')
    return results
if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--version',required=True);args=parser.parse_args()
    print(json.dumps(build(args.version),indent=2))
