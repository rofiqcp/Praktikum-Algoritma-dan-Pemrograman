# Jobsheet Pertemuan 10 — Python API: HTTP, JSON, REST, Integrasi, dan Testing

## Identitas
- Nama:
- NIM/Kelas:
- Tanggal:
- OS:
- Versi Python:
- Link repository:

## Tujuan Praktikum
Mahasiswa membangun dan menguji REST API Python sederhana, menjalankan client Python, membaca request/response HTTP, menggunakan JSON, mempraktikkan CRUD, status code, timeout, dan troubleshooting berdasarkan bukti.

## Persiapan

```bash
cd Pertemuan-10-Python-API-REST/praktikum/rest-api
python -m venv .venv
python -m pip install -r requirements.txt
```

Aktifkan `.venv` sesuai OS, lalu verifikasi:

```bash
python -c "import flask, requests; print('dependency OK')"
```

---

# A. Anatomy HTTP

Amati contoh request:

```text
POST /api/products?source=lab
Content-Type: application/json

{"name":"Monitor","price":1500000,"stock":4}
```

Isi tabel:

| Bagian | Nilai |
|---|---|
| Method | |
| Path | |
| Query parameter | |
| Content-Type | |
| Body | |

Jelaskan perbedaan query parameter dan JSON body.

---

# B. Jalankan Server

Terminal A:

```bash
python app.py
```

Uji:

```text
GET /api/health
GET /api/products
```

Catat status code, Content-Type, dan ringkasan body.

---

# C. GET Collection dan Detail

Uji:

```bash
curl -i http://127.0.0.1:5000/api/products
curl -i http://127.0.0.1:5000/api/products/1
curl -i http://127.0.0.1:5000/api/products/9999
```

| Skenario | Expected | Actual | Pass? |
|---|---:|---:|:---:|
| collection | 200 | | |
| detail ada | 200 | | |
| detail tidak ada | 404 | | |

---

# D. POST JSON

Request valid:

```bash
curl -i -X POST http://127.0.0.1:5000/api/products -H "Content-Type: application/json" -d '{"name":"Monitor","price":1500000,"stock":4}'
```

Uji minimal:

| ID | Skenario | Expected |
|---|---|---|
| D01 | body valid | 201 |
| D02 | body kosong | validation error |
| D03 | nama kosong | ditolak |
| D04 | harga negatif | ditolak |
| D05 | stok negatif | ditolak |
| D06 | stok bukan integer | ditolak |
| D07 | nama duplikat | conflict bila aturan aktif |
| D08 | body bukan JSON | ditolak |

Catat body dan status code.

---

# E. PATCH

```bash
curl -i -X PATCH http://127.0.0.1:5000/api/products/1 -H "Content-Type: application/json" -d '{"stock":12}'
```

Uji:

1. satu field valid;
2. boundary `stock=0`;
3. `stock=-1`;
4. field tidak dikenal;
5. ID tidak ditemukan.

---

# F. DELETE

```bash
curl -i -X DELETE http://127.0.0.1:5000/api/products/1
```

Setelah DELETE, lakukan GET detail ID yang sama. Jelaskan mengapa hasil berikutnya seharusnya not found.

---

# G. Search dan Query Parameter

Jika endpoint mendukung `q`, uji:

```bash
curl -i "http://127.0.0.1:5000/api/products?q=key"
curl -i "http://127.0.0.1:5000/api/products?q=tidakada"
```

Jelaskan perbedaan `/api/products/1` dan `/api/products?q=1`.

---

# H. Client Python

Dengan server tetap hidup, Terminal B:

```bash
python client.py
```

Identifikasi:

- `requests.get()` atau method lain;
- `params=`;
- `timeout=`;
- `raise_for_status()`;
- `.json()`;
- exception handling.

Matikan server lalu jalankan client kembali. Catat error yang muncul dan cara program menanganinya.

---

# I. Status Code Drill

Isi code yang paling sesuai.

| Situasi | Code |
|---|---:|
| Resource berhasil dibuat | |
| Sukses tanpa body | |
| Input tidak valid | |
| Resource tidak ada | |
| Path ada tetapi method salah | |
| Konflik data duplikat | |
| Terlalu banyak request | |
| Exception server | |

---

# J. API Families

Lengkapi:

| Jenis | Ciri utama | Contoh kebutuhan |
|---|---|---|
| REST | | |
| SOAP | | |
| GraphQL | | |
| RPC/gRPC | | |
| WebSocket | | |
| SSE | | |
| Webhook | | |

Jelaskan perbedaan WebSocket, SSE, dan Webhook dengan satu kalimat masing-masing.

---

# K. Security Concept

Jelaskan secara konseptual perbedaan API key, Basic Auth, Bearer token/JWT, dan OAuth 2.0. Untuk laporan gunakan placeholder, jangan credential nyata.

Tuliskan tiga aturan keamanan praktikum:

1. ........................................
2. ........................................
3. ........................................

---

# L. CORS Mental Model

Skenario:

```text
Frontend browser : http://localhost:3000
API Flask        : http://localhost:5000
```

Jawab:

1. Mengapa origin berbeda?
2. Mengapa curl/Python bisa berhasil ketika browser terkena CORS?
3. Mengapa CORS tidak sama dengan server mati?

---

# M. Automated Test

```bash
python -m unittest -v test_api.py
```

Catat:

```text
Jumlah test:
Pass:
Fail/Error:
```

Pilih dua test dan jelaskan request, expected status, expected body/state, dan assertion.

Tambahkan minimal dua test untuk fitur modifikasi Anda.

---

# N. Debugging Lab

Reproduksi minimal tiga kondisi:

- detail ID tidak ada;
- method salah;
- server dimatikan lalu client dijalankan.

Untuk setiap kondisi:

```text
Gejala:
Method + URL:
Status/error:
Body/log relevan:
Layer masalah:
Root cause:
Perbaikan/penjelasan:
Retest:
```

---

# O. Challenge Mandiri

Pilih minimal dua:

1. Search `q`.
2. Filter `min_stock`.
3. Endpoint `/api/stats`.
4. Duplikat menghasilkan status conflict.
5. PATCH hanya menerima field tertentu.
6. Pagination sederhana.
7. Client menampilkan pesan ramah untuk not found.
8. Mock external API lokal.
9. Error contract dengan field error yang konsisten.
10. Dua automated test baru per fitur.

---

# P. Test Report Minimum 12 Kasus

| ID | Method | Endpoint | Skenario | Expected | Actual | Status |
|---|---|---|---|---|---|---|
| TC01 | GET | health | normal | 200 | | |
| TC02 | GET | collection | normal | 200 | | |
| TC03 | GET | detail | ada | 200 | | |
| TC04 | GET | detail | tidak ada | 404 | | |
| TC05 | POST | collection | valid | 201 | | |
| TC06 | POST | collection | nama kosong | 400 | | |
| TC07 | POST | collection | nilai negatif | 400 | | |
| TC08 | POST | collection | duplikat | conflict/aturan | | |
| TC09 | PATCH | detail | valid | 200 | | |
| TC10 | PATCH | detail | invalid | 400 | | |
| TC11 | DELETE | detail | valid | success | | |
| TC12 | method | route valid | method salah | 405 | | |

# Pertanyaan Analisis
1. Apa beda halaman HTML Pertemuan 09 dengan JSON API Pertemuan 10?
2. Mengapa status code bagian dari kontrak API?
3. Apa beda PUT dan PATCH?
4. Apa beda 400, 404, 409, dan 500?
5. Mengapa client perlu timeout?
6. Mengapa parsing JSON dapat gagal?
7. Mengapa error response perlu konsisten?
8. Bagaimana membuktikan PATCH tidak merusak field lain?

# Deliverable
- source API dan client;
- dokumentasi endpoint;
- curl examples;
- tabel minimal 12 test case;
- automated test lulus;
- satu laporan debugging;
- minimal dua challenge;
- link GitHub;
- video sesuai `TugasVideo.md`.
