# Materi Pertemuan 07 — Instalasi VS Code, Python, Git, dan GitHub

> Sumber utama: *Buku Panduan Praktik: Pemrograman Dasar hingga Full Stack — 16 Pertemuan Terstruktur, Edisi Agustus 2026*. Contoh runnable ada di `praktikum/`.

Peserta berpindah dari notebook browser ke workflow developer lokal. Fokus bukan hanya instalasi, tetapi memahami hubungan editor, interpreter, terminal, repository, dan remote GitHub.

## Target Kompetensi
- Membedakan VS Code, Python interpreter, dan extension Python.
- Menjalankan file `.py` dari VS Code dan terminal.
- Membuat virtual environment.
- Melakukan Git `init/add/commit/push/pull/clone`.
- Membaca status repository dan menghindari commit secret.

## Output Pertemuan
- Folder project Python lokal.
- Repository GitHub berisi program uji, README, dan `.gitignore`.
- Minimal tiga commit yang bermakna.

## Alur Pengajaran 180 Menit
| Tahap | Durasi | Aktivitas |
|---|---:|---|
| Konsep environment | 20 | Editor vs interpreter vs terminal |
| Instalasi | 35 | Python, VS Code, Python extension, Git |
| Project lokal | 25 | Folder, `.py`, terminal |
| venv/pip | 25 | Virtual environment dan package |
| Git lokal | 30 | init, status, add, commit |
| GitHub | 30 | remote, push, pull, clone |
| Troubleshoot | 15 | PATH, interpreter, auth GitHub |

## 7.1 Empat Komponen yang Sering Tertukar
| Komponen | Peran | Bukan |
|---|---|---|
| VS Code | Editor/IDE ringan | Bahasa Python |
| Python interpreter | Mengeksekusi kode Python | Editor |
| Extension Python | Fitur Python di VS Code | Pengganti interpreter |
| Terminal | Menjalankan perintah | GitHub |

## 7.2 Struktur Project Lokal
```text
belajar-python/
├── main.py
├── utils.py
├── README.md
├── requirements.txt
└── .gitignore
```

## 7.3 Virtual Environment
```bash
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
# macOS/Linux
source .venv/bin/activate
python -m pip install requests
python -m pip freeze > requirements.txt
```

Gunakan `python -m pip ...` agar `pip` mengikuti interpreter yang sedang aktif.

## 7.4 Git Workflow Minimum
```bash
git init
git status
git add .
git commit -m "feat: tambah program kalkulator"
git remote add origin <URL_REPOSITORY>
git branch -M main
git push -u origin main
```

Commit harus menjawab “perubahan apa yang baru saja stabil?”. Hindari satu commit raksasa di akhir. Contoh: `feat: tambah validasi nilai`, `fix: cegah pembagian nol`, `docs: tambah cara menjalankan program`.

## 7.5 `.gitignore` Minimum
```gitignore
.venv/
__pycache__/
.env
*.pyc
.vscode/
```

## 7.6 Tes Program
```python
def hitung_diskon(total, member):
    if member and total >= 100_000:
        return total * 0.10
    return 0
```
Program runnable dan test ada di `praktikum/python-local/`.

## 7.7 Troubleshooting Instalasi
| Gejala | Kemungkinan penyebab | Pemeriksaan |
|---|---|---|
| `python` tidak dikenali | PATH/alias | `python --version`, `py --version`, pilih interpreter VS Code |
| `ModuleNotFoundError` | Package di interpreter berbeda | aktifkan venv; `python -m pip show ...` |
| VS Code pakai Python salah | Workspace interpreter belum dipilih | Python: Select Interpreter |
| `git` tidak dikenali | Git belum install/PATH belum reload | restart terminal; `git --version` |
| Push ditolak | Remote/branch/auth | `git remote -v`, `git branch`, pull jika perlu |
| Secret terlanjur commit | `.env` tidak di-ignore | rotasi secret segera; bersihkan history sesuai prosedur |
