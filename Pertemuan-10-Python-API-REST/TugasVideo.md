# Tugas Video — Pertemuan 10

## Tema
**Membaca HTTP, Mengonsumsi API, dan Membuat REST API Python yang Diuji**

Durasi rekomendasi: **15–25 menit**.

## Bagian Wajib

### 1. Mental Model HTTP — 2 menit
Jelaskan request dan response. Tunjukkan satu contoh nyata dari API lokal dan sebutkan method, path, query parameter bila ada, status code, Content-Type, dan body.

### 2. REST CRUD — 3–4 menit
Demonstrasikan minimal:

- GET collection;
- GET detail;
- POST valid;
- PATCH valid;
- DELETE;
- satu request not found.

Jelaskan mengapa setiap method dipilih.

### 3. Status Code — 2 menit
Tunjukkan contoh minimal tiga status berbeda, misalnya 200, 201, 400/409, dan 404. Jelaskan bahwa status code adalah bagian kontrak API.

### 4. Client Python — 3 menit
Jalankan `client.py`. Tunjukkan `timeout`, parsing JSON, dan error handling. Matikan server atau gunakan skenario error agar dapat menjelaskan failure path.

### 5. Validation dan Error Contract — 2–3 menit
Kirim minimal dua input salah: nama kosong, nilai negatif, tipe salah, duplikat, atau ID tidak ada. Tunjukkan response error dan status code.

### 6. API Families — 2 menit
Dengan diagram/slide sederhana, jelaskan perbedaan REST, GraphQL, WebSocket, SSE, dan Webhook. SOAP/RPC/gRPC cukup dikenalkan singkat.

### 7. Auth dan CORS — 2 menit
Jelaskan konsep API key/Basic/Bearer/JWT/OAuth tanpa menggunakan credential nyata. Jelaskan mengapa curl/Python dapat berhasil sementara browser mengalami CORS.

### 8. Testing dan Debugging — 2–3 menit
Jalankan:

```bash
python -m unittest -v test_api.py
```

Tunjukkan satu bug/error dengan format:

```text
Gejala → Method/URL → Status/Log → Root Cause → Perbaikan → Retest
```

### 9. Modifikasi Mandiri — 2 menit
Tunjukkan minimal satu fitur tambahan: search/filter, stats endpoint, validasi duplikat, PATCH whitelist, pagination, atau mock external API.

## Bukti Wajib pada Video
- server API berjalan;
- minimal satu request dari curl/alat sejenis;
- `client.py` berjalan;
- JSON response terlihat;
- satu validation error;
- satu not-found/method error;
- hasil automated test;
- Git commit perubahan.

## Rubrik 100 Poin
| Aspek | Bobot |
|---|---:|
| HTTP & status code | 20 |
| REST CRUD | 20 |
| Client/integrasi | 15 |
| Validation & error handling | 15 |
| API families, auth, CORS | 10 |
| Testing & debugging | 15 |
| Penyampaian | 5 |

## Ketentuan
- Jangan menampilkan credential nyata.
- Jangan sekadar membaca dokumentasi; tunjukkan request/response nyata.
- Program pada akhir video harus kembali dalam kondisi berjalan dan test lulus.
