# Tugas Video — Pertemuan 11

## Tema
**Deployment Flask dari GitHub sampai Public URL**

Durasi rekomendasi: **15–25 menit**.

## Urutan Demo Wajib

1. **Local readiness** — jalankan aplikasi dan `python -m unittest -v test_app.py`.
2. **Struktur project** — jelaskan `app.py`, `requirements.txt`, `.gitignore`, `.env.example`, `Procfile` atau start command, dan README.
3. **Mental model** — jelaskan alur `local → Git commit → GitHub → build → start → runtime → public URL`.
4. **Repository dan branch** — tunjukkan repository, branch, serta commit yang dideploy.
5. **Proses deployment** — tunjukkan build dan proses start pada platform yang digunakan di kelas.
6. **Log** — pilih beberapa baris build/runtime log yang membuktikan apa yang sedang terjadi.
7. **Public verification** — buka `/`, `/health`, satu fitur utama, dan satu route yang tidak ada.
8. **Failure drill** — jelaskan satu contoh build, start, atau runtime failure dengan urutan `gejala → bukti → root cause → perbaikan → redeploy → retest`.
9. **Dokumentasi** — tunjukkan README bagian local setup, test, deployment, verification, troubleshooting, dan known limitations.

## Bukti yang Harus Terlihat

- automated test lokal lulus;
- Git history;
- branch/commit deployment;
- proses build/start;
- public URL;
- `/health` berhasil;
- satu failure drill;
- hasil retest setelah perbaikan.

## Rubrik 100 Poin

| Aspek | Bobot |
|---|---:|
| Local readiness | 15 |
| Deployment mental model | 15 |
| Struktur production dan konfigurasi | 15 |
| Proses deploy dan public verification | 20 |
| Log analysis dan troubleshooting | 20 |
| Dokumentasi | 10 |
| Penyampaian | 5 |

## Catatan
Gunakan konfigurasi contoh yang aman pada rekaman. Fokus penilaian adalah kemampuan menjelaskan proses dan membuktikan hasil, bukan nama platform cloud tertentu.
