import sqlite3
from flask import Flask,jsonify,request
from flask_cors import CORS
from db import connect,init_db,rows,row

app=Flask(__name__); CORS(app,resources={r"/api/*":{"origins":["http://127.0.0.1:3000","http://localhost:3000"]}}); init_db()

def err(code,msg,status,details=None):
    body={"error":{"code":code,"message":msg}}
    if details: body["error"]["details"]=details
    return jsonify(body),status

def validate(p,partial=False):
    e={}
    if not partial or "name" in p:
        if not str(p.get("name","")).strip(): e["name"]="wajib diisi"
    for key,cast in [("price",float),("stock",int)]:
        if key in p:
            try:
                if cast(p[key])<0: raise ValueError
            except (ValueError,TypeError): e[key]="harus >= 0"
    return e

@app.get("/api/health")
def health(): return jsonify({"status":"ok"})
@app.get("/api/products")
def list_products(): return jsonify({"data":rows("SELECT id,name,price,stock FROM products ORDER BY id")})
@app.get("/api/products/<int:pid>")
def detail(pid):
    p=row("SELECT id,name,price,stock FROM products WHERE id=?",(pid,)); return jsonify(p) if p else err("NOT_FOUND","Produk tidak ditemukan",404)
@app.post("/api/products")
def create():
    p=request.get_json(silent=True) or {}; e=validate(p)
    if e:return err("VALIDATION_ERROR","Payload tidak valid",400,e)
    try:
        with connect() as c:
            cur=c.execute("INSERT INTO products(name,price,stock) VALUES(?,?,?)",(p["name"].strip(),float(p.get("price",0)),int(p.get("stock",0))))
            pid=cur.lastrowid
    except sqlite3.IntegrityError:return err("CONFLICT","Nama duplikat atau constraint gagal",409)
    return jsonify(row("SELECT * FROM products WHERE id=?",(pid,))),201
@app.patch("/api/products/<int:pid>")
def update(pid):
    current=row("SELECT * FROM products WHERE id=?",(pid,))
    if not current:return err("NOT_FOUND","Produk tidak ditemukan",404)
    p=request.get_json(silent=True) or {}; e=validate(p,True)
    if e:return err("VALIDATION_ERROR","Payload tidak valid",400,e)
    name=str(p.get("name",current["name"])).strip(); price=float(p.get("price",current["price"])); stock=int(p.get("stock",current["stock"]))
    try:
        with connect() as c:c.execute("UPDATE products SET name=?,price=?,stock=? WHERE id=?",(name,price,stock,pid))
    except sqlite3.IntegrityError:return err("CONFLICT","Constraint database gagal",409)
    return jsonify(row("SELECT * FROM products WHERE id=?",(pid,)))
@app.delete("/api/products/<int:pid>")
def delete(pid):
    if not row("SELECT id FROM products WHERE id=?",(pid,)):return err("NOT_FOUND","Produk tidak ditemukan",404)
    with connect() as c:c.execute("DELETE FROM products WHERE id=?",(pid,))
    return "",204

if __name__=="__main__": app.run(port=5001,debug=True)
