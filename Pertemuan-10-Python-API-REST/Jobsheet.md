# Jobsheet Pertemuan 10 — REST API Python

## Setup
```bash
cd praktikum/rest-api
python -m venv .venv
python -m pip install -r requirements.txt
python app.py
```
Server: `http://127.0.0.1:5000`.

## Percobaan Wajib
1. `GET /api/health`.
2. `GET /api/products` dan detail ID.
3. `POST /api/products` valid/invalid.
4. `PATCH /api/products/<id>`.
5. `DELETE /api/products/<id>`.
6. Jalankan `client.py` dengan timeout/error handling.
7. Jalankan curl examples.
8. Jalankan unit test.

## Test
```bash
python -m unittest -v test_api.py
```
Uji status 200, 201, 204, 400, 404, 409 serta payload JSON.

## Analisis
- Bedakan 400, 404, 409, 500.
- Mengapa timeout wajib pada client network?
- Mengapa server-side validation tetap diperlukan?
- Kapan CORS relevan?

## Keamanan
Jangan taruh API key/token sungguhan di kode, log, screenshot, video, atau repository.
