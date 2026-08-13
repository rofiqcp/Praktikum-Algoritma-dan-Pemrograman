# Materi Pertemuan 15 — Node + Python + Database Terstruktur

> Sumber utama: *Buku Panduan Praktik: Pemrograman Dasar hingga Full Stack — 16 Pertemuan Terstruktur, Edisi Agustus 2026*.

Sesi ini memperkuat full-stack preparation: desain data relasional, backend terstruktur, validation, transaction, dan security dasar.

## Target Kompetensi
- Mendesain entity, primary key, foreign key, dan relationship.
- Menggunakan JOIN dan transaction dasar.
- Memisahkan route, service, repository/data-access, schema, dan DB connection secara proporsional.
- Membuat error contract yang konsisten.
- Mengenal PostgreSQL dan ORM sebagai langkah lanjut.
- Menerapkan keamanan dasar: secret, hashing concept, injection prevention, auth vs authorization.

## Output
- Backend Python terstruktur.
- Database minimal dua tabel berelasi.
- Node frontend mengonsumsi API.
- Dokumentasi schema dan endpoint.

## Alur 180 Menit
| Tahap | Durasi | Aktivitas |
|---|---:|---|
| Data modeling | 30 | Entity, key, relationship |
| SQL relation | 25 | FK, JOIN, transaction |
| Backend layers | 30 | route/service/repository |
| Validation | 25 | schema dan error format |
| Security basics | 25 | secret, injection, password |
| Integration | 30 | Node UI + backend |
| Prep final | 15 | Scope dan test strategy |

## 15.1 Contoh Data Model
```text
categories
- id (PK)
- name

products
- id (PK)
- category_id (FK -> categories.id)
- name
- price
- stock

CATEGORY 1 → HAS MANY → PRODUCT N
```

## 15.2 JOIN Dasar
```sql
SELECT products.id,products.name,products.price,
       categories.name AS category_name
FROM products
JOIN categories ON categories.id=products.category_id
ORDER BY products.name;
```

## 15.3 Backend Layering
```text
backend/
├── main.py
├── routes/products.py
├── services/product_service.py
├── repositories/product_repository.py
├── schemas/product.py
└── db/connection.py
```
Tujuannya membuat tanggung jawab jelas, bukan membuat layer sebanyak mungkin. Untuk project kecil, layer yang tidak memberi nilai pendidikan boleh disederhanakan.

## 15.4 Validation dan Error Contract
```json
{
  "error": {
    "code": "INVALID_STOCK",
    "message": "Stock tidak boleh negatif",
    "details": {"field":"stock"}
  }
}
```
Bedakan validation error, not-found, conflict, dan internal error.

## 15.5 Transaction
Jika beberapa perubahan harus berhasil bersama, gunakan transaction. Contoh penjualan: kurangi stok + buat record transaksi; jika salah satu gagal, semuanya di-rollback.

## 15.6 SQLite vs PostgreSQL
SQLite sederhana dan sangat cocok belajar CRUD/SQL lokal. PostgreSQL lebih umum untuk workload multi-client/cloud. File SQLite lokal tidak selalu cocok pada filesystem serverless/ephemeral.

## 15.7 ORM
ORM seperti SQLAlchemy memetakan objek ke tabel. Raw SQL memperkuat pemahaman query dan memberi kontrol; ORM mengurangi boilerplate. Buku tidak mewajibkan ORM untuk semua final project.

## 15.8 Security Minimum
- Parameterized query; jangan concatenate input ke SQL.
- Password tidak disimpan plaintext bila fitur login digunakan.
- Secret/database URL via environment variable.
- Authentication = siapa pengguna; authorization = apakah ia boleh melakukan aksi.
- Backend tetap memvalidasi meski frontend sudah validasi.
- Jangan tampilkan stack trace/secret ke user publik.

## Troubleshooting
| Gejala | Arah perbaikan |
|---|---|
| Foreign key error | validasi parent sebelum insert/update |
| Duplicate data | unique constraint + tangani conflict |
| Partial update | transaction |
| SQL injection risk | parameterized query/ORM |
| Frontend bingung error | error contract stabil |
| Works local, fail deploy | path SQLite/ephemeral storage/env |
