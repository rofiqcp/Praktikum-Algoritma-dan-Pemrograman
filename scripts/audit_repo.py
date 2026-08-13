#!/usr/bin/env python3
from pathlib import Path
import json,py_compile,subprocess,shutil,sys
ROOT=Path(__file__).resolve().parents[1]
MEETINGS=[
'Pertemuan-01-Scratch-Algoritma-Visual','Pertemuan-02-Scratch-Python-Colab-Dasar','Pertemuan-03-Percabangan-Validasi','Pertemuan-04-Loop-Counter-Akumulasi','Pertemuan-05-List-Data-Statistik','Pertemuan-06-Function-Debugging','Pertemuan-07-VSCode-Git-GitHub','Pertemuan-08-Project-Checkpoint-1','Pertemuan-09-Python-Web-Flask','Pertemuan-10-Python-API-REST','Pertemuan-11-Deployment','Pertemuan-12-Project-Checkpoint-2','Pertemuan-13-NodeJS-Express','Pertemuan-14-Node-Python-SQLite','Pertemuan-15-Fullstack-Structured-Backend','Pertemuan-16-Final-Project']
PROJECT={8,12,16}; errors=[]
def need(path):
    if not path.exists():errors.append(f'MISSING {path.relative_to(ROOT)}')
for i,name in enumerate(MEETINGS,1):
    d=ROOT/name;need(d);need(d/'Materi.md');need(d/'Jobsheet.md');need(d/'praktikum');need(d/'praktikum'/'README.md')
    need(d/('Project.md' if i in PROJECT else 'TugasVideo.md'))
    if i in PROJECT and (d/'TugasVideo.md').exists():errors.append(f'UNEXPECTED {name}/TugasVideo.md')
pyfiles=[p for p in ROOT.rglob('*.py') if '.venv' not in p.parts]
for p in pyfiles:
    try:py_compile.compile(str(p),doraise=True)
    except Exception as e:errors.append(f'PYTHON {p.relative_to(ROOT)}: {e}')
for p in [*ROOT.rglob('*.ipynb'),*ROOT.rglob('package.json')]:
    try:json.loads(p.read_text(encoding='utf-8'))
    except Exception as e:errors.append(f'JSON {p.relative_to(ROOT)}: {e}')
node=shutil.which('node');jsfiles=[p for p in ROOT.rglob('*.js') if 'node_modules' not in p.parts]
if node:
    for p in jsfiles:
        r=subprocess.run([node,'--check',str(p)],capture_output=True,text=True)
        if r.returncode:errors.append(f'JS {p.relative_to(ROOT)}: {r.stderr.strip()}')
print(f'Meetings={len(MEETINGS)} Python={len(pyfiles)} JS={len(jsfiles)}')
if errors:
    print('\n'.join(errors));sys.exit(1)
print('Repository audit: PASS')
