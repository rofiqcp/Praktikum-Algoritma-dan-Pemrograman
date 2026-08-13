# Deploy Flask Starter

## Lokal
```bash
python -m venv .venv
python -m pip install -r requirements.txt
python app.py
python -m unittest -v test_app.py
```

## Production-style start
```bash
gunicorn app:app
```

## Environment
Salin nama variable dari `.env.example`, tetapi masukkan nilai secret pada environment/dashboard target. Jangan commit `.env`.

## Verifikasi
- `/` mengembalikan response.
- `/health` → JSON `status: ok`.
- build log tidak error.
- runtime log menunjukkan proses aktif.
- public URL dapat diakses dari perangkat lain.

Platform deployment berubah dari waktu ke waktu; ikuti dokumentasi resmi target untuk build/start/runtime yang aktual.
