import sqlite3,os
from flask import Flask,jsonify,request
from flask_cors import CORS
from db import connect,init_db,all_rows,one

app=Flask(__name__); CORS(app,resources={r"/api/*":{"origins":["http://127.0.0.1:3000","http://localhost:3000"]}}); init_db()

def err(code,msg,status,details=None):
    b={"error":{"code":code,"message":msg}}
    if details:b["error"]["details"]=details
    return jsonify(b),status

def validate(p,partial=False):
    e={}
    if not partial or 'name' in p:
        if not str(p.get('name','')).strip():e['name']='wajib diisi'
    if not partial or 'category_id' in p:
        try:
            if int(p.get('category_id',0))<=0:raise ValueError
        except (TypeError,ValueError):e['category_id']='harus integer > 0'
    for k,cast in [('price',float),('stock',int)]:
        if not partial or k in p:
            try:
                if cast(p.get(k,0))<0:raise ValueError
            except (TypeError,ValueError):e[k]='harus >= 0'
    return e

def category_exists(cid):return one('SELECT id FROM categories WHERE id=?',(cid,)) is not None
def get(pid):return one('''SELECT p.id,p.name,p.price,p.stock,p.category_id,c.name category_name FROM products p JOIN categories c ON c.id=p.category_id WHERE p.id=?''',(pid,))

@app.get('/api/health')
def health():return jsonify({'status':'ok'})
@app.get('/api/categories')
def categories():return jsonify({'data':all_rows('SELECT id,name FROM categories ORDER BY name')})
@app.get('/api/products')
def products():
    q=request.args.get('q','');cid=request.args.get('category_id',type=int);sql='''SELECT p.id,p.name,p.price,p.stock,p.category_id,c.name category_name FROM products p JOIN categories c ON c.id=p.category_id WHERE p.name LIKE ?''';args=[f'%{q}%']
    if cid is not None:sql+=' AND p.category_id=?';args.append(cid)
    sql+=' ORDER BY p.name';return jsonify({'data':all_rows(sql,args)})
@app.get('/api/products/<int:pid>')
def detail(pid):
    p=get(pid);return jsonify(p) if p else err('NOT_FOUND','Produk tidak ditemukan',404)
@app.post('/api/products')
def create():
    p=request.get_json(silent=True) or {};e=validate(p)
    if e:return err('VALIDATION_ERROR','Payload tidak valid',400,e)
    cid=int(p['category_id'])
    if not category_exists(cid):return err('INVALID_CATEGORY','Kategori tidak ditemukan',400,{'category_id':'not found'})
    try:
        with connect() as c:cur=c.execute('INSERT INTO products(category_id,name,price,stock) VALUES(?,?,?,?)',(cid,p['name'].strip(),float(p.get('price',0)),int(p.get('stock',0))));pid=cur.lastrowid
    except sqlite3.IntegrityError:return err('CONFLICT','Nama produk sudah ada/constraint gagal',409)
    return jsonify(get(pid)),201
@app.patch('/api/products/<int:pid>')
def patch(pid):
    current=get(pid)
    if not current:return err('NOT_FOUND','Produk tidak ditemukan',404)
    p=request.get_json(silent=True) or {};e=validate(p,True)
    if e:return err('VALIDATION_ERROR','Payload tidak valid',400,e)
    data={**current,**p};cid=int(data['category_id'])
    if not category_exists(cid):return err('INVALID_CATEGORY','Kategori tidak ditemukan',400)
    try:
        with connect() as c:c.execute('UPDATE products SET category_id=?,name=?,price=?,stock=? WHERE id=?',(cid,str(data['name']).strip(),float(data['price']),int(data['stock']),pid))
    except sqlite3.IntegrityError:return err('CONFLICT','Constraint gagal',409)
    return jsonify(get(pid))
@app.delete('/api/products/<int:pid>')
def delete(pid):
    if not get(pid):return err('NOT_FOUND','Produk tidak ditemukan',404)
    with connect() as c:c.execute('DELETE FROM products WHERE id=?',(pid,))
    return '',204

if __name__=='__main__':app.run(host='0.0.0.0',port=int(os.getenv('API_PORT','5001')),debug=os.getenv('FLASK_DEBUG')=='1')
