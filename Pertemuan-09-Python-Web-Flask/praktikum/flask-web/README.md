# Flask Web — Pertemuan 09

Contoh runnable untuk route, template, form, pencarian, validasi, halaman detail, 404, dan automated test.

## Menjalankan
```bash
python -m venv .venv
python -m pip install -r requirements.txt
python app.py
```
Buka `http://127.0.0.1:5000`.

## Test
```bash
python -m unittest -v test_app.py
```

Route utama: `/`, `/about`, `/products`, `/products?q=key`, `/products/<id>`, dan `/products/new`. Data contoh disimpan di memori sehingga kembali ke kondisi awal saat server dimulai ulang.

Gunakan `../../Jobsheet.md` dan `../UI_UX_CHECKLIST.md` untuk langkah praktik lengkap.
