# Materi Pertemuan 14 — Integrasi Node.js + Python API + SQLite Sederhana

> Sumber utama: *Buku Panduan Praktik: Pemrograman Dasar hingga Full Stack — 16 Pertemuan Terstruktur, Edisi Agustus 2026*.

Pertemuan ini mengubah aplikasi satu service menjadi aplikasi yang memiliki beberapa layer: browser/Node web, Python API, dan SQLite.

## Target Kompetensi
- Menjelaskan komunikasi service melalui HTTP.
- Menjalankan Node frontend dan Python backend secara bersamaan.
- Menggunakan `fetch` dari browser ke Python API.
- Memahami CORS ketika origin frontend/backend berbeda.
- Membuat SQLite sederhana dan CRUD menggunakan parameterized query.
- Mendiagnosis error berdasarkan layer.

## Output
- Mini integrated app Node + Python API + SQLite.
- CRUD resource sederhana.
- Bukti request end-to-end dan database berubah.

## Arsitektur
```text
BROWSER :3000
   ↓ static page + fetch
NODE/EXPRESS :3000
   ↓ browser request lintas origin
PYTHON/FLASK API :5001
   ↓ SQL parameterized
SQLITE DATABASE
```

## SQLite
SQLite menyimpan database pada file lokal. Untuk kelas, ini cocok untuk memahami tabel, primary key, query, dan CRUD tanpa mengelola database server.

```sql
CREATE TABLE products (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL UNIQUE,
  price REAL NOT NULL CHECK(price >= 0),
  stock INTEGER NOT NULL CHECK(stock >= 0)
);
```

## Parameterized Query
Jangan membangun SQL dengan concatenation input pengguna.
```python
conn.execute("SELECT * FROM products WHERE id = ?", (product_id,))
```

## CORS
Jika frontend `http://127.0.0.1:3000` memanggil backend `http://127.0.0.1:5001`, origin berbeda. Browser menerapkan CORS. `curl`/Python requests tidak mengalami kebijakan browser dengan cara yang sama.

## CRUD
- Create → `POST /api/products`
- Read → `GET /api/products`
- Update → `PATCH /api/products/<id>`
- Delete → `DELETE /api/products/<id>`

## Debug Berdasarkan Layer
```text
UI/DOM → FETCH → NETWORK/HTTP → CORS → PYTHON ROUTE → BUSINESS RULE → SQL → DATABASE
```
- Browser console untuk JS/CORS.
- Network tab untuk method/status/body.
- Python terminal untuk traceback/log.
- Query/database untuk data salah tetapi HTTP 200.
