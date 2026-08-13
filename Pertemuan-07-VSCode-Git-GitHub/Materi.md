# Materi Pertemuan 07 — VS Code, Python Lokal, Git, dan GitHub

Pertemuan ini memindahkan workflow dari browser ke komputer lokal. Mahasiswa harus memahami perbedaan editor, interpreter, terminal, repository Git, dan remote GitHub.

## Target
- Menjalankan `.py` dari terminal dan VS Code.
- Membuat `.venv`.
- Menggunakan `git init/status/add/commit`.
- Menghubungkan repository ke GitHub dan melakukan push/pull/clone.
- Membaca status repository dan menggunakan `.gitignore`.

## Mental model
```text
VS Code = editor
Python = interpreter
Terminal = tempat menjalankan perintah
Git = version control lokal
GitHub = remote repository
```

## Struktur project
```text
belajar-python/
├── main.py
├── utils.py
├── README.md
├── requirements.txt
└── .gitignore
```

## Virtual environment
```bash
python -m venv .venv
```
Windows PowerShell: `.venv\Scripts\Activate.ps1`. macOS/Linux: `source .venv/bin/activate`.

## Git workflow
```bash
git init
git status
git add .
git commit -m "feat: tambah program kalkulator"
git remote add origin <URL_REPOSITORY>
git branch -M main
git push -u origin main
```

Commit harus mewakili perubahan stabil dan bermakna, bukan satu commit raksasa di akhir.

## `.gitignore`
```text
.venv/
__pycache__/
.env
*.pyc
.vscode/
```

## Troubleshooting minimum
- `python` tidak dikenali: cek instalasi/PATH dan interpreter VS Code.
- `ModuleNotFoundError`: pastikan environment yang benar aktif.
- `git` tidak dikenali: cek instalasi dan restart terminal.
- push ditolak: cek remote, branch, dan sinkronisasi remote.

## Output
Folder Python lokal, repository GitHub, README, `.gitignore`, dan minimal tiga commit bermakna.