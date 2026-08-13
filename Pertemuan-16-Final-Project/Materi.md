# Materi Pertemuan 16 — Final Project: Full Stack Node.js + Python + Database

> Sumber utama: *Buku Panduan Praktik: Pemrograman Dasar hingga Full Stack — 16 Pertemuan Terstruktur, Edisi Agustus 2026*.

Peserta memilih satu dari 30 variasi final. Semua project memiliki bobot inti setara: **Node.js untuk web/frontend layer, Python untuk backend API/business logic, database relasional minimal dua tabel, dan integrasi end-to-end**.

## Target Kompetensi
- Menyusun arsitektur sebelum implementasi.
- Membangun Node.js/Express web layer.
- Membangun Python API terstruktur.
- Mendesain database relasional minimal dua tabel.
- Menerapkan CRUD, validation, error handling, dan minimal satu relationship.
- Menggunakan Git/GitHub dan melakukan deployment sesuai kemampuan platform.
- Mendemonstrasikan test dan troubleshooting.

## Output
- Source lengkap + GitHub.
- Database schema/ERD.
- API documentation.
- Public deployment atau demonstrasi lokal end-to-end jika batas platform menghalangi, dengan bukti konfigurasi deployment.
- Presentasi final 7–10 menit.

## Requirement Wajib
- Node.js + Express: halaman/dashboard dan static frontend.
- Python backend: Flask/FastAPI REST API dengan validation.
- Database: minimal 2 tabel + relasi one-to-many; 3 tabel dianjurkan.
- CRUD minimal resource utama: list/detail/create/update/delete.
- Search/filter atau pagination sederhana.
- Loading, empty, success, dan error state pada UI.
- Environment variable untuk service/database config.
- Minimal 15 test case + satu catatan bug selama development.
- Git history menunjukkan setup, backend, database, frontend, integration, fix, docs.
- README menjelaskan architecture, setup, env placeholder, run commands, API, dan deployment.

## Rubrik Final
| Aspek | Bobot |
|---|---:|
| Analisis & desain/ERD | 10 |
| Node web/UI | 15 |
| Python API/business logic | 20 |
| Database & relasi | 15 |
| Integrasi end-to-end | 15 |
| Validation/error/security basics | 10 |
| Testing/troubleshooting | 7 |
| Git/docs/deploy | 5 |
| Demo & pemahaman | 3 |

## Arsitektur Acuan
```text
BROWSER
  ↓
NODE/EXPRESS WEB LAYER
  ↓ fetch/HTTP
PYTHON REST API / BUSINESS LOGIC
  ↓ parameterized SQL / transaction
RELATIONAL DATABASE
```

## Definition of Done
Project belum selesai hanya karena halaman tampil. Selesai berarti: request end-to-end benar, state tersimpan di DB, error state diuji, test terdokumentasi, Git history masuk akal, setup dapat diulang orang lain, dan mahasiswa dapat menjelaskan arsitektur tanpa mengandalkan AI/copy-paste.

Bank project lengkap ada di `Project.md`; starter pada `praktikum/final-starter/` hanya referensi teknis.
