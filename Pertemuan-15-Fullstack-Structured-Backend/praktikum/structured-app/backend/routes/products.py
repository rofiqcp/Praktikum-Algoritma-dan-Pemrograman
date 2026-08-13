from flask import Blueprint,jsonify,request
from services import product_service as service
bp=Blueprint("products",__name__,url_prefix="/api")

def error_response(e):
    b={"error":{"code":e.code,"message":e.message}}
    if e.details:b["error"]["details"]=e.details
    return jsonify(b),e.status

@bp.get('/categories')
def categories(): return jsonify({"data":service.categories()})
@bp.get('/products')
def products():
    cid=request.args.get('category_id',type=int); return jsonify({"data":service.list_products(request.args.get('q',''),cid)})
@bp.get('/products/<int:pid>')
def detail(pid):
    try:return jsonify(service.get(pid))
    except service.ServiceError as e:return error_response(e)
@bp.post('/products')
def create():
    try:return jsonify(service.create(request.get_json(silent=True) or {})),201
    except service.ServiceError as e:return error_response(e)
@bp.patch('/products/<int:pid>')
def update(pid):
    try:return jsonify(service.update(pid,request.get_json(silent=True) or {}))
    except service.ServiceError as e:return error_response(e)
@bp.delete('/products/<int:pid>')
def delete(pid):
    try:service.delete(pid); return '',204
    except service.ServiceError as e:return error_response(e)
@bp.post('/products/<int:pid>/stock-movements')
def stock(pid):
    try:return jsonify(service.move_stock(pid,request.get_json(silent=True) or {})),201
    except service.ServiceError as e:return error_response(e)
