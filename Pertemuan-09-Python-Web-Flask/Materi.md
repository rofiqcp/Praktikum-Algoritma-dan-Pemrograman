# Materi Pertemuan 09 — Python Web Programming: Dari Program Terminal menjadi Website

> Sumber utama: *Buku Panduan Praktik: Pemrograman Dasar hingga Full Stack — 16 Pertemuan Terstruktur, Edisi Agustus 2026*. Mulai sesi ini biasakan AI-assisted coding berbasis context, evidence, constraint, dan verification; jangan menempel secret ke prompt/repository.

Fokus sesi adalah pemrograman web berbasis Python. HTML/CSS/JavaScript dikenalkan secukupnya untuk membangun antarmuka; backend utama tetap Python Flask.

## Target Kompetensi
- Menjelaskan client, server, request, response, route, template, dan static asset.
- Membuat web lokal dengan Flask.
- Mengenal komponen UI/UX umum dan state komponen.
- Membuat form GET/POST dan validasi server-side sederhana.
- Menyusun struktur project web yang rapi.

## Output
- Website Python lokal minimal tiga halaman.
- Form yang memproses input menggunakan Python.
- Halaman daftar data sederhana dari list/dictionary.

## Alur 180 Menit
| Tahap | Durasi | Aktivitas |
|---|---:|---|
| Mental model web | 25 | Browser, HTTP, server Python |
| UI/UX vocabulary | 30 | Komponen halaman dan state |
| Flask first app | 30 | route dan local server |
| Template/static | 30 | HTML, CSS, Jinja |
| Form | 35 | GET/POST, `request.form`, validation |
| Challenge | 20 | Tambah halaman/komponen |
| Troubleshoot + prompt | 10 | 404, 500, template not found |

## 9.1 Arsitektur Web Sederhana
```text
BROWSER → HTTP REQUEST → FLASK ROUTE → PYTHON LOGIC
       ← TEMPLATE/RESPONSE ←
```
Frontend berinteraksi dengan user di browser; backend menjalankan logic, validasi, dan akses data.

## 9.2 Kamus Komponen UI
| Kelompok | Contoh | Tujuan |
|---|---|---|
| Layout | header, navbar, main, section, footer, grid | Struktur halaman |
| Text | heading, paragraph, label, caption, link | Informasi/hierarki |
| Input | text, number, email, date, textarea | Menerima data |
| Selection | checkbox, radio, select, toggle | Memilih nilai |
| Action | button, submit, cancel | Memicu aksi |
| Data display | card, table, list, badge | Menampilkan data |
| Navigation | navbar, tabs, breadcrumb | Berpindah konteks |
| Feedback | alert, toast, modal, spinner, validation | Status aksi |

## 9.3 State UI/UX
Normal, hover, focus, disabled, loading, error, success. State harus terlihat dan tidak hanya mengandalkan warna bila bisa dihindari.

## 9.4 UX Dasar
- Hierarchy: judul/aksi utama mudah ditemukan.
- Consistency: pola tombol/form konsisten.
- Feedback: setiap submit memberi hasil/error.
- Error prevention: constraint dan validasi jelas.
- Empty state: halaman data kosong tetap informatif.

## 9.5 Flask Pertama
```python
from flask import Flask
app = Flask(__name__)

@app.get("/")
def home():
    return "Hello Flask"
```
Jalankan dengan `flask --app app run --debug` atau `python app.py` sesuai entrypoint project.

## 9.6 Struktur Project
```text
flask-web/
├── app.py
├── requirements.txt
├── templates/
│   ├── base.html
│   ├── home.html
│   └── products.html
└── static/
    ├── css/style.css
    └── js/app.js
```

## 9.7 Form GET/POST dan Validasi
Browser-side validation membantu UX tetapi backend tetap harus memvalidasi data. Cocokkan atribut `name` di HTML dengan key `request.form`.

## 9.8 Troubleshooting Web
| Gejala | Penyebab | Perbaikan |
|---|---|---|
| 404 | route/URL tidak cocok | cek decorator dan URL |
| 500 | exception backend | baca traceback terminal |
| `TemplateNotFound` | folder/nama salah | pastikan `templates/` dan case |
| CSS tidak masuk | static path/cache | `url_for('static',...)`, hard refresh |
| Form kosong | `name` tidak cocok | cocokkan HTML dengan `request.form` |
| Port dipakai | server lama hidup | stop proses atau pilih port lain |

## Prompt Teknis yang Baik
Sebutkan environment, struktur file, state yang sudah bekerja, gejala, expected, traceback/evidence, constraint perubahan, dan test verifikasi. Hindari prompt “error, fix” tanpa bukti.
