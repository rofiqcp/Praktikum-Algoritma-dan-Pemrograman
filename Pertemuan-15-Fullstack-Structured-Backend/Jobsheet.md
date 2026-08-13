# Jobsheet Pertemuan 15 — Structured Backend + Relational DB

## Setup Backend
```bash
cd praktikum/structured-app/backend
python -m venv .venv
python -m pip install -r requirements.txt
python main.py
python -m unittest -v test_backend.py
```

## Setup Frontend
```bash
cd ../frontend
npm install
npm start
```

## Percobaan Wajib
1. Baca schema categories/products/stock_movements.
2. Jalankan JOIN list produk + nama kategori.
3. Create produk dengan validasi FK.
4. Update produk.
5. Delete produk/not-found.
6. Mutasi stok dalam transaction.
7. Uji error contract validation/not-found/conflict.
8. Node UI memanggil backend.
9. Jalankan backend unit tests.

## Code Review Checklist
- route hanya menangani HTTP?
- service memegang business rule?
- repository melakukan SQL parameterized?
- transaction dipakai pada multi-step write?
- response error konsisten?
- frontend menangani loading/empty/error/success?

## Challenge
Tambahkan filter kategori atau low-stock endpoint beserta unit test dan regression test.
