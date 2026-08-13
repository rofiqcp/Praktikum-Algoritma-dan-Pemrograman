from flask import Flask,jsonify,request
app=Flask(__name__)
products=[{'id':1,'name':'Keyboard','stock':10},{'id':2,'name':'Mouse','stock':8}]
def find(i): return next((p for p in products if p['id']==i),None)
@app.get('/api/products')
def all_products(): return jsonify({'data':products})
@app.get('/api/products/<int:i>')
def one(i):
    p=find(i); return (jsonify(p),200) if p else (jsonify({'error':'not_found'}),404)
@app.post('/api/products')
def create():
    b=request.get_json(silent=True) or {}; name=str(b.get('name','')).strip(); stock=b.get('stock',0)
    if not name or not isinstance(stock,int) or stock<0: return jsonify({'error':'invalid_input'}),400
    p={'id':max([x['id'] for x in products],default=0)+1,'name':name,'stock':stock}; products.append(p); return jsonify(p),201
@app.patch('/api/products/<int:i>')
def patch(i):
    p=find(i)
    if not p: return jsonify({'error':'not_found'}),404
    b=request.get_json(silent=True) or {}
    if 'stock' in b and (not isinstance(b['stock'],int) or b['stock']<0): return jsonify({'error':'invalid_stock'}),400
    if 'name' in b: p['name']=str(b['name']).strip()
    if 'stock' in b: p['stock']=b['stock']
    return jsonify(p)
@app.delete('/api/products/<int:i>')
def delete(i):
    p=find(i)
    if not p: return jsonify({'error':'not_found'}),404
    products.remove(p); return '',204
if __name__=='__main__': app.run(debug=True)
