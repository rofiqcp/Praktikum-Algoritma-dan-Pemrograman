import sqlite3
from pathlib import Path
from flask import Flask,jsonify,request
DB=Path(__file__).with_name('final.db');app=Flask(__name__)
def connect():
    c=sqlite3.connect(DB);c.row_factory=sqlite3.Row;c.execute('PRAGMA foreign_keys=ON');return c
def init_db():
    with connect() as c:
        c.executescript('CREATE TABLE IF NOT EXISTS categories(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL UNIQUE);CREATE TABLE IF NOT EXISTS products(id INTEGER PRIMARY KEY AUTOINCREMENT,category_id INTEGER NOT NULL,name TEXT NOT NULL,stock INTEGER NOT NULL CHECK(stock>=0),FOREIGN KEY(category_id) REFERENCES categories(id) ON DELETE RESTRICT);')
        c.execute("INSERT OR IGNORE INTO categories(id,name) VALUES(1,'Default')");c.commit()
@app.after_request
def cors(r):r.headers['Access-Control-Allow-Origin']='http://localhost:3000';r.headers['Access-Control-Allow-Headers']='Content-Type';r.headers['Access-Control-Allow-Methods']='GET,POST,PATCH,DELETE,OPTIONS';return r
@app.get('/health')
def health():return jsonify({'status':'ok'})
@app.get('/api/categories')
def categories():
    with connect() as c:rows=c.execute('SELECT id,name FROM categories ORDER BY name').fetchall()
    return jsonify({'data':[dict(x) for x in rows]})
@app.get('/api/products')
def products():
    with connect() as c:rows=c.execute('SELECT p.id,p.name,p.stock,p.category_id,c.name category_name FROM products p JOIN categories c ON c.id=p.category_id ORDER BY p.id').fetchall()
    return jsonify({'data':[dict(x) for x in rows]})
@app.post('/api/products')
def create():
    b=request.get_json(silent=True) or {};name=str(b.get('name','')).strip();cid=b.get('category_id');stock=b.get('stock')
    if not name or not isinstance(cid,int) or not isinstance(stock,int) or stock<0:return jsonify({'error':{'code':'INVALID_INPUT','message':'name/category_id/stock invalid'}}),400
    try:
        with connect() as c:cur=c.execute('INSERT INTO products(category_id,name,stock) VALUES(?,?,?)',(cid,name,stock));c.commit();i=cur.lastrowid
    except sqlite3.IntegrityError:return jsonify({'error':{'code':'INVALID_CATEGORY','message':'kategori tidak tersedia'}}),409
    return jsonify({'id':i,'name':name,'category_id':cid,'stock':stock}),201
@app.patch('/api/products/<int:i>')
def patch(i):
    b=request.get_json(silent=True) or {};stock=b.get('stock')
    if not isinstance(stock,int) or stock<0:return jsonify({'error':{'code':'INVALID_STOCK','message':'stock harus integer >=0'}}),400
    with connect() as c:cur=c.execute('UPDATE products SET stock=? WHERE id=?',(stock,i));c.commit()
    return (jsonify({'id':i,'stock':stock}),200) if cur.rowcount else (jsonify({'error':{'code':'NOT_FOUND'}}),404)
@app.delete('/api/products/<int:i>')
def delete(i):
    with connect() as c:cur=c.execute('DELETE FROM products WHERE id=?',(i,));c.commit()
    return ('',204) if cur.rowcount else (jsonify({'error':{'code':'NOT_FOUND'}}),404)
if __name__=='__main__':init_db();app.run(port=5000,debug=True)
