# Jobsheet Pertemuan 09 — Python Web Flask, UI/UX, Template, dan Form

## Identitas
- Nama:
- NIM/Kelas:
- Tanggal:
- Sistem operasi:
- Versi Python:
- Versi Flask:
- Link repository GitHub:

## Tujuan Praktikum
Mahasiswa membangun aplikasi web lokal berbasis Flask dengan minimal tiga halaman, template inheritance, static asset, halaman daftar data, form GET/POST, validasi server-side, feedback UI, responsive layout, dan automated test sederhana.

## Hasil Akhir yang Harus Terlihat
Aplikasi contoh minimal mempunyai route:

```text
GET  /
GET  /about
GET  /products
GET  /products/new
POST /products/new
GET  /products?q=<kata>
404  route tidak dikenal
```

Data pada pertemuan ini masih boleh disimpan di memory menggunakan list/dictionary.

---

# Bagian A — Persiapan Environment

## A1. Buka folder praktikum

```bash
cd Pertemuan-09-Python-Web-Flask/praktikum/flask-web
```

## A2. Buat virtual environment

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
source .venv/bin/activate
```

## A3. Install dependency

```bash
python -m pip install -r requirements.txt
```

## A4. Verifikasi

```bash
python --version
python -m pip --version
python -c "import flask; print(flask.__version__)"
```

Catat hasil:

| Pemeriksaan | Hasil |
|---|---|
| Python | |
| pip | |
| Flask dapat import | |
| `.venv` aktif | |

---

# Bagian B — Mental Model Request/Response

Sebelum menjalankan program, isi tabel prediksi berikut.

| Aksi browser | Method | URL | Route Python | Response yang diharapkan |
|---|---|---|---|---|
| Buka Home | GET | `/` | `home()` | HTML Home |
| Buka Produk | GET | `/products` | `product_list()` | HTML list |
| Buka form | GET | `/products/new` | `product_new()` | HTML form |
| Submit form | POST | `/products/new` | `product_new()` | validasi lalu redirect/form |
| URL salah | GET | `/abc` | tidak ada | 404 |

Tuliskan dengan kata-kata sendiri alur:

```text
Browser → ...................................................... → Browser
```

---

# Bagian C — Menjalankan Flask

Jalankan:

```bash
python app.py
```

Buka URL lokal yang ditampilkan terminal, biasanya:

```text
http://127.0.0.1:5000
```

Uji:

```text
/
/about
/products
/products/new
```

Catat status:

| Route | Bisa dibuka? | Komponen utama yang terlihat |
|---|:---:|---|
| `/` | | |
| `/about` | | |
| `/products` | | |
| `/products/new` | | |

---

# Bagian D — Audit Struktur Project

Periksa struktur berikut:

```text
flask-web/
├── app.py
├── requirements.txt
├── README.md
├── test_app.py
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── products.html
│   ├── product_form.html
│   ├── about.html
│   └── 404.html
└── static/
    ├── css/style.css
    └── js/app.js
```

Jawab:

1. Mengapa HTML berada di `templates/`?
2. Mengapa CSS/JS berada di `static/`?
3. Apa fungsi `base.html`?
4. Mengapa test tidak diletakkan di dalam route?

---

# Bagian E — Template Inheritance

Buka `templates/base.html`, lalu identifikasi:

- `<meta name="viewport">`;
- navigation;
- `url_for('static', ...)`;
- block title;
- block content;
- flash message.

Isi tabel:

| Bagian | Ada? | Fungsinya |
|---|:---:|---|
| `block title` | | |
| `block content` | | |
| Navbar | | |
| CSS `url_for` | | |
| Flash | | |

Modifikasi kecil wajib: tambahkan nama/kelas pada footer atau bagian About.

---

# Bagian F — Data List/Dictionary ke Template

Buka data `products` di `app.py`.

Amati bentuk satu data:

```python
{"id": 1, "name": "Keyboard", "price": 250000, "stock": 10}
```

Jawab:

1. Apa tipe `products`?
2. Apa tipe setiap elemen di dalamnya?
3. Key apa yang tersedia?
4. Di file template mana data tersebut di-loop?

Tambahkan satu produk awal secara manual, restart server bila diperlukan, lalu pastikan produk terlihat.

---

# Bagian G — Form dan Server-side Validation

Uji form `/products/new` dengan kasus berikut.

| TC | Nama | Harga | Stok | Expected | Actual | Pass? |
|---|---|---:|---:|---|---|:---:|
| G01 | Monitor | 1500000 | 4 | berhasil | | |
| G02 | kosong | 10000 | 1 | nama ditolak | | |
| G03 | Kabel | -1 | 2 | harga ditolak | | |
| G04 | Kabel | abc | 2 | harga ditolak | | |
| G05 | Kabel | 10000 | -1 | stok ditolak | | |
| G06 | Kabel | 10000 | 1.5 | stok ditolak | | |
| G07 | Keyboard | 10000 | 1 | duplikat ditolak bila fitur aktif | | |
| G08 | NolStok | 1000 | 0 | boundary stok 0 diterima | | |

Pertanyaan analisis:

1. Mengapa `required` di HTML belum cukup sebagai validasi keamanan/keandalan?
2. Apa perbedaan `float()` dan `int()` pada form?
3. Mengapa `stock=0` seharusnya valid tetapi `stock=-1` tidak?

---

# Bagian H — Search dengan Query Parameter

Jika project contoh mempunyai search, buka:

```text
/products?q=key
```

Lalu coba:

```text
/products?q=keyboard
/products?q=KEY
/products?q=tidakada
/products?q=
```

Catat:

| Query | Expected | Actual | Pass? |
|---|---|---|:---:|
| `keyboard` | Keyboard muncul | | |
| `KEY` | pencarian tidak sensitif case | | |
| `tidakada` | empty/no-result state | | |
| kosong | semua data | | |

---

# Bagian I — UI/UX Audit

Gunakan `praktikum/UI_UX_CHECKLIST.md`.

Minimal periksa:

- heading utama jelas;
- navigation konsisten;
- label terhubung dengan input;
- focus keyboard terlihat;
- error message dekat field;
- success feedback terlihat;
- empty state ada;
- table/card dapat digunakan pada layar sempit;
- warna bukan satu-satunya pembeda status.

Lakukan satu perbaikan UI sendiri dan tulis:

```text
Masalah awal:
Perubahan:
Alasan UX:
Cara verifikasi:
```

---

# Bagian J — Debugging Lab

Lakukan pada salinan kerja, lalu kembalikan ke kondisi benar.

## J1. 404 disengaja
Ubah link ke URL yang tidak memiliki route.

Catat:

```text
Gejala:
Status code:
Root cause:
Perbaikan:
```

## J2. TemplateNotFound
Ubah sementara nama template yang dipanggil route.

Cari bukti dari traceback terminal. Jangan menebak hanya dari halaman browser.

## J3. Form key salah
Ubah sementara salah satu `name` input sehingga tidak sama dengan key pada `request.form`.

Jelaskan mengapa field menjadi kosong/tidak terbaca.

## J4. Static path salah
Ubah sementara path CSS dan amati network/visual result.

---

# Bagian K — Automated Test

Jalankan:

```bash
python -m unittest -v test_app.py
```

Catat jumlah test:

```text
Jumlah test dijalankan :
Jumlah pass            :
Jumlah fail/error      :
```

Buka `test_app.py` dan identifikasi pola:

```text
SETUP → REQUEST → ASSERT STATUS → ASSERT BODY/STATE
```

Tambahkan minimal **dua test mandiri**, misalnya:

- query search case-insensitive;
- stok 0 diterima;
- produk duplikat ditolak;
- halaman form dapat dibuka;
- response 404 mempunyai pesan yang benar.

Setelah modifikasi:

```bash
python -m unittest -v test_app.py
```

Semua test lama harus tetap lulus.

---

# Bagian L — Challenge Mandiri

Pilih minimal dua:

1. Tambah route detail `/products/<id>`.
2. Tambah filter stok tersedia/habis.
3. Tambah badge stok habis.
4. Tambah tombol reset search.
5. Tambah halaman bantuan penggunaan.
6. Tambah validasi duplikat nama.
7. Tambah field kategori dengan `select`.
8. Tambah sort nama/harga sederhana.

Aturan:

- tidak menambah framework frontend;
- server-side validation tetap ada;
- minimal satu test baru per fitur;
- tulis expected sebelum coding.

---

# Bagian M — Test Report

Isi minimal 10 kasus.

| ID | Layer | Skenario | Expected | Actual | Status |
|---|---|---|---|---|---|
| TC01 | route | Home | 200 | | |
| TC02 | route | About | 200 | | |
| TC03 | route | Products | 200 | | |
| TC04 | form | POST valid | tersimpan | | |
| TC05 | form | nama kosong | ditolak | | |
| TC06 | form | harga negatif | ditolak | | |
| TC07 | form | stok non-integer | ditolak | | |
| TC08 | search | tidak ditemukan | empty state | | |
| TC09 | error | route salah | 404 | | |
| TC10 | regression | fitur lama setelah challenge | tetap benar | | |

---

# Bagian N — Pertanyaan Analisis

Jawab dengan kalimat sendiri.

1. Apa beda frontend dan backend pada project ini?
2. Apa yang terjadi dari saat button submit ditekan sampai browser menerima halaman berikutnya?
3. Apa beda route, view function, dan template?
4. Mengapa data list/dictionary hilang ketika process server restart?
5. Apa fungsi redirect setelah POST?
6. Mengapa status code 404 harus tetap 404 walaupun memakai template HTML yang bagus?
7. Apa beda client-side dan server-side validation?
8. Mengapa responsive layout termasuk kualitas fungsional, bukan hanya dekorasi?
9. Bagaimana cara membuktikan sebuah bug sudah benar-benar diperbaiki?
10. Apa materi Pertemuan 09 yang menjadi dasar untuk REST API pada Pertemuan 10?

---

# Deliverable
Kumpulkan:

- source code project;
- screenshot halaman Home, Products, Form, dan satu error/success state;
- hasil automated test;
- tabel test report minimal 10 kasus;
- satu catatan debugging lengkap: gejala → bukti → root cause → fix → retest;
- satu challenge mandiri;
- link GitHub branch/repository;
- video sesuai `TugasVideo.md`.

## Checklist Selesai
- [ ] Environment dapat dibuat ulang.
- [ ] Aplikasi berjalan lokal.
- [ ] Minimal tiga halaman.
- [ ] Form GET/POST berjalan.
- [ ] Validasi server-side berjalan.
- [ ] Template inheritance digunakan.
- [ ] Static CSS/JS termuat.
- [ ] Search/empty state diuji.
- [ ] 404 diuji.
- [ ] Automated test lulus.
- [ ] README menjelaskan setup/run/test.
