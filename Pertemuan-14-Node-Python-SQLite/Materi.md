# Materi Pertemuan 14 — Integrasi Node.js + Python Backend + SQLite

## Target
Memisahkan frontend Node dan backend Python, melakukan komunikasi HTTP/fetch, memahami CORS, membuat SQLite CRUD sederhana dan menelusuri error per layer.

Arsitektur: `Browser/Node UI → HTTP → Python API → SQLite`. Frontend tidak mengakses database langsung. Gunakan parameterized query `?`, bukan string concatenation input.

SQLite cocok untuk belajar CRUD lokal. CORS muncul ketika browser membaca resource dari origin berbeda. Contoh lokal membatasi origin ke `http://localhost:3000`.

Diagnosis per layer: UI → Network/HTTP → Python route/business logic → SQL/database.
