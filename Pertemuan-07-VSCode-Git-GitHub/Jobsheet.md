# Jobsheet Pertemuan 07 — VS Code, Python Lokal, Git, dan GitHub

## Identitas

| Item | Isian |
|---|---|
| Nama |  |
| NIM |  |
| Kelas |  |
| OS | Windows / macOS / Linux |
| Versi Python |  |
| Versi Git |  |
| Link repository latihan |  |

## Tujuan Praktikum

Mahasiswa membuktikan workflow lokal end-to-end:

```text
EDITOR → PYTHON INTERPRETER → TERMINAL → VENV → PROGRAM → TEST
→ GIT LOCAL → REMOTE GITHUB → CLONE/PULL
```

Setelah praktikum mahasiswa harus dapat menjelaskan fungsi setiap komponen, bukan hanya mengikuti perintah.

---

# P01 — Verifikasi Instalasi

Jalankan di terminal:

```bash
python --version
python -m pip --version
git --version
```

Pada sebagian Windows, perintah Python dapat berupa:

```bash
py --version
```

Catat hasil:

| Komponen | Perintah | Hasil |
|---|---|---|
| Python |  |  |
| pip |  |  |
| Git |  |  |
| VS Code | cek About |  |

Jawab: mana yang merupakan editor, interpreter, extension, terminal, version control, dan hosting repository?

---

# P02 — Buka Project Lokal di VS Code

Buka folder:

```text
Pertemuan-07-VSCode-Git-GitHub/praktikum/python-local/
```

Kenali file:

```text
main.py
utils.py
README.md
requirements.txt
.gitignore
```

Jalankan:

```bash
python main.py
```

Kemudian jalankan file yang sama melalui tombol Run Python File di VS Code. Pastikan interpreter yang dipakai sama.

### Observasi

| Cara menjalankan | Interpreter | Output | Sama? |
|---|---|---|:---:|
| terminal |  |  | ☐ |
| VS Code |  |  | ☐ |

---

# P03 — Virtual Environment

Dari folder project:

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

Verifikasi interpreter:

```bash
python --version
python -m pip --version
```

Di VS Code pilih **Python: Select Interpreter** lalu pilih interpreter dari `.venv`.

### Pertanyaan

1. Mengapa `.venv` dibuat per project?
2. Apa akibat memasang package pada interpreter berbeda dengan interpreter yang menjalankan program?
3. Mengapa `.venv/` tidak seharusnya di-commit?

---

# P04 — Package dan requirements.txt

Sesuai panduan, lakukan latihan package:

```bash
python -m pip install requests
python -m pip freeze > requirements.txt
```

Lihat isi `requirements.txt`. Tujuan latihan ini adalah memahami bahwa dependency project dapat dicatat sehingga environment lain dapat menyiapkannya kembali.

Untuk instalasi dari requirements:

```bash
python -m pip install -r requirements.txt
```

---

# P05 — Menjalankan Test

Dari `praktikum/python-local`:

```bash
python -m unittest discover -s tests -v
```

Catat:

| Test | Expected | Actual | Pass |
|---|---|---|:---:|
| test 1 |  |  | ☐ |
| test 2 |  |  | ☐ |

Jika test gagal, baca nama test, expected, actual, dan function yang diuji sebelum mengubah source.

---

# P06 — Git Repository Lokal

Pada salinan folder latihan atau project baru:

```bash
git init
git status
```

Perhatikan bahwa file belum otomatis masuk commit.

Tambahkan file:

```bash
git add .
git status
```

Buat commit:

```bash
git commit -m "chore: siapkan project Python lokal"
```

Lakukan perubahan kecil yang stabil lalu commit lagi. Target latihan minimal **3 commit bermakna**.

Contoh:

```text
chore: siapkan project Python lokal
feat: tambah perhitungan diskon
 test: tambah test boundary
 docs: lengkapi README
```

---

# P07 — Memahami Working Tree dan Staging Area

Eksperimen:

1. ubah README;
2. jalankan `git status`;
3. `git add README.md`;
4. jalankan `git status` lagi;
5. ubah README sekali lagi tanpa `git add`;
6. amati perbedaannya.

Tuliskan kesimpulan:

```text
working tree =
staging area =
commit =
```

---

# P08 — `.gitignore`

Pastikan berisi minimal:

```text
.venv/
__pycache__/
.env
*.pyc
.vscode/
```

Buat file `.env` dummy **tanpa secret nyata**, misalnya:

```text
DEMO_KEY=placeholder
```

Jalankan:

```bash
git status
```

Pastikan `.env` tidak muncul sebagai file yang akan di-commit.

---

# P09 — Remote GitHub dan Push

Buat repository GitHub latihan sesuai arahan pengajar, kemudian:

```bash
git remote add origin <URL_REPOSITORY>
git branch -M main
git push -u origin main
```

Verifikasi:

```bash
git remote -v
git log --oneline
```

Buka GitHub dan cocokkan file serta commit.

---

# P10 — Pull dan Clone

## Pull

Lakukan satu perubahan dokumentasi melalui workflow yang disetujui pengajar, kemudian sinkronkan:

```bash
git pull
```

## Clone

Di folder lain:

```bash
git clone <URL_REPOSITORY>
cd <NAMA_REPOSITORY>
```

Coba jalankan program berdasarkan README.

Tujuannya membuktikan repository dapat dipakai dari lokasi baru, bukan hanya bekerja pada folder asal.

---

# P11 — Troubleshooting Instalasi

Lengkapi tabel berikut berdasarkan eksperimen atau simulasi pengajar.

| Gejala | Pemeriksaan pertama | Bukti | Solusi |
|---|---|---|---|
| `python` tidak dikenali |  |  |  |
| package tidak ditemukan |  |  |  |
| VS Code memilih interpreter lain |  |  |  |
| `git` tidak dikenali |  |  |  |
| push ditolak |  |  |  |

Gunakan prinsip: cek environment dan bukti terlebih dahulu, jangan mengubah banyak konfigurasi sekaligus.

---

# P12 — Git History Berkualitas

Tampilkan:

```bash
git log --oneline
```

Evaluasi setiap commit dengan pertanyaan:

- apakah pesannya menjelaskan perubahan?
- apakah perubahan cukup kecil untuk dipahami?
- apakah commit dibuat saat kondisi stabil?
- apakah seluruh project baru muncul dalam satu commit besar?

---

# Bukti Wajib

- output `python --version` dan `git --version`;
- interpreter VS Code yang dipilih;
- `.venv` aktif;
- output program lokal;
- hasil unit test;
- `git status` pada beberapa tahap;
- `.gitignore` bekerja;
- `git log --oneline` minimal tiga commit;
- repository GitHub;
- bukti clone/pull;
- README yang dapat diikuti.

## Pertanyaan Analisis

1. Apa beda VS Code dan Python interpreter?
2. Apa fungsi extension Python?
3. Mengapa package dapat terlihat terpasang tetapi program tetap tidak menemukannya?
4. Apa fungsi staging area Git?
5. Apa beda Git dengan GitHub?
6. Apa beda `git add`, `git commit`, dan `git push`?
7. Mengapa commit kecil yang bermakna lebih mudah ditinjau?
8. Mengapa `.env` dan `.venv` di-ignore?
9. Mengapa repository perlu diuji dengan clone ke folder lain?
10. Apa bukti bahwa local repository dan remote sudah sinkron?

## Checklist Selesai

- [ ] Program berjalan dari terminal.
- [ ] Program berjalan dari VS Code dengan interpreter yang benar.
- [ ] `.venv` berhasil dibuat dan dipilih.
- [ ] Unit test dijalankan.
- [ ] Git repository lokal dibuat.
- [ ] Minimal tiga commit bermakna tersedia.
- [ ] `.gitignore` bekerja.
- [ ] Push ke GitHub berhasil.
- [ ] Pull/clone dipahami dan dicoba.
- [ ] README cukup untuk menjalankan project pada folder baru.
