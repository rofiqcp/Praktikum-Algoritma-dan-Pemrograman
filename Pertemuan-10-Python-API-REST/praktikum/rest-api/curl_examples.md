# Curl Examples

```bash
curl http://127.0.0.1:5000/api/health
curl http://127.0.0.1:5000/api/products
curl -i http://127.0.0.1:5000/api/products/999
curl -i -X POST http://127.0.0.1:5000/api/products -H "Content-Type: application/json" -d '{"name":"Monitor","price":1500000,"stock":3}'
curl -i -X PATCH http://127.0.0.1:5000/api/products/1 -H "Content-Type: application/json" -d '{"stock":8}'
curl -i -X DELETE http://127.0.0.1:5000/api/products/2
```
