# Integrated App — Node + Python + SQLite

## Arsitektur
```text
Browser http://127.0.0.1:3000
  └─ Node/Express static frontend
       └─ browser fetch → http://127.0.0.1:5001/api
            └─ Flask API → sqlite3 → app.db
```

## Backend
```bash
cd backend
python -m venv .venv
python -m pip install -r requirements.txt
python app.py
python -m unittest -v test_app.py
```

## Frontend
```bash
cd frontend
npm install
npm start
```

## Verifikasi
1. Buka frontend.
2. List produk muncul dari Python API.
3. Tambah produk dari form.
4. Refresh: data tetap karena SQLite.
5. Matikan backend: UI harus menampilkan error, bukan diam.
6. Nyalakan kembali backend dan reload.

Database `app.db` adalah file runtime dan tidak perlu di-commit.
