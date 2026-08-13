from flask import Flask,jsonify,request
import repository
from db import init_db
from service import validate_product
app=Flask(__name__)
@app.after_request
def cors(r):r.headers['Access-Control-Allow-Origin']='http://localhost:3000';r.headers['Access-Control-Allow-Headers']='Content-Type';r.headers['Access-Control-Allow-Methods']='GET,POST,OPTIONS';return r
def err(code,msg,status,details=None):return jsonify({'error':{'code':code,'message':msg,'details':details or {}}}),status
@app.get('/api/products')
def products():return jsonify({'data':repository.list_products()})
@app.post('/api/products')
def create():
    data,errors=validate_product(request.get_json(silent=True) or {})
    if errors:return err('VALIDATION_ERROR','Data tidak valid',400,errors)
    i=repository.create_product(data);return jsonify({'id':i,**data}),201
if __name__=='__main__':init_db();app.run(port=5000,debug=True)
