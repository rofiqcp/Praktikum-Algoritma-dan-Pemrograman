# Jobsheet Pertemuan 07 — VS Code, Python Lokal, Git, dan GitHub

## Tujuan Praktikum
Membuktikan workflow lokal end-to-end: editor → interpreter → venv → terminal → test → Git → GitHub.

## Persiapan
Cek:
```bash
python --version
python -m pip --version
git --version
```
Pilih interpreter `.venv` di VS Code.

## Percobaan Wajib
1. Buat dan aktifkan `.venv`.
2. Jalankan `python-local/main.py` dari terminal.
3. Jalankan `debug_demo.py`, baca error, lalu perbaiki pada salinan kerja.
4. Jalankan unit test.
5. `git init/status/add/commit` dengan minimal tiga commit bermakna.
6. Buat remote GitHub, push, ubah README, lalu pull/clone untuk membuktikan sinkronisasi.

## Perintah Test
```bash
cd praktikum/python-local
python main.py
python -m unittest discover -s tests -v
```

## Bukti Wajib
- `python --version` dan interpreter VS Code.
- venv aktif.
- output program dan unit test.
- `git log --oneline` minimal 3 commit.
- repo GitHub dan README.
- `.env`/`.venv` tidak ikut commit.

## Analisis
1. Apa beda editor dan interpreter?
2. Mengapa package bisa “installed” tetapi tetap `ModuleNotFoundError`?
3. Apa fungsi staging area Git?
4. Mengapa secret yang pernah ter-push harus dirotasi, bukan hanya dihapus dari file terbaru?
