# API Pertemuan 10

Base URL lokal: `http://127.0.0.1:5000/api`.

| Method | Path | Tujuan |
|---|---|---|
| GET | `/health` | Status service |
| GET | `/products` | Daftar data |
| GET | `/products?q=key` | Pencarian nama |
| GET | `/products/<id>` | Detail data |
| POST | `/products` | Menambah data |
| PATCH | `/products/<id>` | Memperbarui sebagian data |
| DELETE | `/products/<id>` | Mengeluarkan data dari collection |

Contoh POST:
```json
{"name":"Monitor","price":1500000,"stock":3}
```

Contoh PATCH:
```json
{"stock":0}
```

Response error menggunakan object `error` yang berisi `code`, `message`, dan `details` bila diperlukan. Uji status 200, 201, 204, 400, 404, 405, dan 409 sesuai skenario pada Jobsheet.
