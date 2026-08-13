import sqlite3
from repositories import product_repository as repo
from schemas.product import validate_product,validate_movement

class ServiceError(Exception):
    def __init__(self,code,message,status=400,details=None): super().__init__(message); self.code=code; self.message=message; self.status=status; self.details=details

def list_products(search="",category_id=None): return repo.list_products(search,category_id)
def categories(): return repo.list_categories()
def get(pid):
    p=repo.get_product(pid)
    if not p: raise ServiceError("NOT_FOUND","Produk tidak ditemukan",404)
    return p

def normalize(payload,current=None):
    partial=current is not None; e=validate_product(payload,partial)
    if e: raise ServiceError("VALIDATION_ERROR","Payload tidak valid",400,e)
    src={**(current or {}),**payload}; data={"name":str(src["name"]).strip(),"category_id":int(src["category_id"]),"price":float(src.get("price",0)),"stock":int(src.get("stock",0))}
    if not repo.category_exists(data["category_id"]): raise ServiceError("INVALID_CATEGORY","Kategori tidak ditemukan",400,{"category_id":"not found"})
    return data

def create(payload):
    data=normalize(payload)
    try: pid=repo.create_product(data)
    except sqlite3.IntegrityError: raise ServiceError("CONFLICT","Nama produk sudah ada",409)
    return get(pid)

def update(pid,payload):
    current=get(pid); data=normalize(payload,current)
    try: repo.update_product(pid,data)
    except sqlite3.IntegrityError: raise ServiceError("CONFLICT","Nama produk sudah ada",409)
    return get(pid)

def delete(pid):
    get(pid); repo.delete_product(pid)

def move_stock(pid,payload):
    e=validate_movement(payload)
    if e: raise ServiceError("VALIDATION_ERROR","Payload tidak valid",400,e)
    status,new_stock=repo.apply_stock_movement(pid,int(payload["qty"]),str(payload.get("note","")))
    if status=="NOT_FOUND": raise ServiceError("NOT_FOUND","Produk tidak ditemukan",404)
    if status=="INSUFFICIENT_STOCK": raise ServiceError("INSUFFICIENT_STOCK","Stok tidak cukup",409)
    return {"product_id":pid,"stock":new_stock}
