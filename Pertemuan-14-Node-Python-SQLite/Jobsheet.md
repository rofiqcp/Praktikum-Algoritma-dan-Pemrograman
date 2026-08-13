# Jobsheet Pertemuan 14 — Node + Python + SQLite

## Terminal 1 — Backend
```bash
cd praktikum/integrated-app/backend
python -m venv .venv
python -m pip install -r requirements.txt
python app.py
```
Backend: `http://127.0.0.1:5001`.

## Terminal 2 — Frontend
```bash
cd praktikum/integrated-app/frontend
npm install
npm start
```
Frontend: `http://127.0.0.1:3000`.

## Percobaan Wajib
1. Backend `/api/health`.
2. SQLite dibuat otomatis dan seed data muncul.
3. Frontend mengambil list dari Python.
4. Create product dari browser.
5. Update stock lewat API/curl.
6. Delete resource.
7. Uji validation dan not-found.
8. Matikan backend lalu amati frontend error state.
9. Jalankan backend tests.

## Layer Failure Drill
- backend mati → network/connection error;
- CORS dimatikan → browser CORS error;
- endpoint salah → 404;
- payload salah → 400;
- SQL constraint → conflict/validation.

## Analisis
Jelaskan layer mana yang bertanggung jawab untuk UI, HTTP, business validation, dan persistence.
