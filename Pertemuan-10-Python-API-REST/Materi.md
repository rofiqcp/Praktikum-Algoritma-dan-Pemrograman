# Materi Pertemuan 10 — Python API: HTTP, JSON, REST, Variasi API, dan Integrasi

> Sumber utama: *Buku Panduan Praktik: Scratch → Python → Web → API → Node.js → Full Stack*, Edisi Agustus 2026. Pertemuan ini melanjutkan mental model web dari Pertemuan 09, tetapi fokus berpindah dari response HTML menuju **data JSON dan komunikasi antarprogram**.

Sesi ini menjelaskan API mulai dari anatomy HTTP request/response, status code, JSON, REST CRUD, konsumsi API dengan Python `requests`, pembuatan REST API sederhana, variasi keluarga API, authentication secara konseptual, CORS, sampai troubleshooting berdasarkan bukti.

## Target Kompetensi
Setelah praktikum, mahasiswa mampu:

1. Menjelaskan anatomy HTTP request dan response.
2. Mengidentifikasi method, URL/path, query parameter, headers, body, status code, dan response body.
3. Menggunakan `GET`, `POST`, `PUT`, `PATCH`, dan `DELETE` sesuai tujuan operasi.
4. Membaca dan menghasilkan JSON.
5. Memetakan operasi CRUD ke endpoint REST sederhana.
6. Mengonsumsi API menggunakan Python `requests` dengan `params`, `timeout`, dan error handling.
7. Membuat REST API Python sederhana menggunakan Flask.
8. Menghasilkan status code yang sesuai untuk sukses, validation error, not found, dan conflict.
9. Mengenal REST, SOAP, GraphQL, RPC/gRPC, WebSocket, SSE, dan Webhook.
10. Mengenal API key, Basic Auth, Bearer token/JWT, dan OAuth 2.0 secara konseptual.
11. Menjelaskan CORS secara intuitif dan membedakan masalah browser dengan masalah API/network umum.
12. Menguji API dengan browser, curl/Postman sejenis, Python `requests`, dan automated test.
13. Mendiagnosis 400/401/403/404/405/409/422/429/500/502/503, invalid JSON, timeout, dan connection refused berdasarkan bukti.

## Output Pertemuan
- satu client Python yang memanggil API;
- satu REST API Python sederhana;
- dokumentasi endpoint;
- contoh request/response JSON;
- curl examples;
- minimal 10 test case;
- automated test;
- catatan troubleshooting;
- video sesuai `TugasVideo.md`.

## Alur Pengajaran 180 Menit
| Tahap | Durasi | Aktivitas |
|---|---:|---|
| HTTP mental model | 30 | Request/response, URL, headers, body |
| REST & methods | 30 | CRUD mapping dan status codes |
| Consume API | 30 | `requests`, params, timeout, errors |
| Create API | 40 | Flask JSON endpoints |
| API families | 25 | REST, SOAP, GraphQL, RPC/gRPC, WebSocket, SSE, Webhook |
| Auth & CORS | 15 | Konsep credential, token, origin |
| Troubleshooting | 10 | Diagnosis network/log based |

---

# 10.1 Apa Itu API?

API adalah antarmuka komunikasi antarperangkat lunak. Pada konteks web API:

```text
CLIENT
  │
  │ HTTP Request
  ▼
API ENDPOINT
  │
  ▼
BACKEND LOGIC
  │
  ▼
JSON + STATUS CODE
  │
  ▼
CLIENT
```

Client tidak harus browser. Client bisa berupa:

- Python script;
- JavaScript frontend;
- mobile app;
- service backend lain;
- curl/Postman;
- automated test.

Ini menjelaskan mengapa API berbeda dengan halaman web HTML. Halaman web terutama ditujukan untuk manusia melalui browser; API terutama ditujukan untuk program lain melalui kontrak request/response.

---

# 10.2 Anatomy HTTP Request

Contoh:

```http
GET /api/products?page=2&q=keyboard HTTP/1.1
Host: example.com
Accept: application/json
Authorization: Bearer <TOKEN>
```

Lima bagian request yang wajib dikenali:

1. **Method** — tindakan yang diminta.
2. **URL/path** — resource/endpoint yang dituju.
3. **Query parameter** — parameter setelah `?`, misalnya `page=2`.
4. **Headers** — metadata request seperti `Accept`, `Content-Type`, `Authorization`.
5. **Body** — data yang dikirim, umum pada POST/PATCH/PUT.

Contoh request dengan JSON body:

```http
POST /api/products HTTP/1.1
Content-Type: application/json

{
  "name": "Monitor",
  "price": 1500000,
  "stock": 4
}
```

---

# 10.3 Anatomy HTTP Response

Contoh sukses:

```http
HTTP/1.1 201 Created
Content-Type: application/json

{
  "id": 3,
  "name": "Monitor",
  "price": 1500000,
  "stock": 4
}
```

Tiga bagian yang paling penting untuk praktikum:

- status code;
- response headers;
- response body.

Jangan menilai keberhasilan hanya dari body. Response JSON yang terlihat “benar” tetapi status `500` tetap menunjukkan kegagalan server.

---

# 10.4 HTTP Methods dan CRUD

| Tujuan | CRUD | Method umum | Contoh endpoint |
|---|---|---|---|
| daftar produk | Read | GET | `/api/products` |
| detail produk | Read | GET | `/api/products/12` |
| tambah produk | Create | POST | `/api/products` |
| ganti seluruh representasi | Update | PUT | `/api/products/12` |
| ubah sebagian field | Update | PATCH | `/api/products/12` |
| hapus produk | Delete | DELETE | `/api/products/12` |

Implementasi nyata dapat berbeda. Dokumentasi API tetap menjadi sumber kontrak utama.

## PUT vs PATCH
Secara mental model:

- **PUT**: mengganti representasi resource secara penuh.
- **PATCH**: mengubah sebagian field.

Dalam praktik framework tertentu, aturan detail dapat berbeda sesuai dokumentasi dan desain API.

---

# 10.5 Status Code Penting

| Kelompok | Code | Makna praktis |
|---|---:|---|
| 2xx | 200 OK | request sukses dan ada response |
| 2xx | 201 Created | resource baru berhasil dibuat |
| 2xx | 204 No Content | sukses tanpa response body |
| 4xx | 400 Bad Request | request/input tidak valid |
| 4xx | 401 Unauthorized | belum/tidak terautentikasi |
| 4xx | 403 Forbidden | sudah dikenali tetapi tidak diizinkan |
| 4xx | 404 Not Found | route/resource tidak ditemukan |
| 4xx | 405 Method Not Allowed | path ada tetapi method tidak diterima |
| 4xx | 409 Conflict | konflik state, misalnya data duplikat |
| 4xx | 422 Unprocessable Content | struktur/validasi data gagal pada framework tertentu |
| 4xx | 429 Too Many Requests | rate limit |
| 5xx | 500 Internal Server Error | exception/bug server |
| 5xx | 502/503 | gateway/service tidak tersedia |

## Prinsip penting
Status code adalah bagian dari kontrak API. Hindari pola:

```json
{"success": false, "error": "not found"}
```

dengan HTTP `200` untuk semua kondisi. Client menjadi lebih sulit membedakan keberhasilan dan kegagalan.

---

# 10.6 JSON

JSON menyimpan data sebagai object, array, string, number, boolean, dan `null`.

Contoh object:

```json
{
  "id": 1,
  "name": "Keyboard",
  "stock": 10,
  "active": true
}
```

Contoh response collection:

```json
{
  "data": [
    {"id": 1, "name": "Keyboard", "stock": 10},
    {"id": 2, "name": "Mouse", "stock": 6}
  ],
  "count": 2
}
```

Python dictionary mirip JSON object, tetapi bukan hal yang sama. JSON adalah format teks pertukaran data; dictionary adalah object Python di memory.

---

# 10.7 Query Parameter

Contoh:

```text
GET /api/products?q=key&min_stock=1
```

Flask:

```python
q = request.args.get("q", "").strip().lower()
min_stock = request.args.get("min_stock", type=int)
```

Query parameter cocok untuk filter, search, pagination, sorting, dan pilihan request yang tidak mengubah resource.

---

# 10.8 Mengonsumsi API dengan Python Requests

```python
import requests

url = "https://example.com/api/items"

try:
    response = requests.get(
        url,
        params={"page": 1},
        timeout=10,
    )
    response.raise_for_status()
    data = response.json()
    print(data)
except requests.Timeout:
    print("Request timeout")
except requests.HTTPError as error:
    print("HTTP error:", error)
except requests.RequestException as error:
    print("Network error:", error)
```

## Mengapa `timeout` penting?
Tanpa timeout, program dapat menunggu terlalu lama ketika dependency/network bermasalah. Timeout bukan jaminan semua masalah selesai, tetapi memberi batas menunggu yang eksplisit.

## Jangan langsung memanggil `.json()` tanpa berpikir
Response error dapat berupa HTML/text. Saat parsing JSON gagal, cek:

```python
print(response.status_code)
print(response.headers.get("Content-Type"))
print(response.text[:300])
```

Jangan mencetak credential/token.

---

# 10.9 Membuat API Flask Sederhana

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

products = [
    {"id": 1, "name": "Keyboard", "stock": 10}
]

@app.get("/api/products")
def get_products():
    return jsonify({"data": products, "count": len(products)})

@app.post("/api/products")
def create_product():
    payload = request.get_json(silent=True) or {}
    name = str(payload.get("name", "")).strip()

    if not name:
        return jsonify({"error": "validation_error", "message": "name wajib diisi"}), 400

    item = {
        "id": max((p["id"] for p in products), default=0) + 1,
        "name": name,
        "stock": 0,
    }
    products.append(item)
    return jsonify(item), 201
```

---

# 10.10 Error Contract

Agar client mudah memproses error, gunakan bentuk yang konsisten.

Contoh:

```json
{
  "error": "validation_error",
  "message": "Input tidak valid",
  "fields": {
    "stock": "stock harus integer >= 0"
  }
}
```

Not found:

```json
{
  "error": "not_found",
  "message": "Produk tidak ditemukan"
}
```

Konsistensi lebih penting daripada membuat banyak variasi format error.

---

# 10.11 Validasi POST/PATCH

Server harus memeriksa:

- body benar-benar JSON bila endpoint mensyaratkan JSON;
- field wajib tersedia;
- tipe data dapat diproses;
- boundary benar;
- data duplikat bila aturan melarang;
- resource target ada sebelum PATCH/DELETE.

Contoh boundary:

```text
stock = 0   → valid
stock = -1  → invalid
price = 0   → valid jika aturan mengizinkan
name = ""   → invalid
```

---

# 10.12 REST API Example yang Lebih Lengkap

Project runnable pada `praktikum/rest-api/app.py` menyediakan pola:

```text
GET    /api/health
GET    /api/products
GET    /api/products/<id>
POST   /api/products
PATCH  /api/products/<id>
DELETE /api/products/<id>
```

Endpoint collection juga dapat mendukung filter/search sederhana.

---

# 10.13 Peta Variasi API

| Jenis | Pola komunikasi | Kapan dikenal/dipakai |
|---|---|---|
| REST | resource + HTTP methods; sering JSON | web/mobile API umum |
| SOAP | message XML dengan kontrak formal | enterprise/legacy tertentu |
| GraphQL | client meminta field melalui schema | data graph/endpoint fleksibel |
| RPC | client memanggil prosedur/fungsi remote | service-oriented |
| gRPC | RPC berbasis schema/protobuf dan HTTP/2 | service-to-service performa tinggi |
| WebSocket | koneksi dua arah persisten | chat, game, telemetry realtime |
| SSE | server streaming event satu arah | notifikasi/stream update ke browser |
| Webhook | server melakukan callback HTTP saat event | integrasi event, pembayaran, CI |

Tujuan pertemuan ini **mengenal mental model**, bukan mengimplementasikan semua jenis API.

---

# 10.14 Authentication/API Security Dasar

| Mekanisme | Gagasan | Catatan belajar |
|---|---|---|
| API Key | identifier rahasia pada header/query | jangan hard-code/push ke repo |
| Basic Auth | username/password mengikuti skema HTTP | gunakan HTTPS pada dunia nyata |
| Bearer Token | token di `Authorization` header | perlakukan seperti password |
| JWT | token berisi claims dan signature | tetap harus diverifikasi |
| OAuth 2.0 | delegasi akses tanpa membagikan password aplikasi | kenali flow; tidak perlu membuat provider sendiri |

Contoh header konseptual:

```http
Authorization: Bearer <TOKEN>
```

Jangan memasukkan token nyata ke dokumentasi, screenshot, log, video, atau repository publik.

---

# 10.15 CORS secara Intuitif

CORS berkaitan dengan kebijakan **browser** ketika frontend mencoba membaca resource dari origin berbeda.

Misalnya:

```text
Frontend : http://localhost:3000
API      : http://localhost:5000
```

Origin berbeda karena kombinasi scheme/host/port berbeda.

Hal penting:

- curl dapat berhasil sementara browser terkena CORS;
- Python `requests` dapat berhasil sementara browser terkena CORS;
- karena itu jangan menyimpulkan “API mati” hanya dari pesan CORS;
- konfigurasi CORS harus dibatasi sesuai kebutuhan, bukan selalu membuka semua origin tanpa alasan.

---

# 10.16 Testing API dengan curl

Health:

```bash
curl -i http://127.0.0.1:5000/api/health
```

Collection:

```bash
curl -i http://127.0.0.1:5000/api/products
```

POST JSON:

```bash
curl -i -X POST http://127.0.0.1:5000/api/products \
  -H "Content-Type: application/json" \
  -d '{"name":"Monitor","price":1500000,"stock":4}'
```

PATCH:

```bash
curl -i -X PATCH http://127.0.0.1:5000/api/products/1 \
  -H "Content-Type: application/json" \
  -d '{"stock":12}'
```

DELETE:

```bash
curl -i -X DELETE http://127.0.0.1:5000/api/products/1
```

Selalu baca **status line** dan body.

---

# 10.17 Testing dengan Flask Test Client

Automated test tidak memerlukan server network sungguhan.

```python
response = client.get("/api/products")
assert response.status_code == 200
assert response.get_json()["count"] >= 0
```

Test yang baik mencakup:

1. health 200;
2. GET collection;
3. GET detail valid;
4. detail not found 404;
5. POST valid 201;
6. POST body kosong 400;
7. POST nama kosong 400;
8. POST stock negatif 400;
9. duplikat 409 bila aturan berlaku;
10. PATCH valid;
11. PATCH invalid;
12. DELETE valid 204/200;
13. DELETE not found 404;
14. filter/search;
15. method salah 405.

---

# 10.18 Troubleshooting API Berdasarkan Bukti

| Gejala | Kemungkinan penyebab | Langkah pemeriksaan/perbaikan |
|---|---|---|
| Connection refused | server mati/host-port salah | cek process, URL, port |
| 404 | path/resource tidak ada | cek base URL, prefix, ID, route |
| 405 | method salah | bandingkan method dengan dokumentasi |
| 400/422 | payload tidak sesuai | cek Content-Type, JSON, field, tipe |
| 401/403 | credential/permission | cek authorization tanpa membocorkan secret |
| 409 | konflik state | cek duplikat/state resource |
| 429 | rate limit | baca header/dokumentasi, hindari retry agresif |
| 500 | exception server | baca backend traceback/log |
| 502/503 | service/gateway tidak tersedia | cek dependency/platform status/log |
| Invalid JSON | response bukan JSON/body rusak | cek Content-Type dan `response.text` |
| Timeout | server/network/dependency lambat | gunakan timeout, cek dependency |

## Prosedur diagnosis

```text
REPRODUCE
→ CATAT METHOD + URL + STATUS
→ LIHAT BODY/HEADER
→ TENTUKAN LAYER
→ BACA LOG BACKEND JIKA PERLU
→ PERUBAHAN MINIMAL
→ RETEST REQUEST GAGAL
→ REGRESSION TEST
```

---

# 10.19 Lab Client dan Server

Terminal A:

```bash
python app.py
```

Terminal B:

```bash
python client.py
```

Mahasiswa harus dapat menjelaskan:

```text
client.py
  ↓ requests
HTTP
  ↓
app.py
  ↓ jsonify
HTTP response
  ↓
client.py
```

---

# 10.20 Challenge Mandiri

Pilih minimal dua:

- tambahkan filter `q` pada collection;
- tambahkan `min_stock`;
- tambahkan validasi nama duplikat → 409;
- tambahkan PATCH hanya untuk field yang diizinkan;
- tambahkan endpoint `/api/stats`;
- tambahkan pagination sederhana;
- tambah client yang menunjukkan penanganan 404;
- tambah mock external API lokal untuk latihan timeout/error;
- tambah minimal dua automated test per fitur.

---

# 10.21 Checklist Selesai

- [ ] Dapat menjelaskan request dan response.
- [ ] Dapat membedakan method HTTP.
- [ ] Dapat membaca status code.
- [ ] Dapat membedakan JSON dan dictionary Python.
- [ ] API collection/detail berjalan.
- [ ] POST mempunyai server-side validation.
- [ ] PATCH/DELETE menangani not found.
- [ ] Error response konsisten.
- [ ] Client menggunakan timeout.
- [ ] curl examples diuji.
- [ ] Automated test lulus.
- [ ] Tidak ada credential nyata dalam repository.

## Exit Ticket
1. Apa perbedaan query parameter dan JSON body?
2. Kapan 201 digunakan?
3. Apa beda 401 dan 403?
4. Mengapa 404 berbeda dengan 405?
5. Mengapa API client sebaiknya menggunakan timeout?
6. Mengapa curl bisa berhasil tetapi browser tetap menampilkan CORS error?
7. Apa beda REST, WebSocket, dan Webhook secara mental model?
8. Jelaskan proses diagnosis ketika POST menghasilkan 400/422.

## Referensi Internal
- `Jobsheet.md`
- `TugasVideo.md`
- `praktikum/rest-api/app.py`
- `praktikum/rest-api/client.py`
- `praktikum/rest-api/API.md`
- `praktikum/rest-api/curl_examples.md`
- `praktikum/rest-api/test_api.py`
