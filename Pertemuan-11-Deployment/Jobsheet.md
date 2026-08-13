# Jobsheet Pertemuan 11 — Deployment

## Praktik Lokal Dulu
```bash
cd praktikum/deploy-flask
python -m venv .venv
python -m pip install -r requirements.txt
python app.py
python -m unittest -v test_app.py
```
Verifikasi `/`, `/health`, dan environment variable sebelum push.

## Checklist Sebelum Deploy
- `requirements.txt` lengkap.
- Start command/entrypoint benar.
- `.gitignore` mengabaikan `.env` dan venv.
- `.env.example` tidak berisi secret nyata.
- Aplikasi membaca `PORT`/environment sesuai kebutuhan target.
- Repo berhasil dijalankan dari clone bersih.
- README mencatat perintah run dan deploy.

## Praktik Deployment
1. Push repo ke GitHub.
2. Pilih satu platform yang disetujui pengajar.
3. Hubungkan repo/branch.
4. Konfigurasi build/start command sesuai dokumentasi resmi platform.
5. Masukkan environment variable pada dashboard platform, bukan source.
6. Deploy.
7. Baca build log dan runtime log.
8. Uji public URL dari perangkat/browser lain.
9. Uji `/health`.
10. Simpan screenshot/log bukti.

## Failure Drill
Buat satu kesalahan aman pada branch latihan, misalnya dependency hilang atau env var salah nama. Prediksi layer gagal, deploy/reproduce, baca log, fix, lalu redeploy.

## Deliverable
Public URL, repository GitHub, README deployment, screenshot/log, test table, dan catatan satu failure drill.
