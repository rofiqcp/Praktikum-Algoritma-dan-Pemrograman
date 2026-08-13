# Materi Pertemuan 12 — Project Checkpoint 2: Python Web + API + Deployment

> Sumber utama: *Buku Panduan Praktik: Pemrograman Dasar hingga Full Stack — 16 Pertemuan Terstruktur, Edisi Agustus 2026*.

Pertemuan 12 adalah checkpoint kompetensi pertemuan 9–11. Peserta memilih satu dari 30 project dan menggabungkan Flask web, UI sederhana, REST API internal, integrasi external/mock API, GitHub, serta deployment publik.

## Target Kompetensi
- Merancang halaman dan endpoint sebelum coding.
- Membuat website Flask minimal tiga route halaman.
- Menyediakan REST API JSON minimal GET dan POST; PATCH/DELETE jika relevan.
- Menggunakan minimal satu API publik atau mock API yang disediakan pengajar.
- Mendeploy dan membuktikan aplikasi dapat diakses publik.

## Output
- Public URL.
- GitHub repository.
- Dokumentasi endpoint.
- Test report dan demo.

## Requirement Setara
- Minimal 3 halaman: dashboard/home, list data, form/detail.
- Minimal 6 komponen UI berbeda.
- REST API sendiri: GET collection, GET detail atau POST, dan satu operasi perubahan data.
- Minimal satu request external/mock API dengan timeout/error handling.
- Environment variable untuk credential/config sensitif.
- Deploy dari GitHub dan test dari URL publik.

## Rubrik
| Aspek | Bobot |
|---|---:|
| UI & alur pengguna | 15 |
| Backend Flask | 20 |
| API sendiri | 20 |
| Integrasi API eksternal/mock | 10 |
| Validation & error state | 10 |
| Deployment & config | 15 |
| Dokumentasi/testing/demo | 10 |

## Workflow
```text
USER FLOW → PAGE MAP → ENDPOINT CONTRACT → MOCK/EXTERNAL API CONTRACT
→ IMPLEMENT INTERNAL FEATURE → INTEGRATE EXTERNAL DATA → ERROR STATES
→ TEST → GIT → DEPLOY → PUBLIC REGRESSION TEST → DOCS/DEMO
```

Bank lengkap ada di `Project.md`. Starter `praktikum/starter-web-api/` menunjukkan struktur teknis saja.
