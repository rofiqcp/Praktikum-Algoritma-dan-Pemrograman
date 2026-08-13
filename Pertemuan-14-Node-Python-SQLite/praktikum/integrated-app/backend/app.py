import math
import sqlite3
from flask import Flask, jsonify, request
from flask_cors import CORS
import db

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": ["http://127.0.0.1:3000", "http://localhost:3000"]}})
db.init_db()
ALLOWED_FIELDS = {"name", "price", "stock"}


def err(code, message, status, details=None):
    body = {"error": {"code": code, "message": message}}
    if details:
        body["error"]["details"] = details
    return jsonify(body), status


def parse_json_object():
    payload = request.get_json(silent=True)
    if not isinstance(payload, dict):
        return None, err("INVALID_JSON", "Body harus JSON object", 400)
    return payload, None


def exact_int(value):
    if isinstance(value, bool):
        raise ValueError
    if isinstance(value, int):
        return value
    if isinstance(value, float):
        if not value.is_integer():
            raise ValueError
        return int(value)
    text = str(value).strip()
    if not text or text.lstrip("+-").isdigit() is False:
        raise ValueError
    return int(text)


def nonnegative_number(value):
    if isinstance(value, bool):
        raise ValueError
    number = float(value)
    if not math.isfinite(number) or number < 0:
        raise ValueError
    return number


def validate(payload, partial=False):
    errors = {}
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
            nonnegative_number(payload["price"])
        except (TypeError, ValueError, OverflowError):
            errors["price"] = "harus angka >= 0"
    if "stock" in payload:
        try:
            if exact_int(payload["stock"]) < 0:
                raise ValueError
        except (TypeError, ValueError, OverflowError):
            errors["stock"] = "harus bilangan bulat >= 0"
    return errors


@app.get("/api/health")
def health():
    return jsonify({"status": "ok"})


@app.get("/api/products")
def list_products():
    return jsonify({"data": db.rows("SELECT id,name,price,stock FROM products ORDER BY id")})


@app.get("/api/products/<int:pid>")
def detail(pid):
    product = db.row("SELECT id,name,price,stock FROM products WHERE id=?", (pid,))
    return jsonify(product) if product else err("NOT_FOUND", "Produk tidak ditemukan", 404)


@app.post("/api/products")
def create():
    payload, response = parse_json_object()
    if response:
        return response
    errors = validate(payload)
    if errors:
        return err("VALIDATION_ERROR", "Payload tidak valid", 400, errors)
    try:
        with db.connect() as conn:
            cur = conn.execute(
                "INSERT INTO products(name,price,stock) VALUES(?,?,?)",
                (payload["name"].strip(), nonnegative_number(payload.get("price", 0)), exact_int(payload.get("stock", 0))),
            )
            pid = cur.lastrowid
    except sqlite3.IntegrityError:
        return err("CONFLICT", "Nama duplikat atau constraint gagal", 409)
    return jsonify(db.row("SELECT * FROM products WHERE id=?", (pid,))), 201


@app.patch("/api/products/<int:pid>")
def update(pid):
    current = db.row("SELECT * FROM products WHERE id=?", (pid,))
    if not current:
        return err("NOT_FOUND", "Produk tidak ditemukan", 404)
    payload, response = parse_json_object()
    if response:
        return response
    errors = validate(payload, True)
    if errors:
        return err("VALIDATION_ERROR", "Payload tidak valid", 400, errors)
    name = str(payload.get("name", current["name"])).strip()
    price = nonnegative_number(payload.get("price", current["price"]))
    stock = exact_int(payload.get("stock", current["stock"]))
    try:
        with db.connect() as conn:
            conn.execute("UPDATE products SET name=?,price=?,stock=? WHERE id=?", (name, price, stock, pid))
    except sqlite3.IntegrityError:
        return err("CONFLICT", "Constraint database gagal", 409)
    return jsonify(db.row("SELECT * FROM products WHERE id=?", (pid,)))


@app.delete("/api/products/<int:pid>")
def delete(pid):
    if not db.row("SELECT id FROM products WHERE id=?", (pid,)):
        return err("NOT_FOUND", "Produk tidak ditemukan", 404)
    with db.connect() as conn:
        conn.execute("DELETE FROM products WHERE id=?", (pid,))
    return "", 204


if __name__ == "__main__":
    app.run(port=5001, debug=True)
