# Dokumentasi Endpoint

Base URL lokal: `http://127.0.0.1:5000/api`

| Method | Path | Sukses | Error utama |
|---|---|---:|---|
| GET | `/health` | 200 | - |
| GET | `/products` | 200 | - |
| GET | `/products/<id>` | 200 | 404 |
| POST | `/products` | 201 | 400,409 |
| PATCH | `/products/<id>` | 200 | 400,404 |
| DELETE | `/products/<id>` | 204 | 404 |

## Error Contract
```json
{"error":{"code":"VALIDATION_ERROR","message":"Payload tidak valid","details":{"stock":"harus integer >= 0"}}}
```
