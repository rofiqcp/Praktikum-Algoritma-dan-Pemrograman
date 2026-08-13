from flask import Flask,jsonify,request

app=Flask(__name__)
products=[{"id":1,"name":"Keyboard","price":250000.0,"stock":10},{"id":2,"name":"Mouse","price":120000.0,"stock":6}]

def error(code,message,status,details=None):
    body={"error":{"code":code,"message":message}}
    if details is not None: body["error"]["details"]=details
    return jsonify(body),status

def find_product(pid): return next((p for p in products if p["id"]==pid),None)

def validate(payload,partial=False):
    errors={}
    if not partial or "name" in payload:
        name=str(payload.get("name","")).strip()
        if not name: errors["name"]="wajib diisi"
    if "price" in payload:
        try:
            if float(payload["price"])<0: raise ValueError
        except (TypeError,ValueError): errors["price"]="harus angka >= 0"
    if "stock" in payload:
        try:
            if int(payload["stock"])<0: raise ValueError
        except (TypeError,ValueError): errors["stock"]="harus integer >= 0"
    return errors

@app.get("/api/health")
def health(): return jsonify({"status":"ok"})

@app.get("/api/products")
def list_products(): return jsonify({"data":products,"count":len(products)})

@app.get("/api/products/<int:pid>")
def get_product(pid):
    p=find_product(pid); return jsonify(p) if p else error("NOT_FOUND","Produk tidak ditemukan",404)

@app.post("/api/products")
def create_product():
    payload=request.get_json(silent=True) or {}; errors=validate(payload)
    if errors: return error("VALIDATION_ERROR","Payload tidak valid",400,errors)
    name=payload["name"].strip()
    if any(p["name"].lower()==name.lower() for p in products): return error("DUPLICATE","Nama produk sudah ada",409)
    item={"id":max((p["id"] for p in products),default=0)+1,"name":name,"price":float(payload.get("price",0)),"stock":int(payload.get("stock",0))}; products.append(item)
    return jsonify(item),201

@app.patch("/api/products/<int:pid>")
def update_product(pid):
    p=find_product(pid)
    if not p: return error("NOT_FOUND","Produk tidak ditemukan",404)
    payload=request.get_json(silent=True) or {}; errors=validate(payload,partial=True)
    if errors: return error("VALIDATION_ERROR","Payload tidak valid",400,errors)
    if "name" in payload: p["name"]=payload["name"].strip()
    if "price" in payload: p["price"]=float(payload["price"])
    if "stock" in payload: p["stock"]=int(payload["stock"])
    return jsonify(p)

@app.delete("/api/products/<int:pid>")
def delete_product(pid):
    p=find_product(pid)
    if not p: return error("NOT_FOUND","Produk tidak ditemukan",404)
    products.remove(p); return "",204

if __name__=="__main__": app.run(debug=True)
