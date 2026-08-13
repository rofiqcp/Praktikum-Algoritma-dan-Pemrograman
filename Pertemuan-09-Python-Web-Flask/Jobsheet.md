# Jobsheet Pertemuan 09 — Flask Web Lokal

## Setup
```bash
cd praktikum/flask-web
python -m venv .venv
# aktifkan venv
python -m pip install -r requirements.txt
python app.py
```
Buka `http://127.0.0.1:5000`.

## Percobaan Wajib
1. Route `/`, `/about`, `/products`.
2. Template inheritance dengan `base.html`.
3. Static CSS dan JS.
4. Tabel/list produk dan empty state.
5. Form `/products/new` GET/POST.
6. Validasi nama, harga, dan stok server-side.
7. Halaman 404.
8. Unit test Flask.

## Test
```bash
python -m unittest -v test_app.py
```
Uji manual juga: 200 route benar, 404 route salah, form valid, nama kosong, harga negatif, stok bukan integer, dan data berhasil muncul sesudah submit.

## Debug Berbasis Layer
- Browser/UI: inspect field/name/static.
- HTTP: URL/method/status.
- Flask: route/traceback/template.
- Business logic: validation/data.

## Challenge
Tambah edit/delete atau filter produk tanpa framework frontend tambahan; tambahkan test dan regression test.
