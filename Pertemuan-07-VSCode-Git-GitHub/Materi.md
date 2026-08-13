# Materi Pertemuan 07 — Instalasi VS Code, Python, Git, dan GitHub

> Pertemuan ini memindahkan workflow dari notebook browser ke komputer lokal. Fokus bukan hanya instalasi, tetapi memahami hubungan editor, interpreter, terminal, virtual environment, Git repository lokal, dan remote GitHub.

## Target Kompetensi

Mahasiswa mampu:

- membedakan VS Code, Python interpreter, Python extension, dan terminal;
- menjalankan file `.py` melalui terminal dan VS Code;
- memilih interpreter yang benar pada workspace;
- membuat dan mengaktifkan virtual environment;
- menggunakan `pip` dan `requirements.txt` secara dasar;
- menggunakan Git `init`, `status`, `add`, `commit`, dan `log`;
- menghubungkan repository lokal dengan GitHub;
- melakukan `push`, `pull`, dan `clone`;
- menggunakan `.gitignore` untuk file environment lokal;
- membuat commit kecil yang bermakna;
- melakukan pemeriksaan sistematis jika program bekerja di satu terminal tetapi gagal di terminal lain.

## Output Pertemuan

1. Folder project Python lokal.
2. Virtual environment `.venv`.
3. Program Python yang berjalan dari terminal dan VS Code.
4. Unit test sederhana.
5. Repository GitHub.
6. README dan `.gitignore`.
7. Minimal tiga commit bermakna untuk latihan workflow.

---

# 7.1 Lima Komponen yang Sering Tertukar

| Komponen | Fungsi | Bukan |
|---|---|---|
| VS Code | editor/IDE ringan untuk menulis dan mengelola file | bahasa Python |
| Python interpreter | program yang mengeksekusi source Python | editor |
| Python extension | menambahkan linting, run, debug, interpreter selector | pengganti Python interpreter |
| Terminal | tempat menjalankan perintah | GitHub |
| Git | version control lokal | layanan hosting remote |
| GitHub | tempat repository remote dan kolaborasi | pengganti Git lokal |

Mental model:

```text
SOURCE .PY
   ↓
VS CODE menulis file
   ↓
PYTHON INTERPRETER menjalankan file
   ↑
TERMINAL memberi perintah

GIT mencatat perubahan lokal
   ↓ push / ↑ pull
GITHUB menyimpan repository remote
```

---

# 7.2 Struktur Project Lokal

Contoh struktur minimum:

```text
belajar-python/
├── main.py
├── utils.py
├── tests/
│   └── test_utils.py
├── README.md
├── requirements.txt
└── .gitignore
```

Prinsip sederhana:

- `main.py` menjadi entry point program;
- `utils.py` berisi function yang dapat dipakai kembali;
- `tests/` berisi pengujian;
- `README.md` menjelaskan cara menjalankan;
- `requirements.txt` mencatat dependency;
- `.gitignore` menyatakan file/folder yang tidak perlu masuk repository.

---

# 7.3 Menjalankan Python dari Terminal

Cek versi:

```bash
python --version
python -m pip --version
```

Pada beberapa Windows:

```bash
py --version
```

Jalankan file:

```bash
python main.py
```

Jika file berada di folder lain, pastikan terminal berada pada working directory yang tepat.

Periksa lokasi sekarang:

```bash
pwd
```

Pada Windows PowerShell, `pwd` juga dapat digunakan.

---

# 7.4 Interpreter di VS Code

VS Code dapat memiliki beberapa pilihan interpreter. Program dapat bekerja di terminal A tetapi gagal di VS Code jika interpreter yang dipilih berbeda.

Gunakan Command Palette:

```text
Python: Select Interpreter
```

Pilih interpreter yang sesuai dengan project, terutama interpreter dari `.venv` setelah virtual environment dibuat.

Hal yang harus dibandingkan:

```text
terminal interpreter
VS Code selected interpreter
pip location
```

---

# 7.5 Virtual Environment

Buat virtual environment:

```bash
python -m venv .venv
```

Aktivasi Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Aktivasi macOS/Linux:

```bash
source .venv/bin/activate
```

Setelah aktif, cek:

```bash
python --version
python -m pip --version
```

Tujuan `.venv` adalah mengisolasi dependency project. Project A dapat memakai versi package tertentu tanpa harus memengaruhi Project B.

---

# 7.6 `pip` dan `requirements.txt`

Contoh memasang package:

```bash
python -m pip install requests
```

Catat environment:

```bash
python -m pip freeze > requirements.txt
```

Pada environment baru:

```bash
python -m pip install -r requirements.txt
```

Biasakan menggunakan `python -m pip` agar lebih jelas bahwa `pip` yang dipanggil terkait dengan interpreter Python yang aktif.

---

# 7.7 Git sebagai Version Control Lokal

Git mencatat snapshot perubahan source.

Mulai repository:

```bash
git init
```

Lihat kondisi file:

```bash
git status
```

Tambahkan perubahan ke staging area:

```bash
git add .
```

Buat commit:

```bash
git commit -m "feat: tambah program kalkulator"
```

Lihat history:

```bash
git log --oneline
```

---

# 7.8 Working Tree, Staging Area, dan Commit

Mental model:

```text
WORKING TREE
file sedang diedit
      ↓ git add
STAGING AREA
perubahan yang disiapkan
      ↓ git commit
COMMIT HISTORY
snapshot stabil
```

`git add` belum membuat commit. `git commit` belum otomatis mengirim data ke GitHub.

---

# 7.9 Commit yang Bermakna

Commit sebaiknya menjawab:

```text
Perubahan stabil apa yang baru selesai?
```

Contoh:

```text
feat: tambah validasi nilai
fix: cegah pembagian saat data kosong
test: tambah boundary diskon
docs: lengkapi cara menjalankan
```

Hindari pola satu commit besar setelah seluruh pekerjaan selesai karena proses perubahan menjadi sulit ditelusuri.

---

# 7.10 `.gitignore`

Contoh minimum:

```text
.venv/
__pycache__/
.env
*.pyc
.vscode/
```

Alasan:

- `.venv/` dapat dibuat ulang dari dependency;
- `__pycache__/` dan `*.pyc` merupakan artefak runtime;
- `.env` biasanya menyimpan konfigurasi lokal;
- `.vscode/` dapat berisi setting lokal yang tidak selalu perlu dibagikan.

Periksa dengan:

```bash
git status
```

---

# 7.11 Menghubungkan GitHub

Setelah repository remote tersedia:

```bash
git remote add origin <URL_REPOSITORY>
git branch -M main
git push -u origin main
```

Cek remote:

```bash
git remote -v
```

Setelah push, bandingkan Git history lokal dengan commit yang muncul di GitHub.

---

# 7.12 `push`, `pull`, dan `clone`

### Push
Mengirim commit lokal ke remote.

```bash
git push
```

### Pull
Mengambil dan mengintegrasikan perubahan remote ke branch lokal.

```bash
git pull
```

### Clone
Membuat salinan repository ke folder baru.

```bash
git clone <URL_REPOSITORY>
```

Clone penting untuk membuktikan bahwa project tidak hanya berjalan karena kondisi khusus pada folder kerja asli.

---

# 7.13 Testing Project Lokal

Pada starter P07:

```bash
cd praktikum/python-local
python main.py
python -m unittest discover -s tests -v
```

Jika test gagal, jangan langsung mengubah banyak file. Catat:

```text
nama test
expected
actual
function yang diuji
interpreter yang digunakan
```

---

# 7.14 Troubleshooting Environment

| Gejala | Kemungkinan penyebab | Pemeriksaan |
|---|---|---|
| `python` tidak dikenali | instalasi/PATH/alias berbeda | cek `python --version` dan `py --version` |
| package tidak ditemukan | package terpasang pada interpreter lain | cek `.venv`, `python -m pip show` |
| VS Code menjalankan Python berbeda | interpreter workspace salah | gunakan Select Interpreter |
| `git` tidak dikenali | Git belum tersedia di PATH | cek `git --version`, restart terminal |
| push ditolak | remote/branch/sinkronisasi berbeda | cek `git remote -v`, `git branch`, lalu status |
| file yang harus diabaikan muncul | aturan `.gitignore` belum sesuai | cek nama/path dan `git status` |

Prinsip troubleshooting:

```text
REPRODUCE → CEK ENVIRONMENT → BACA OUTPUT → UBAH SATU HAL → RETEST
```

---

# 7.15 Workflow Lengkap P07

```text
BUAT/BUKA FOLDER PROJECT
→ PILIH INTERPRETER
→ BUAT .VENV
→ JALANKAN PROGRAM
→ JALANKAN TEST
→ GIT INIT
→ STATUS
→ ADD
→ COMMIT
→ HUBUNGKAN REMOTE
→ PUSH
→ CLONE/PULL
→ JALANKAN ULANG DARI README
```

---

# 7.16 Praktikum yang Harus Dijalankan

Folder utama:

```text
praktikum/python-local/
```

File penting:

```text
main.py
utils.py
debug_demo.py
test_utils.py
tests/test_utils.py
requirements.txt
.gitignore
README.md
```

Mahasiswa harus menjalankan `main.py` dan test suite, bukan hanya membaca source.

---

# 7.17 Exit Ticket

- [ ] Saya dapat membedakan editor dan interpreter.
- [ ] Saya dapat memilih interpreter VS Code.
- [ ] Saya dapat membuat dan mengaktifkan `.venv`.
- [ ] Saya memahami fungsi `requirements.txt`.
- [ ] Saya memahami working tree, staging area, dan commit.
- [ ] Saya dapat menggunakan `git status`, `add`, `commit`, dan `log`.
- [ ] Saya dapat menghubungkan remote GitHub.
- [ ] Saya memahami `push`, `pull`, dan `clone`.
- [ ] Saya dapat menjelaskan fungsi `.gitignore`.
- [ ] Saya dapat menjalankan project dari folder hasil clone berdasarkan README.
