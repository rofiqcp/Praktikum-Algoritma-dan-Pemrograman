# API Contract

Base: `http://127.0.0.1:5001/api`

| Method | Path | Success | Error |
|---|---|---:|---|
| GET | `/health` | 200 | - |
| GET | `/categories` | 200 | - |
| GET | `/products?q=&category_id=` | 200 | 400 bila filter invalid |
| GET | `/products/<id>` | 200 | 404 |
| POST | `/products` | 201 | 400,409 |
| PATCH | `/products/<id>` | 200 | 400,404,409 |
| DELETE | `/products/<id>` | 204 | 404 |

Error contract:
```json
{"error":{"code":"VALIDATION_ERROR","message":"Payload tidak valid","details":{"stock":"harus >= 0"}}}
```
