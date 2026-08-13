from flask import Flask, jsonify, request

app = Flask(__name__)

INITIAL_PRODUCTS = [
    {"id": 1, "name": "Keyboard", "price": 250000.0, "stock": 10},
    {"id": 2, "name": "Mouse", "price": 120000.0, "stock": 6},
]
products = [item.copy() for item in INITIAL_PRODUCTS]
ALLOWED_FIELDS = {"name", "price", "stock"}


def reset_products():
    products.clear()
    products.extend(item.copy() for item in INITIAL_PRODUCTS)


def error(code, message, status, details=None):
    body = {"error": {"code": code, "message": message}}
    if details:
        body["error"]["details"] = details
    return jsonify(body), status


def find_product(product_id):
    return next((item for item in products if item["id"] == product_id), None)


def validate(payload, partial=False):
    errors = {}
    if not isinstance(payload, dict):
        return {"_schema": "JSON harus berupa object"}
    unknown = sorted(set(payload) - ALLOWED_FIELDS)
    if unknown:
        errors["_schema"] = "field tidak dikenal: " + ", ".join(unknown)
    if partial and not payload:
        errors["_schema"] = "minimal satu field harus dikirim"
    if not partial or "name" in payload:
        if not str(payload.get("name", "")).strip():
            errors["name"] = "wajib diisi"
    if "price" in payload:
        try:
            value = float(payload["price"])
            if value < 0:
                raise ValueError
        except (TypeError, ValueError):
            errors["price"] = "harus angka >= 0"
    if "stock" in payload:
        try:
            value = int(payload["stock"])
            if value < 0 or str(value) != str(payload["stock"]).strip():
                raise ValueError
        except (TypeError, ValueError):
            errors["stock"] = "harus bilangan bulat >= 0"
    return errors


def duplicate_name(name, ignore_id=None):
    normalized = name.strip().lower()
    return any(item["name"].lower() == normalized and item["id"] != ignore_id for item in products)


@app.get("/api/health")
def health():
    return jsonify({"status": "ok"})


@app.get("/api/products")
def list_products():
    q = request.args.get("q", "").strip()
    data = products if not q else [item for item in products if q.lower() in item["name"].lower()]
    return jsonify({"data": data, "count": len(data), "query": q})


@app.get("/api/products/<int:product_id>")
def get_product(product_id):
    item = find_product(product_id)
    return jsonify(item) if item else error("NOT_FOUND", "Produk tidak ditemukan", 404)


@app.post("/api/products")
def create_product():
    payload = request.get_json(silent=True)
    if payload is None:
        return error("INVALID_JSON", "Body harus JSON", 400)
    errors = validate(payload)
    if errors:
        return error("VALIDATION_ERROR", "Payload tidak valid", 400, errors)
    name = payload["name"].strip()
    if duplicate_name(name):
        return error("DUPLICATE", "Nama produk sudah ada", 409)
    item = {
        "id": max((p["id"] for p in products), default=0) + 1,
        "name": name,
        "price": float(payload.get("price", 0)),
        "stock": int(payload.get("stock", 0)),
    }
    products.append(item)
    return jsonify(item), 201


@app.patch("/api/products/<int:product_id>")
def update_product(product_id):
    item = find_product(product_id)
    if item is None:
        return error("NOT_FOUND", "Produk tidak ditemukan", 404)
    payload = request.get_json(silent=True)
    if payload is None:
        return error("INVALID_JSON", "Body harus JSON", 400)
    errors = validate(payload, partial=True)
    if errors:
        return error("VALIDATION_ERROR", "Payload tidak valid", 400, errors)
    if "name" in payload:
        name = payload["name"].strip()
        if duplicate_name(name, ignore_id=product_id):
            return error("DUPLICATE", "Nama produk sudah ada", 409)
        item["name"] = name
    if "price" in payload:
        item["price"] = float(payload["price"])
    if "stock" in payload:
        item["stock"] = int(payload["stock"])
    return jsonify(item)


@app.delete("/api/products/<int:product_id>")
def delete_product(product_id):
    item = find_product(product_id)
    if item is None:
        return error("NOT_FOUND", "Produk tidak ditemukan", 404)
    products.remove(item)
    return "", 204


if __name__ == "__main__":
    app.run(debug=True)
