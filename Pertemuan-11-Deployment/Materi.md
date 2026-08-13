# Materi Pertemuan 11 — Deployment: Dari GitHub ke Aplikasi Publik

> Sumber utama: *Buku Panduan Praktik: Scratch → Python → Web → API → Node.js → Full Stack*, Edisi Agustus 2026. Buku menekankan **konsep dan workflow deployment**, karena tampilan dashboard, paket gratis, batas resource, dan detail konfigurasi platform cloud dapat berubah. Sebelum kelas, verifikasi dokumentasi resmi platform yang dipilih.

Tujuan sesi adalah memahami bagaimana source code lokal berubah menjadi service yang dapat diakses melalui internet, serta bagaimana membaca **build log** dan **runtime log** ketika deployment gagal.

## Target Kompetensi
Setelah praktikum, mahasiswa mampu:

1. Membedakan local development, build, deploy, runtime, domain/public URL, dan environment variable.
2. Menjelaskan alur `VS Code → Git commit → GitHub push → cloud build → runtime → public URL`.
3. Menyiapkan `requirements.txt`, `.gitignore`, entrypoint, dan start command yang benar.
4. Menjalankan aplikasi lokal dari environment baru sebelum deploy.
5. Mendeploy aplikasi Python dari GitHub ke minimal satu platform yang tersedia di kelas.
6. Mengenal variasi model Vercel, Render, Railway, PythonAnywhere, dan static hosting.
7. Memindahkan konfigurasi sensitif ke environment variable.
8. Menjelaskan mengapa `.env`, token, password, dan credential tidak boleh masuk repository publik.
9. Membedakan build error, start error, runtime error, public 404, dan missing environment variable.
10. Membaca log berdasarkan bukti dan melakukan perubahan minimal.
11. Menambahkan health endpoint untuk verifikasi service.
12. Menguji aplikasi dari public URL dan perangkat/jaringan lain bila memungkinkan.
13. Mendokumentasikan deployment dan troubleshooting pada README.

## Output Pertemuan
- aplikasi Python mempunyai public URL;
- source berada di GitHub;
- secret/config sensitif dipindahkan ke environment variable;
- health endpoint dapat diuji;
- README mempunyai setup, deployment, verification, dan troubleshooting;
- deployment checklist terisi;
- satu log lab build/start/runtime;
- automated test lokal lulus sebelum deploy;
- video sesuai `TugasVideo.md`.

## Alur Pengajaran 180 Menit
| Tahap | Durasi | Aktivitas |
|---|---:|---|
| Konsep cloud | 25 | local vs public, build vs runtime |
| Production prep | 30 | requirements, env, debug off, port |
| GitHub deploy flow | 25 | repo → platform → build → start |
| Platform variations | 25 | Vercel/Render/Railway/PythonAnywhere/static |
| Hands-on deploy | 50 | deploy satu web/API |
| Log lab | 15 | build failure vs runtime failure |
| Security & recap | 10 | secrets dan caveat platform |

---

# 11.1 Deployment Mental Model

```text
CODE DI VS CODE
      ↓
GIT COMMIT
      ↓
GITHUB PUSH
      ↓
CLOUD MENARIK SOURCE
      ↓
BUILD / INSTALL DEPENDENCY
      ↓
START APPLICATION
      ↓
RUNTIME
      ↓
PUBLIC URL
      ↓
REQUEST PENGGUNA
      ↓
LOG / RESPONSE
```

Setiap tahap dapat gagal dengan bukti berbeda. Karena itu debugging deployment harus mencari **layer yang gagal**, bukan langsung mengganti framework atau menghapus project.

---

# 11.2 Local Development vs Production

## Local development
Biasanya:

```bash
python app.py
```

atau:

```bash
flask --app app run --debug
```

Tujuannya cepat mengembangkan dan membaca traceback.

## Production runtime
Platform cloud membutuhkan process yang dapat dijalankan secara konsisten. Untuk Flask, contoh umum menggunakan WSGI server seperti Gunicorn:

```text
gunicorn app:app
```

Arti `app:app`:

```text
file/module : object Flask
app.py      : app
```

Development server Flask bukan target production deployment.

---

# 11.3 File yang Umumnya Dibutuhkan

```text
project/
├── app.py
├── requirements.txt
├── .gitignore
├── .env.example
├── README.md
├── Procfile              # bila platform/konfigurasi memakainya
├── templates/
└── static/
```

## requirements.txt
Contoh:

```text
Flask
gunicorn
requests
```

Prinsipnya: dependency yang diperlukan aplikasi harus dapat di-install ulang dari file dependency.

---

# 11.4 Reproducible Environment

Sebelum deploy, uji project dari environment baru:

```bash
python -m venv .venv-test
```

Aktifkan, lalu:

```bash
python -m pip install -r requirements.txt
python -m unittest -v test_app.py
```

Jika environment bersih gagal, cloud sangat mungkin juga gagal. Jangan mengandalkan package yang kebetulan terpasang global pada laptop.

---

# 11.5 Environment Variable

Konfigurasi runtime sebaiknya dibaca dari environment.

```python
import os

APP_NAME = os.getenv("APP_NAME", "Praktikum Deployment")
```

Untuk konfigurasi wajib:

```python
import os

SERVICE_URL = os.getenv("SERVICE_URL")
if not SERVICE_URL:
    raise RuntimeError("SERVICE_URL belum dikonfigurasi")
```

`.env.example` berisi **nama variable dan nilai contoh yang aman**, bukan secret nyata.

Contoh:

```text
APP_NAME=Praktikum Deployment
SERVICE_URL=https://example.invalid
```

---

# 11.6 Jangan Commit Secret

Yang tidak boleh dimasukkan ke repository publik:

- `.env` berisi credential;
- API key nyata;
- password database;
- token akses;
- private key;
- file credential private;
- screenshot dashboard yang menampilkan secret.

Jika credential pernah terlanjur dipublikasikan, menghapus baris pada commit terbaru **tidak cukup**. Credential tersebut harus dianggap bocor dan dirotasi sesuai layanan terkait.

`.gitignore` minimal:

```text
.venv/
__pycache__/
*.pyc
.env
```

---

# 11.7 Entrypoint dan Start Command

Pertanyaan yang harus bisa dijawab sebelum deploy:

1. File aplikasi utama apa?
2. Object Flask bernama apa?
3. Command lokal yang berhasil apa?
4. Command production yang akan dijalankan apa?
5. Dependency untuk command itu ada di `requirements.txt`?

Contoh:

```text
Module  : app.py
Object  : app
Start   : gunicorn app:app
```

Kesalahan umum:

```text
gunicorn main:app
```

padahal file sebenarnya `app.py`.

Hasilnya adalah start error, bukan bug route.

---

# 11.8 Port

Pada cloud, port sering diberikan oleh environment/platform. Aplikasi sebaiknya tidak menganggap hanya satu port tetap untuk semua environment.

Untuk kode yang memang menjalankan server langsung:

```python
import os

port = int(os.getenv("PORT", "5000"))
app.run(host="0.0.0.0", port=port)
```

Namun pada setup Gunicorn, process manager/server production biasanya menangani binding sesuai start command platform.

---

# 11.9 Health Endpoint

Tambahkan endpoint sederhana:

```python
@app.get("/health")
def health():
    return {"status": "ok"}
```

Health endpoint berguna untuk membedakan:

```text
service hidup tetapi route fitur bermasalah
```

dengan:

```text
service tidak start sama sekali
```

Health endpoint bukan pengganti monitoring production yang lengkap; pada praktikum ini digunakan sebagai verifikasi dasar.

---

# 11.10 Alur GitHub ke Cloud

```text
1. Pastikan local test PASS
2. git status
3. git add
4. git commit
5. git push
6. Hubungkan repository pada platform
7. Pilih branch deploy
8. Tentukan build/install command bila diminta
9. Tentukan start command bila diminta
10. Set environment variable
11. Deploy
12. Baca build log
13. Baca start/runtime log
14. Buka public URL
15. Test /health dan fitur utama
16. Test dari perangkat/jaringan lain bila memungkinkan
17. Catat hasil di README
```

---

# 11.11 Variasi Platform yang Dikenalkan dalam Buku

| Platform/model | Model belajar | Cocok untuk menjelaskan | Catatan |
|---|---|---|---|
| Vercel | function/serverless-style deployment dengan dukungan Python framework tertentu | deploy framework dari GitHub | perhatikan runtime/function dan entrypoint |
| Render | web service dengan build/start command | server process dan logs | free resource/batas dapat berubah |
| Railway | project/service runtime dan networking | backend + database tahap lanjut | plan/kredit dapat berubah |
| PythonAnywhere | hosting berfokus Python | alternatif pemula untuk Flask | batas akun perlu dicek |
| Static hosting | HTML/CSS/JS tanpa Python server | beda frontend static dan backend | tidak menjalankan Flask server |

## Prinsip penting
Repository praktikum **tidak mengunci satu platform**. Pengajar memilih platform yang tersedia dan sesuai kebijakan saat kelas berlangsung.

---

# 11.12 Build vs Start vs Runtime

## Build/install phase
Contoh kegiatan:

```text
clone source
→ pilih runtime Python
→ install requirements
→ siapkan artifact/environment
```

Contoh kegagalan:

- dependency tidak ditemukan;
- syntax requirement salah;
- versi runtime tidak kompatibel;
- file dependency tidak berada di lokasi yang diharapkan.

## Start phase
Platform mencoba menjalankan process.

Contoh kegagalan:

- command salah;
- module/object salah;
- Gunicorn tidak ter-install;
- application crash saat import karena env wajib tidak ada.

## Runtime
Service sudah start, tetapi request tertentu gagal.

Contoh:

- route melempar exception;
- API eksternal timeout;
- konfigurasi salah;
- path tertentu 404.

---

# 11.13 Matriks Diagnosis Error

| Jenis | Contoh | Tempat mencari bukti |
|---|---|---|
| Build error | package gagal install | build logs |
| Start error | command/entrypoint salah | deploy/start logs |
| Runtime 500 | exception saat request | application/runtime logs |
| Public 404 | route/path/domain salah | routing/request logs |
| Env missing | variable config tidak ada | environment settings + logs |
| Timeout dependency | service eksternal lambat | runtime log + timing request |

---

# 11.14 Contoh Analisis Build Error

Log hipotetis:

```text
ERROR: Could not find a version that satisfies the requirement SomePackageXYZ
```

Jangan langsung mengubah seluruh project. Periksa:

1. apakah nama dependency benar;
2. apakah dependency memang diperlukan;
3. apakah versi yang dipin kompatibel;
4. apakah Python version sesuai;
5. apakah local clean install menghasilkan error yang sama.

---

# 11.15 Contoh Analisis Start Error

Gejala:

```text
ModuleNotFoundError: No module named 'main'
```

Start command:

```text
gunicorn main:app
```

Struktur:

```text
app.py
```

Hipotesis yang didukung bukti: module pada start command salah. Perubahan minimal:

```text
gunicorn app:app
```

Lalu redeploy dan verifikasi log start.

---

# 11.16 Contoh Runtime 500

Jika homepage sukses tetapi `/data` 500:

```text
SERVICE STARTED
/health → 200
/ → 200
/data → 500
```

Ini menunjukkan deployment dasar sudah hidup. Fokus diagnosis pindah ke handler `/data` atau dependency yang dipanggil route itu, bukan kembali mengganti build command.

---

# 11.17 Verifikasi Deployment

Setelah platform menampilkan “deployed”, pekerjaan belum selesai.

Uji minimal:

```text
GET /
GET /health
GET satu halaman/API utama
POST/form bila ada
invalid input
404
```

Catat:

| Test | URL/path | Expected | Actual | Pass? |
|---|---|---|---|:---:|
| Homepage | `/` | 200 | | |
| Health | `/health` | 200 | | |
| Feature | | | | |
| Invalid | | error ramah | | |
| 404 | `/route-tidak-ada` | 404 | | |

---

# 11.18 Test dari Perangkat/Jaringan Lain

Jika hanya diuji dari browser yang sama, masih ada kemungkinan cache/session/local assumption menutupi masalah. Bila memungkinkan:

- buka public URL dari mode private;
- buka dari perangkat lain;
- gunakan mobile data/jaringan lain;
- minta teman mengakses `/health`.

Jangan membagikan URL yang berisi credential pada query string.

---

# 11.19 Deployment Documentation di README

README minimal mempunyai:

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

Hindari menulis secret pada README.

---

# 11.20 Rollback Mental Model

Jika deployment terbaru rusak tetapi commit sebelumnya diketahui baik:

```text
GOOD COMMIT → deploy berhasil
BAD COMMIT  → deploy gagal
```

Git history membantu membandingkan perubahan. Di kelas, jangan langsung menghapus repository. Identifikasi commit/perubahan penyebab lalu perbaiki atau redeploy versi yang diketahui stabil sesuai workflow platform.

---

# 11.21 Troubleshooting Workflow

```text
1. Reproduce dari public URL
2. Catat status/gejala
3. Tentukan: build, start, runtime, routing, env, dependency
4. Baca log yang tepat
5. Ambil bagian error paling relevan
6. Bandingkan dengan local clean run
7. Buat satu hipotesis
8. Lakukan perubahan minimal
9. Commit dan push
10. Redeploy
11. Retest kasus gagal
12. Regression test
13. Dokumentasikan root cause
```

---

# 11.22 Security Minimum

- jangan deploy dengan debug mode production;
- jangan commit `.env`;
- jangan menampilkan credential di log;
- gunakan environment variable untuk konfigurasi sensitif;
- cek kembali public repository sebelum demo;
- jika credential bocor, lakukan rotasi;
- gunakan data praktikum/non-sensitif.

---

# 11.23 Challenge Mandiri

Pilih minimal dua:

1. Tambah `/health` dengan metadata aman seperti nama aplikasi dan status.
2. Tambah config `APP_NAME` melalui environment variable.
3. Buat halaman `/config-demo` yang hanya menampilkan apakah config tersedia, bukan nilainya bila sensitif.
4. Buat simulasi build/start/runtime error dan tulis laporan diagnosis.
5. Deploy branch tertentu dan buktikan branch yang dipakai.
6. Tambah smoke-test script untuk public URL.
7. Tambah deployment section pada README.
8. Tambah tabel known limitations.

---

# 11.24 Checklist Deploy

- [ ] Program berjalan lokal dari environment baru.
- [ ] Automated test lulus.
- [ ] `requirements.txt` benar.
- [ ] `.env` ada di `.gitignore`.
- [ ] `.env.example` tidak mengandung secret.
- [ ] Debug mode tidak digunakan untuk production.
- [ ] Repository/branch deploy sudah benar.
- [ ] Build berhasil.
- [ ] Service start berhasil.
- [ ] `/health` mengembalikan response.
- [ ] Homepage/fitur utama diuji.
- [ ] Environment variable tersedia.
- [ ] Runtime log diperiksa setelah request gagal.
- [ ] Public URL diuji dari perangkat/jaringan lain bila memungkinkan.
- [ ] README diperbarui.

## Exit Ticket
1. Apa beda build error dan runtime error?
2. Mengapa `requirements.txt` penting walaupun aplikasi berjalan di laptop?
3. Apa fungsi start command?
4. Mengapa `.env.example` boleh di-commit tetapi `.env` tidak?
5. Apa fungsi health endpoint?
6. Jika `/health` 200 tetapi `/products` 500, layer mana yang harus diperiksa lebih dulu?
7. Mengapa detail paket cloud harus diverifikasi kembali sebelum kelas?
8. Apa tindakan yang benar jika credential pernah masuk repository publik?

## Referensi Internal
- `Jobsheet.md`
- `TugasVideo.md`
- `praktikum/deploy-flask/`
- `praktikum/deploy-flask/DEPLOYMENT_CHECKLIST.md`
- `Referensi/N-Referensi-Resmi.md`
