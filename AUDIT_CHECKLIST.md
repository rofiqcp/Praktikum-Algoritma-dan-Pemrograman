# Checklist Audit Repository Praktikum

Gunakan sebelum release/semester baru.

## Struktur
- [ ] 16 folder pertemuan tersedia.
- [ ] Semua pertemuan punya `Materi.md` dan `Jobsheet.md`.
- [ ] P01–07,09–11,13–15 punya `TugasVideo.md`.
- [ ] P08, P12, P16 punya `Project.md` dan tidak bergantung pada `TugasVideo.md`.
- [ ] Semua pertemuan punya `praktikum/README.md`.

## Materi
- [ ] Target kompetensi sesuai buku.
- [ ] Output pertemuan sesuai buku.
- [ ] Istilah konsisten.
- [ ] Troubleshooting tersedia.
- [ ] Contoh runnable sesuai konsep.

## Runnable
- [ ] Python dapat di-compile.
- [ ] Notebook valid JSON.
- [ ] Test Python berjalan setelah dependency tersedia.
- [ ] `package.json` valid JSON.
- [ ] Node source lolos syntax check.
- [ ] README praktikum berisi command run.
- [ ] Tidak ada path absolut komputer pembuat.

## Web/API
- [ ] Route/endpoint terdokumentasi.
- [ ] Status code sesuai.
- [ ] Validation error dibedakan dari 404/409/500.
- [ ] Timeout/error handling tersedia untuk external API.
- [ ] CORS dijelaskan bila browser cross-origin.

## Database
- [ ] SQL parameterized.
- [ ] Foreign key diaktifkan bila digunakan.
- [ ] Constraint dasar tersedia.
- [ ] Transaction digunakan untuk perubahan atomic.
- [ ] File database runtime di-ignore bila tidak perlu versioning.

## Security
- [ ] `.env` di-ignore.
- [ ] Tidak ada token/API key/password nyata.
- [ ] Secret via environment.
- [ ] Traceback internal tidak diekspos sebagai response publik.
- [ ] Backend tetap validasi walaupun frontend validasi.

## Assessment
- [ ] Jobsheet punya test normal/boundary/invalid/failure.
- [ ] Tugas video menuntut program benar-benar dijalankan.
- [ ] Project punya requirement/deliverable terukur.
- [ ] Rubrik menilai proses, testing, dokumentasi, dan penjelasan.
