# Materi Pertemuan 15 — Node + Python + Database Terstruktur

## Target
Data modeling entity/key/relationship, PK/FK/JOIN/transaction, backend route-service-repository, validation/error contract, security dasar, Node UI mengonsumsi API.

Contoh model: `categories 1 → N products`. Route menangani HTTP, service aturan bisnis, repository query. Jangan memaksakan layer tanpa manfaat, tetapi tanggung jawab harus jelas.

Gunakan parameterized query. Password tidak plaintext jika login ditambahkan. Secret/database URL di environment variable. Authentication menjawab siapa; authorization bolehkah aksi. Validasi tetap di backend.

Transaction dipakai ketika beberapa perubahan harus berhasil bersama. Error contract konsisten memudahkan frontend.
