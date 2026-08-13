# Materi Pertemuan 11 — Deployment dari GitHub

## Target
Membedakan local development/build/deploy/runtime/domain/environment variable, menyiapkan requirements/entrypoint, deploy minimal satu platform, dan membaca build/runtime logs.

Alur: source lokal → Git commit/push → platform clone/build/install → start command → runtime/public URL. Secret dipindahkan ke environment variable, bukan repo.

Platform yang dibahas buku: Vercel, Render, Railway, PythonAnywhere dan static hosting. Detail plan, runtime dan command dapat berubah; selalu verifikasi dokumentasi resmi sebelum kelas.

Diagnosis: build fail=dependency/config; deploy sukses tapi 500=runtime log; env hilang=cek environment variable; works local/fail cloud=port/path/filesystem/version.
