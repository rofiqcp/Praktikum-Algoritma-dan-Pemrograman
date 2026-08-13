# Materi Pertemuan 10 — Python API: HTTP, JSON, REST, Variasi API, dan Integrasi

> Sumber utama: *Buku Panduan Praktik: Pemrograman Dasar hingga Full Stack — 16 Pertemuan Terstruktur, Edisi Agustus 2026*.

Sesi ini menjelaskan API dari mental model sampai praktik mengonsumsi API eksternal dan membuat REST API Python sederhana.

## Target Kompetensi
- Menjelaskan anatomy HTTP request/response.
- Menggunakan GET, POST, PUT/PATCH, DELETE secara tepat.
- Membaca dan menghasilkan JSON.
- Mengenal REST, SOAP, GraphQL, RPC/gRPC, WebSocket, SSE, dan Webhook.
- Mengenal API key, Basic Auth, Bearer token/JWT, OAuth 2.0 secara konseptual.
- Menguji API dengan browser/curl/Postman dan Python `requests`.

## Output
- Satu client Python yang memanggil API.
- Satu REST API Python sederhana.
- Dokumentasi endpoint dan test cases.

## Alur 180 Menit
| Tahap | Durasi | Aktivitas |
|---|---:|---|
| HTTP mental model | 30 | Request/response, URL, headers, body |
| REST & methods | 30 | CRUD mapping dan status codes |
| Consume API | 30 | `requests`, params, timeout, errors |
| Create API | 40 | Flask/FastAPI JSON endpoints |
| API families | 25 | GraphQL, SOAP, gRPC, WebSocket, SSE, webhook |
| Auth & CORS | 15 | Konsep keamanan dan origin |
| Troubleshoot | 10 | Network/log based diagnosis |

## 10.1 Anatomy HTTP Request
```http
GET /api/products?page=2 HTTP/1.1
Host: example.com
Accept: application/json
Authorization: Bearer <TOKEN>
```
Kenali method, URL/path, query parameter, headers, dan body.

## 10.2 Status Code Penting
| Kelompok | Code | Makna praktis |
|---|---:|---|
| 2xx | 200 | OK |
| 2xx | 201 | Resource dibuat |
| 2xx | 204 | Sukses tanpa body |
| 4xx | 400 | Request/input tidak valid |
| 4xx | 401 | Belum/tidak terautentikasi |
| 4xx | 403 | Tidak diizinkan |
| 4xx | 404 | Resource/route tidak ada |
| 4xx | 409 | Conflict state/duplikat |
| 4xx | 422 | Struktur/validasi gagal pada framework tertentu |
| 4xx | 429 | Rate limit |
| 5xx | 500 | Bug/exception server |
| 5xx | 502/503 | Gateway/service tidak tersedia |

## 10.3 REST CRUD
| Tujuan | Method | Endpoint contoh |
|---|---|---|
| Daftar | GET | `/api/products` |
| Detail | GET | `/api/products/12` |
| Tambah | POST | `/api/products` |
| Ubah sebagian | PATCH | `/api/products/12` |
| Hapus | DELETE | `/api/products/12` |

## 10.4 Mengonsumsi API dengan Python
```python
import requests
try:
    response=requests.get(url,params={"page":1},timeout=10)
    response.raise_for_status()
    data=response.json()
except requests.Timeout:
    print("Request timeout")
except requests.HTTPError as e:
    print("HTTP error:",e)
except requests.RequestException as e:
    print("Network error:",e)
```

## 10.5 Membuat API Flask
Endpoint harus mengembalikan JSON, status code sesuai hasil, validation error yang stabil, dan tidak membocorkan traceback publik.

## 10.6 Peta Variasi API
| Jenis | Pola | Contoh penggunaan |
|---|---|---|
| REST | resource + HTTP methods | web/mobile API |
| SOAP | XML + kontrak formal | enterprise/legacy |
| GraphQL | client memilih field via schema | data graph |
| RPC | panggil prosedur remote | service-oriented |
| gRPC | protobuf + HTTP/2 | service-to-service |
| WebSocket | dua arah persisten | chat/game/telemetry |
| SSE | streaming satu arah server→browser | update event |
| Webhook | callback HTTP saat event | payment/CI/integration |

## 10.7 Authentication/API Security Dasar
- API key: jangan hard-code/push.
- Basic Auth: wajib HTTPS di dunia nyata.
- Bearer token/JWT: token diperlakukan seperti password; JWT tetap harus diverifikasi.
- OAuth 2.0: delegasi akses; cukup pahami flow pada level ini.

## 10.8 CORS Intuitif
CORS adalah kebijakan browser saat frontend membaca resource dari origin berbeda. Jika `curl`/Python berhasil tetapi browser gagal, periksa origin dan header CORS.

## 10.9 Troubleshooting API
| Gejala | Fokus pemeriksaan |
|---|---|
| Connection refused | server/host/port/firewall |
| 404 | path/prefix/routing |
| 405 | method |
| 401/403 | Authorization/scope |
| 400/422 | JSON/schema/type |
| 500 | backend log/traceback |
| Invalid JSON | Content-Type/body |
| Timeout | network/dependency/timeout/retry terbatas |
