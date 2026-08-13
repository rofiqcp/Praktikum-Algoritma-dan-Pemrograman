import math
import os
import sqlite3
from flask import Flask, jsonify, request
from flask_cors import CORS
import db

app = Flask(__name__)
origins = [x.strip() for x in os.getenv('CORS_ORIGINS', 'http://127.0.0.1:3000,http://localhost:3000').split(',') if x.strip()]
CORS(app, resources={r"/api/*": {"origins": origins}})
db.init_db()
PRODUCT_FIELDS = {'name', 'category_id', 'price', 'stock'}


def err(code, message, status, details=None):
    body = {'error': {'code': code, 'message': message}}
    if details:
        body['error']['details'] = details
    return jsonify(body), status


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
    if not text or not text.lstrip('+-').isdigit():
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
    if not isinstance(payload, dict):
        return {'_schema': 'JSON harus berupa object'}
    errors = {}
    unknown = sorted(set(payload) - PRODUCT_FIELDS)
    if unknown:
        errors['_schema'] = 'field tidak dikenal: ' + ', '.join(unknown)
    if partial and not payload:
        errors['_schema'] = 'minimal satu field harus dikirim'
    if not partial or 'name' in payload:
        if not str(payload.get('name', '')).strip():
            errors['name'] = 'wajib diisi'
    if not partial or 'category_id' in payload:
        try:
            if exact_int(payload.get('category_id', 0)) <= 0:
                raise ValueError
        except (TypeError, ValueError, OverflowError):
            errors['category_id'] = 'harus integer > 0'
    if not partial or 'price' in payload:
        try:
            nonnegative_number(payload.get('price', 0))
        except (TypeError, ValueError, OverflowError):
            errors['price'] = 'harus angka >= 0'
    if not partial or 'stock' in payload:
        try:
            if exact_int(payload.get('stock', 0)) < 0:
                raise ValueError
        except (TypeError, ValueError, OverflowError):
            errors['stock'] = 'harus bilangan bulat >= 0'
    return errors


def parse_json_object():
    payload = request.get_json(silent=True)
    if not isinstance(payload, dict):
        return None, err('INVALID_JSON', 'Body harus JSON object', 400)
    return payload, None


def category_exists(category_id):
    return db.one('SELECT id FROM categories WHERE id=?', (category_id,)) is not None


def get_product(product_id):
    return db.one('''SELECT p.id,p.name,p.price,p.stock,p.category_id,c.name category_name
                     FROM products p JOIN categories c ON c.id=p.category_id WHERE p.id=?''', (product_id,))


@app.get('/api/health')
def health():
    return jsonify({'status': 'ok'})


@app.get('/api/categories')
def categories():
    return jsonify({'data': db.all_rows('SELECT id,name FROM categories ORDER BY name')})


@app.get('/api/products')
def products():
    q = request.args.get('q', '')
    raw_category = request.args.get('category_id')
    category_id = None
    if raw_category not in (None, ''):
        try:
            category_id = exact_int(raw_category)
            if category_id <= 0:
                raise ValueError
        except ValueError:
            return err('VALIDATION_ERROR', 'Filter tidak valid', 400, {'category_id': 'harus integer > 0'})
    sql = '''SELECT p.id,p.name,p.price,p.stock,p.category_id,c.name category_name
             FROM products p JOIN categories c ON c.id=p.category_id WHERE p.name LIKE ?'''
    args = [f'%{q}%']
    if category_id is not None:
        sql += ' AND p.category_id=?'
        args.append(category_id)
    sql += ' ORDER BY p.name'
    return jsonify({'data': db.all_rows(sql, args)})


@app.get('/api/products/<int:product_id>')
def detail(product_id):
    product = get_product(product_id)
    return jsonify(product) if product else err('NOT_FOUND', 'Produk tidak ditemukan', 404)


@app.post('/api/products')
def create():
    payload, response = parse_json_object()
    if response:
        return response
    errors = validate(payload)
    if errors:
        return err('VALIDATION_ERROR', 'Payload tidak valid', 400, errors)
    category_id = exact_int(payload['category_id'])
    if not category_exists(category_id):
        return err('INVALID_CATEGORY', 'Kategori tidak ditemukan', 400, {'category_id': 'not found'})
    try:
        with db.connect() as conn:
            cur = conn.execute(
                'INSERT INTO products(category_id,name,price,stock) VALUES(?,?,?,?)',
                (category_id, payload['name'].strip(), nonnegative_number(payload.get('price', 0)), exact_int(payload.get('stock', 0))),
            )
            product_id = cur.lastrowid
    except sqlite3.IntegrityError:
        return err('CONFLICT', 'Nama produk sudah ada atau constraint gagal', 409)
    return jsonify(get_product(product_id)), 201


@app.patch('/api/products/<int:product_id>')
def patch(product_id):
    current = get_product(product_id)
    if not current:
        return err('NOT_FOUND', 'Produk tidak ditemukan', 404)
    payload, response = parse_json_object()
    if response:
        return response
    errors = validate(payload, True)
    if errors:
        return err('VALIDATION_ERROR', 'Payload tidak valid', 400, errors)
    data = {**current, **payload}
    category_id = exact_int(data['category_id'])
    if not category_exists(category_id):
        return err('INVALID_CATEGORY', 'Kategori tidak ditemukan', 400, {'category_id': 'not found'})
    try:
        with db.connect() as conn:
            conn.execute(
                'UPDATE products SET category_id=?,name=?,price=?,stock=? WHERE id=?',
                (category_id, str(data['name']).strip(), nonnegative_number(data['price']), exact_int(data['stock']), product_id),
            )
    except sqlite3.IntegrityError:
        return err('CONFLICT', 'Constraint gagal', 409)
    return jsonify(get_product(product_id))


@app.delete('/api/products/<int:product_id>')
def delete(product_id):
    if not get_product(product_id):
        return err('NOT_FOUND', 'Produk tidak ditemukan', 404)
    with db.connect() as conn:
        conn.execute('DELETE FROM products WHERE id=?', (product_id,))
    return '', 204


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('API_PORT', '5001')), debug=os.getenv('FLASK_DEBUG') == '1')
