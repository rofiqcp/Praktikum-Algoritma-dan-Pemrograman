# Jobsheet Pertemuan 11 — Deployment GitHub ke Aplikasi Publik

## Identitas
- Nama:
- NIM/Kelas:
- Tanggal:
- OS:
- Repository:
- Branch deploy:
- Platform yang dipakai di kelas:
- Public URL:

## Tujuan Praktikum
Mahasiswa menyiapkan aplikasi Flask agar dapat direproduksi dari environment baru, menghubungkannya ke GitHub, mendeploy ke platform yang tersedia, mengatur environment variable, memverifikasi public URL, dan mendiagnosis build/start/runtime error berdasarkan log.

> Nama menu pada dashboard cloud dapat berubah. Ikuti dokumentasi resmi platform yang dipilih pengajar. Fokus jobsheet ini adalah workflow dan bukti teknis yang harus dipahami.

---

# A. Audit Kondisi Lokal

Masuk ke folder:

```bash
cd Pertemuan-11-Deployment/praktikum/deploy-flask
```

Periksa:

```bash
python --version
python -m pip --version
git status
```

Jalankan test:

```bash
python -m unittest -v test_app.py
```

Catat:

| Pemeriksaan | Hasil |
|---|---|
| Python | |
| test pass | |
| git status bersih? | |
| branch | |

Deployment **tidak dimulai** sebelum program lokal dan test diketahui berjalan.

---

# B. Clean Environment Test

Buat environment baru agar dependency global tidak menutupi masalah.

```bash
python -m venv .venv-clean
```

Aktifkan sesuai OS, lalu:

```bash
python -m pip install -r requirements.txt
python -m unittest -v test_app.py
```

Isi:

```text
Apakah clean install berhasil?
Jika gagal, error:
Perbaikan:
Retest:
```

---

# C. Audit File Production

Periksa minimal:

```text
app.py
requirements.txt
.gitignore
.env.example
README.md
Procfile atau start-command documentation
DEPLOYMENT_CHECKLIST.md
```

Isi tabel:

| File | Ada? | Fungsi | Masalah ditemukan? |
|---|:---:|---|---|
| `app.py` | | | |
| `requirements.txt` | | | |
| `.gitignore` | | | |
| `.env.example` | | | |
| `README.md` | | | |
| `Procfile`/start command | | | |

---

# D. requirements.txt

Buka file dan identifikasi dependency.

Jawab:

1. Mengapa Flask harus tertulis?
2. Jika start command memakai Gunicorn tetapi `gunicorn` tidak ada di dependency, fase mana yang berpotensi gagal?
3. Mengapa `pip freeze` dari environment yang terlalu banyak package dapat menghasilkan dependency tidak perlu?

Uji:

```bash
python -m pip install -r requirements.txt
```

---

# E. Environment Variable

Gunakan `.env.example` sebagai daftar konfigurasi yang perlu diketahui tanpa secret nyata.

Periksa source dan identifikasi penggunaan:

```python
os.getenv("...")
```

Isi:

| Variable | Wajib/opsional | Default aman? | Sensitif? |
|---|---|---|:---:|
| | | | |

Aturan:

- `.env` lokal tidak boleh di-commit;
- credential nyata tidak ditulis pada README;
- screenshot/video tidak menampilkan nilai secret.

---

# F. GitHub Readiness

Jalankan:

```bash
git status
git log --oneline -5
```

Pastikan source terbaru sudah di-commit dan push.

Catat:

```text
Repository:
Branch:
Commit SHA yang akan dideploy:
```

Verifikasi bahwa branch pada platform nanti sama dengan branch yang dimaksud.

---

# G. Tentukan Build dan Start Mental Model

Isi sebelum membuka dashboard platform:

```text
Runtime              : Python
Dependency file      : requirements.txt
File utama           : app.py
Object Flask         : app
Local run            : python app.py
Production start     : ................................
Health path          : /health
```

Jika contoh memakai Gunicorn:

```text
gunicorn app:app
```

Jelaskan arti `app:app`.

---

# H. Hubungkan Repository ke Platform

Langkah generik:

1. pilih create/import service/project;
2. hubungkan GitHub bila diperlukan;
3. pilih repository;
4. pilih branch;
5. pilih runtime/framework yang sesuai;
6. atur build/install command bila platform meminta;
7. atur start command bila model platform membutuhkan;
8. tambahkan environment variable;
9. mulai deploy;
10. jangan tutup log sebelum hasil build/start diketahui.

Catat konfigurasi aktual:

| Item | Nilai |
|---|---|
| Platform | |
| Repo | |
| Branch | |
| Build command | |
| Start command | |
| Region bila ada | |
| Health path bila ada | |

---

# I. Membaca Build Log

Saat build berlangsung, cari bukti:

```text
source/repository ditemukan
runtime Python dipilih
install dependency dimulai
requirements diproses
build/install selesai atau error
```

Jika gagal, salin **hanya bagian log relevan** untuk laporan.

Format:

```text
Jenis masalah: BUILD
Baris error utama:
3–5 baris context:
Hipotesis:
Perubahan minimal:
Hasil redeploy:
```

---

# J. Membaca Start/Runtime Log

Setelah build sukses, pastikan process start.

Cari bukti:

```text
start command dijalankan
app/module dapat import
server bind/start
request masuk
status response
```

Jika build sukses tetapi public URL tidak bekerja, jangan kembali mengubah requirements tanpa bukti. Periksa start/runtime log.

---

# K. Public Verification

Setelah URL tersedia, uji:

| Test | Path | Expected | Actual | Pass? |
|---|---|---|---|:---:|
| Homepage | `/` | 200 | | |
| Health | `/health` | 200 + status | | |
| Route salah | `/tidak-ada` | 404 | | |
| Fitur utama | | sukses | | |
| Invalid input bila ada | | error ramah | | |

Catat public URL tanpa credential.

---

# L. Test dari Perangkat/Jaringan Lain

Bila memungkinkan:

- buka dari private/incognito;
- buka dari ponsel;
- gunakan jaringan berbeda;
- minta rekan menguji `/health`.

Catat:

```text
Perangkat/jaringan kedua:
URL yang diuji:
Hasil:
```

---

# M. Log Lab — Empat Kategori Error

Pengajar dapat menyediakan log contoh atau mahasiswa membuat simulasi aman pada branch latihan.

## M1. Build Error
Contoh: dependency salah.

## M2. Start Error
Contoh: start command menunjuk module yang tidak ada.

## M3. Runtime 500
Contoh: route tertentu melempar exception setelah service hidup.

## M4. Environment Missing
Contoh: konfigurasi wajib tidak tersedia.

Untuk setiap kasus isi:

| Aspek | Catatan |
|---|---|
| Kategori | |
| Gejala publik | |
| Log utama | |
| Layer | |
| Root cause | |
| Fix minimal | |
| Retest | |
| Regression test | |

---

# N. Security Audit

Periksa repository sebelum demo.

```bash
git status
```

Cari secara manual file/config yang tidak seharusnya dipublikasi.

Checklist:

- [ ] `.env` tidak tracked.
- [ ] `.venv` tidak tracked.
- [ ] Tidak ada credential pada source.
- [ ] Tidak ada credential pada README.
- [ ] Tidak ada credential pada screenshot/video.
- [ ] Debug mode production tidak digunakan.

Pertanyaan: jika credential pernah terlanjur masuk repository publik, apa tindakan yang diperlukan selain menghapus barisnya?

---

# O. README Deployment Section

Tambahkan:

```text
## Local Setup
## Run Local
## Test
## Environment Variables
## Deployment
## Public Verification
## Troubleshooting
## Known Limitations
```

Pada `Environment Variables`, tulis **nama variable dan tujuan**, bukan nilai secret.

---

# P. Challenge Mandiri

Pilih minimal dua:

1. Tambah metadata aman pada `/health`.
2. Tambah `APP_NAME` melalui environment variable.
3. Buat smoke-test script manual untuk public URL.
4. Dokumentasikan satu build failure dan satu runtime failure.
5. Uji deployment commit/branch berbeda secara terkontrol.
6. Tambah known limitations pada README.
7. Tambah tabel verifikasi desktop/mobile.
8. Buat diagram deployment flow project sendiri.

---

# Q. Deployment Report

Isi:

```text
Repository:
Branch:
Commit:
Platform:
Public URL:
Build result:
Start result:
Health result:
Feature result:
Second-device result:
Environment variables configured:
Known limitations:
```

## Troubleshooting Record

```text
Gejala:
Timestamp:
Build/start/runtime?
Log relevan:
Hipotesis:
Perubahan:
Commit perbaikan:
Redeploy result:
Retest:
```

---

# Pertanyaan Analisis
1. Mengapa aplikasi yang berjalan lokal belum tentu bisa dideploy?
2. Apa beda build dan start?
3. Apa beda start error dan runtime 500?
4. Mengapa health endpoint membantu diagnosis?
5. Mengapa clean environment test penting?
6. Apa akibat branch deploy salah?
7. Mengapa `.env.example` berguna?
8. Mengapa credential bocor harus dirotasi?
9. Mengapa platform free-tier tidak boleh dianggap permanen?
10. Bagaimana Git history membantu rollback/debugging?

# Deliverable
- GitHub repository;
- public URL;
- screenshot/status bukti deployment;
- hasil `/health`;
- deployment checklist;
- satu log troubleshooting lengkap;
- README deployment section;
- hasil test lokal;
- bukti test perangkat/jaringan lain bila memungkinkan;
- video sesuai `TugasVideo.md`.
