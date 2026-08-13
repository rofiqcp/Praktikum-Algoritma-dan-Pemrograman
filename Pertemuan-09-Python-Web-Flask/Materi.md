# Materi Pertemuan 09 — Python Web Programming: Dari Program Terminal menjadi Website

> Sumber utama: *Buku Panduan Praktik: Scratch → Python → Web → API → Node.js → Full Stack*, Edisi Agustus 2026. Fokus sesi ini tetap **Python sebagai backend utama**. HTML, CSS, dan JavaScript dikenalkan secukupnya untuk membangun antarmuka web yang dapat digunakan dan diuji.

Pertemuan 09 adalah transisi dari program terminal menuju aplikasi web. Mahasiswa tidak hanya belajar syntax Flask, tetapi juga memahami aliran **browser → HTTP request → route Flask → Python logic → template/response → browser**. Tujuan utamanya adalah membangun mental model web yang benar sebelum masuk ke REST API pada pertemuan berikutnya.

## Target Kompetensi
Setelah praktikum, mahasiswa mampu:

1. Menjelaskan istilah **client, browser, server, request, response, route, template, dan static asset**.
2. Menjalankan aplikasi Flask secara lokal dari virtual environment.
3. Membuat minimal tiga route halaman.
4. Menggunakan template Jinja dan template inheritance.
5. Menghubungkan stylesheet dan JavaScript melalui folder `static/`.
6. Mengenali komponen UI/UX umum dan state komponennya.
7. Membuat form `GET/POST` dan membaca `request.form`.
8. Melakukan validasi server-side untuk data wajib, angka, dan boundary sederhana.
9. Menampilkan feedback error/success kepada pengguna.
10. Membaca traceback Flask untuk mendiagnosis `404`, `500`, `TemplateNotFound`, static path, dan masalah form.
11. Menuliskan test case normal, boundary, invalid, empty-state, dan route-not-found.
12. Menjelaskan struktur project web yang rapi dan alasan setiap folder digunakan.

## Output Pertemuan
Mahasiswa menghasilkan:

- website Flask lokal dengan minimal tiga halaman;
- halaman daftar data sederhana dari `list`/`dictionary`;
- form yang memproses input dengan Python;
- UI yang mempunyai normal, focus, error, success, dan empty state;
- CSS responsive sederhana;
- unit/integration test menggunakan Flask test client;
- catatan troubleshooting berdasarkan bukti;
- video demo sesuai `TugasVideo.md`.

## Prasyarat
Mahasiswa sudah memahami Python dasar, function, list/dictionary, validasi, VS Code, virtual environment, terminal, Git, dan GitHub dari Pertemuan 01–08.

## Alur Pengajaran 180 Menit
| Tahap | Durasi | Aktivitas |
|---|---:|---|
| Mental model web | 25 menit | Browser, HTTP, client-server, request-response |
| UI/UX vocabulary | 30 menit | Komponen halaman, state, hierarchy, feedback |
| Flask first app | 30 menit | `Flask`, route, development server |
| Template & static | 30 menit | HTML, CSS, Jinja, `url_for()` |
| Form | 35 menit | GET/POST, `request.form`, server-side validation |
| Challenge | 20 menit | Tambah halaman/komponen/empty state |
| Troubleshooting & refleksi | 10 menit | 404, 500, template, static, form |

---

# 9.1 Dari CLI ke Web

Pada program terminal, interaksi biasanya langsung:

```text
USER → input() → PYTHON LOGIC → print() → USER
```

Pada web, browser menjadi perantara:

```text
BROWSER
   │
   │ HTTP Request
   ▼
FLASK ROUTE
   │
   ▼
PYTHON LOGIC
   │
   ├── validasi
   ├── baca/ubah data
   └── pilih template
   │
   ▼
HTML / HTTP Response
   │
   ▼
BROWSER
```

Perbedaan ini penting. Tombol pada halaman **tidak otomatis memanggil function Python**. Browser mengirim request ke URL tertentu. Flask menerima request itu melalui route, menjalankan logic, lalu mengirim response.

## Istilah inti
| Istilah | Makna praktis |
|---|---|
| Client | Pihak yang mengirim request; pada sesi ini biasanya browser |
| Server | Program yang menerima request dan memberikan response |
| Request | Pesan dari client: method, URL, header, dan kadang body |
| Response | Balasan server: status code, header, dan body |
| Route | Aturan yang memetakan URL/method ke handler Python |
| Handler/View function | Function Python yang dijalankan ketika route cocok |
| Template | File HTML yang dapat diisi data dinamis |
| Static asset | File yang umumnya dikirim apa adanya seperti CSS, JS, gambar |

---

# 9.2 Mengenal URL dan Route

Contoh route sederhana:

```python
from flask import Flask

app = Flask(__name__)

@app.get("/")
def home():
    return "Halo dari Flask"

@app.get("/about")
def about():
    return "Halaman About"
```

Jika browser membuka `/about`, Flask mencari route yang cocok dan menjalankan function `about()`.

## Route parameter

```python
@app.get("/hello/<name>")
def hello(name):
    return f"Halo, {name}"
```

Route parameter berguna ketika bagian URL mewakili identitas atau nilai dinamis. Namun pada Pertemuan 09 penggunaannya cukup dikenalkan; desain REST detail dibahas pada Pertemuan 10.

---

# 9.3 UI: Komponen yang Harus Dikenali

Buku panduan mengenalkan kosakata komponen agar mahasiswa dapat menyebut antarmuka secara tepat, bukan hanya berkata “bagian ini”.

| Kelompok | Contoh komponen | Tujuan |
|---|---|---|
| Layout | header, navbar, sidebar, main content, section, footer, container, grid, column | Menyusun struktur halaman |
| Text | heading, paragraph, label, caption, link | Menyampaikan informasi dan hierarki |
| Input | text, number, email, password, date, textarea, file input | Menerima data pengguna |
| Selection | checkbox, radio, select/dropdown, toggle, slider | Memilih satu/beberapa nilai |
| Action | button, submit button, icon button, cancel | Memicu aksi |
| Data display | card, table, list, badge, avatar, image, chart | Menampilkan data |
| Navigation | navbar, sidebar, tabs, breadcrumb, pagination, menu | Berpindah konteks/halaman |
| Feedback | alert, toast, modal, tooltip, spinner, progress bar, validation message | Memberi status terhadap aksi |
| Behavior | scroll, sticky, fixed, overflow, accordion, carousel | Mengatur interaksi/konten panjang |

Mahasiswa tidak diwajibkan memakai semua komponen. Yang penting adalah memahami **fungsi komponen** dan memilih komponen yang sesuai kebutuhan.

---

# 9.4 State UI/UX

Komponen tidak hanya memiliki bentuk, tetapi juga **state**.

| State | Arti | Contoh |
|---|---|---|
| Normal | Siap digunakan | Tombol “Simpan” aktif |
| Hover | Pointer berada di atas komponen | Tombol berubah tampilan |
| Focus | Input aktif untuk keyboard | Outline focus terlihat |
| Disabled | Aksi belum diizinkan | Tombol submit nonaktif |
| Loading | Proses sedang berlangsung | “Menyimpan…”/spinner |
| Error | Proses gagal atau data salah | Pesan validasi dekat field |
| Success | Aksi berhasil | Alert/flash “Data berhasil disimpan” |
| Empty | Belum ada data | Pesan “Belum ada produk” + aksi tambah |

State merupakan bagian dari fungsi aplikasi. Misalnya halaman daftar yang kosong **bukan halaman rusak**; aplikasi harus memiliki empty state yang menjelaskan apa yang dapat dilakukan pengguna berikutnya.

---

# 9.5 Prinsip UX Dasar yang Wajib

## 1. Hierarchy
Judul halaman, aksi utama, dan informasi penting harus mudah ditemukan. Jangan memberi semua elemen tingkat penekanan yang sama.

## 2. Consistency
Button dengan fungsi serupa seharusnya memiliki pola tampilan dan label yang konsisten. Format harga, jarak antar form, dan navigasi juga sebaiknya konsisten.

## 3. Feedback
Setelah pengguna mengirim form, aplikasi harus memberi respons. Jangan membuat pengguna menebak apakah data sudah tersimpan atau tidak.

## 4. Validation
Pesan validasi sebaiknya dekat dengan field yang salah dan menjelaskan tindakan perbaikan, misalnya:

```text
Harga harus berupa angka lebih besar atau sama dengan 0.
```

lebih berguna daripada:

```text
ERROR!
```

## 5. Accessibility dasar
- setiap input mempunyai `label`;
- focus keyboard tetap terlihat;
- teks mempunyai kontras yang cukup;
- gambar penting mempunyai teks alternatif bila relevan;
- jangan mengandalkan warna saja untuk menyampaikan error/success.

## 6. Responsive
Layout tetap dapat digunakan pada layar sempit. Table dapat dibuat memiliki horizontal overflow bila kolom banyak.

---

# 9.6 Membuat Environment Flask

Dari terminal VS Code:

```bash
python -m venv .venv
```

Aktifkan environment.

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Install dependency:

```bash
python -m pip install Flask
```

Simpan dependency:

```bash
python -m pip freeze > requirements.txt
```

Pada repository contoh, cukup gunakan:

```bash
python -m pip install -r requirements.txt
```

---

# 9.7 Flask First App dengan Template

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.get("/")
def home():
    return render_template("home.html", title="Home")

if __name__ == "__main__":
    app.run(debug=True)
```

Development server dapat dijalankan dengan:

```bash
python app.py
```

atau:

```bash
flask --app app run --debug
```

`debug=True` berguna **hanya untuk development lokal** karena menyediakan auto reload dan debugger. Production deployment dibahas pada Pertemuan 11 dan tidak menggunakan development server sebagai server production.

---

# 9.8 Struktur Project

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
    ├── css/
    │   └── style.css
    └── js/
        └── app.js
```

## Mengapa dipisahkan?
- `app.py`: route dan logic server.
- `templates/`: tampilan HTML dinamis.
- `static/`: CSS/JS yang dikirim sebagai asset.
- `test_app.py`: test route dan perilaku form.
- `requirements.txt`: dependency Python.
- `README.md`: petunjuk setup, run, test, dan struktur.

---

# 9.9 Jinja dan Template Inheritance

`base.html` dapat menjadi kerangka utama:

```html
<!doctype html>
<html lang="id">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{% block title %}Praktikum Flask{% endblock %}</title>
  <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
  <nav>
    <a href="{{ url_for('home') }}">Home</a>
    <a href="{{ url_for('product_list') }}">Produk</a>
  </nav>
  <main>
    {% block content %}{% endblock %}
  </main>
</body>
</html>
```

Halaman lain:

```html
{% extends "base.html" %}
{% block title %}Daftar Produk{% endblock %}
{% block content %}
  <h1>Daftar Produk</h1>
{% endblock %}
```

Keuntungan inheritance: navbar, metadata, dan struktur utama tidak perlu disalin berulang.

---

# 9.10 Menampilkan List/Dictionary ke Template

Python:

```python
products = [
    {"id": 1, "name": "Keyboard", "price": 250000, "stock": 10},
    {"id": 2, "name": "Mouse", "price": 120000, "stock": 6},
]

@app.get("/products")
def product_list():
    return render_template("products.html", products=products)
```

Jinja:

```html
{% if products %}
  <ul>
    {% for product in products %}
      <li>{{ product.name }} — stok {{ product.stock }}</li>
    {% endfor %}
  </ul>
{% else %}
  <p>Belum ada produk.</p>
{% endif %}
```

Catatan: data pertemuan ini masih dapat disimpan di memory. Database baru menjadi fokus pada Pertemuan 14–16.

---

# 9.11 Form GET dan POST

`GET` biasa digunakan untuk membaca halaman. `POST` digunakan saat form mengirim data yang akan diproses/menyebabkan perubahan state.

```python
from flask import request

@app.route("/products/new", methods=["GET", "POST"])
def product_new():
    errors = {}

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        price_raw = request.form.get("price", "")

        if not name:
            errors["name"] = "Nama wajib diisi."

        try:
            price = float(price_raw)
            if price < 0:
                raise ValueError
        except ValueError:
            errors["price"] = "Harga harus angka >= 0."

        if not errors:
            # simpan data
            pass

    return render_template("product_form.html", errors=errors)
```

HTML:

```html
<form method="post">
  <label for="name">Nama produk</label>
  <input id="name" name="name" required>

  {% if errors.get('name') %}
    <p role="alert">{{ errors['name'] }}</p>
  {% endif %}

  <button type="submit">Simpan</button>
</form>
```

## Mengapa validasi browser tidak cukup?
Atribut HTML seperti `required` membantu UX tetapi request tetap dapat dikirim tanpa browser normal. Karena itu backend harus memvalidasi lagi.

---

# 9.12 Redirect Setelah POST

Setelah penyimpanan berhasil, pola sederhana yang baik adalah:

```text
POST → validate → save → redirect → GET daftar
```

Ini mengurangi risiko form terkirim ulang ketika halaman direfresh.

```python
from flask import redirect, url_for

return redirect(url_for("product_list"))
```

---

# 9.13 Flash Message

```python
from flask import flash

flash("Produk berhasil ditambahkan.", "success")
```

Template dapat menampilkan flash sebagai feedback. Gunakan `SECRET_KEY` hanya untuk kebutuhan session/flash; pada aplikasi production nilainya tidak boleh hard-coded. Pengelolaan environment variable dibahas lebih lanjut pada Pertemuan 11.

---

# 9.14 Query Parameter untuk Search Sederhana

Search dapat menggunakan query parameter:

```text
/products?q=key
```

Python:

```python
q = request.args.get("q", "").strip().lower()
filtered = products
if q:
    filtered = [p for p in products if q in p["name"].lower()]
```

Ini menjadi jembatan menuju pemahaman query parameter pada API di Pertemuan 10.

---

# 9.15 404 dan Error Handler

```python
@app.errorhandler(404)
def not_found(error):
    return render_template("404.html"), 404
```

Status code tetap `404`; jangan hanya menampilkan halaman “tidak ditemukan” tetapi mengirim `200`.

---

# 9.16 Testing dengan Flask Test Client

```python
import unittest
import app as module

class FlaskWebTest(unittest.TestCase):
    def setUp(self):
        module.app.config.update(TESTING=True)
        self.client = module.app.test_client()

    def test_home(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
```

Test minimal sebaiknya mencakup:

1. home `200`;
2. about `200`;
3. list `200`;
4. form GET `200`;
5. POST valid;
6. nama kosong;
7. harga negatif;
8. stok bukan integer;
9. search menghasilkan data;
10. route tidak ada `404`.

---

# 9.17 Troubleshooting Web Berdasarkan Bukti

| Gejala | Kemungkinan penyebab | Pemeriksaan/perbaikan |
|---|---|---|
| `404 Not Found` | route/URL tidak cocok | cek decorator `@app.route` dan URL browser |
| `405 Method Not Allowed` | route tidak menerima method | cek `methods=[...]` atau `@app.post` |
| `500 Internal Server Error` | exception backend | baca traceback terminal |
| `TemplateNotFound` | nama/lokasi template salah | pastikan folder `templates/` dan case nama file |
| CSS tidak masuk | static path/cache | gunakan `url_for('static', filename=...)`, hard refresh |
| form selalu kosong | atribut `name` tidak cocok | cocokkan HTML dengan key `request.form` |
| angka melempar `ValueError` | konversi input gagal | validasi dan tangani exception |
| hasil tidak berubah | state/data berbeda dari dugaan | print/log nilai sementara, lalu retest |
| port dipakai | server lama masih berjalan | hentikan proses lama atau pilih port lain |

## Prosedur debug yang disarankan

```text
REPRODUCE
→ BACA STATUS/TRACEBACK
→ TENTUKAN ROUTE/FILE/BARIS
→ BUAT HIPOTESIS
→ UJI PERUBAHAN KECIL
→ RETEST KASUS GAGAL
→ REGRESSION TEST
```

---

# 9.18 Challenge Mandiri

Tanpa menambah framework frontend, ubah project contoh agar mempunyai:

- search produk;
- empty state;
- badge stok “habis” ketika `stock == 0`;
- validasi nama duplikat;
- pesan error dekat field;
- responsive table;
- satu route detail produk atau satu halaman tambahan;
- minimal dua test baru untuk fitur tersebut.

Mahasiswa harus menjelaskan file yang diubah dan alasan perubahan.

---

# 9.19 Checklist Sebelum Selesai

- [ ] Flask dapat dijalankan dari environment baru.
- [ ] Minimal tiga halaman dapat dibuka.
- [ ] Template inheritance digunakan.
- [ ] CSS dimuat melalui `url_for('static', ...)`.
- [ ] Form memiliki label dan `name` yang benar.
- [ ] Server-side validation aktif.
- [ ] Ada feedback error dan success.
- [ ] Halaman list mempunyai empty state.
- [ ] Layout dapat digunakan pada layar sempit.
- [ ] Route tidak ada mengembalikan 404.
- [ ] Unit/integration test lulus.
- [ ] Tidak ada secret yang di-commit.

## Exit Ticket
Jawab tanpa melihat catatan:

1. Apa beda route dengan template?
2. Mengapa form `POST` tetap perlu validasi Python walaupun HTML menggunakan `required`?
3. Apa beda `404` dan `500`?
4. Mengapa `url_for()` lebih baik daripada menulis path static secara sembarang?
5. Apa yang dimaksud empty state?
6. Jelaskan aliran request dari browser sampai response kembali ke browser.

## Referensi Internal
- `Jobsheet.md` — langkah praktik terstruktur.
- `TugasVideo.md` — tugas demonstrasi.
- `praktikum/flask-web/` — aplikasi runnable.
- `praktikum/UI_UX_CHECKLIST.md` — checklist evaluasi interface.
- `praktikum/TESTING.md` — skenario pengujian manual dan otomatis.
