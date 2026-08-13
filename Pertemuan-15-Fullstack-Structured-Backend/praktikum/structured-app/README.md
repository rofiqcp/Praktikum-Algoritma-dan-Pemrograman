# Structured Full-stack Preparation

## Architecture
```text
Node static UI :3000
  → Browser fetch
Python Flask :5001
  routes → services → repositories → SQLite
                     ↘ schema validation
```

Python adalah pemilik database. Node/frontend mengakses data melalui HTTP API, bukan membaca SQLite secara langsung.

## Backend
```bash
cd backend
python -m venv .venv
python -m pip install -r requirements.txt
python -m unittest -v test_backend.py
python main.py
```

Default lokal dapat langsung digunakan. Untuk konfigurasi lain, gunakan environment variable yang dicontohkan pada `.env.example`: `API_PORT`, `DATABASE_PATH`, `CORS_ORIGINS`, dan `FLASK_DEBUG`. File `.env.example` adalah referensi nilai; set variable melalui shell/IDE/platform deployment yang digunakan.

## Frontend
Buka terminal kedua:
```bash
cd frontend
npm install
npm start
```
Buka `http://127.0.0.1:3000`.

## Verifikasi Wajib
- `/api/health` merespons 200;
- list produk berisi `category_name` dari JOIN;
- search dan category filter bekerja;
- create menolak kategori yang tidak ada;
- input tidak valid dan field tidak dikenal menghasilkan 400;
- mutasi stok memakai transaksi dan menolak hasil stok negatif;
- UI menunjukkan loading, empty, success, dan error;
- test backend lulus pada database sementara.

`app.db` adalah file runtime dan tidak perlu di-commit.
