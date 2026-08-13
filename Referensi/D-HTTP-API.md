> Diadaptasi langsung dari lampiran/panduan pada buku sumber Edisi Agustus 2026.

# Lampiran D — HTTP dan API Cheat Sheet

| Method | Tujuan umum | Body |
|---|---|---|
| GET | Read | Biasanya tidak |
| POST | Create/command | Ya |
| PUT | Replace | Ya |
| PATCH | Partial update | Ya |
| DELETE | Delete | Biasanya tidak |

| Code | Arti singkat |
|---:|---|
| 200 | OK |
| 201 | Created |
| 204 | No Content |
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 409 | Conflict |
| 422 | Validation error |
| 429 | Rate limited |
| 500 | Server error |

```bash
curl -i http://localhost:8000/api/products
curl -i -X POST http://localhost:8000/api/products \
  -H "Content-Type: application/json" \
  -d '{"name":"Keyboard","stock":3}'
```
