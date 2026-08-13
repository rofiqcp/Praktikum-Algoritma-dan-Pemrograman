import math

PRODUCT_FIELDS={"name","category_id","price","stock"}
MOVEMENT_FIELDS={"qty","note"}

def exact_int(value):
    if isinstance(value,bool):raise ValueError
    if isinstance(value,int):return value
    if isinstance(value,float):
        if not value.is_integer():raise ValueError
        return int(value)
    text=str(value).strip()
    if not text or not text.lstrip('+-').isdigit():raise ValueError
    return int(text)

def nonnegative_number(value):
    if isinstance(value,bool):raise ValueError
    number=float(value)
    if not math.isfinite(number) or number<0:raise ValueError
    return number

def validate_product(payload,partial=False):
    if not isinstance(payload,dict):return {"_schema":"JSON harus berupa object"}
    e={}
    unknown=sorted(set(payload)-PRODUCT_FIELDS)
    if unknown:e["_schema"]="field tidak dikenal: "+", ".join(unknown)
    if partial and not payload:e["_schema"]="minimal satu field harus dikirim"
    if not partial or "name" in payload:
        if not str(payload.get("name","")).strip():e["name"]="wajib diisi"
    if not partial or "category_id" in payload:
        try:
            if exact_int(payload.get("category_id",0))<=0:raise ValueError
        except (ValueError,TypeError,OverflowError):e["category_id"]="harus integer > 0"
    if not partial or "price" in payload:
        try:nonnegative_number(payload.get("price",0))
        except (ValueError,TypeError,OverflowError):e["price"]="harus angka >= 0"
    if not partial or "stock" in payload:
        try:
            if exact_int(payload.get("stock",0))<0:raise ValueError
        except (ValueError,TypeError,OverflowError):e["stock"]="harus bilangan bulat >= 0"
    return e

def validate_movement(payload):
    if not isinstance(payload,dict):return {"_schema":"JSON harus berupa object"}
    e={}
    unknown=sorted(set(payload)-MOVEMENT_FIELDS)
    if unknown:e["_schema"]="field tidak dikenal: "+", ".join(unknown)
    try:
        qty=exact_int(payload.get("qty"))
        if qty==0:raise ValueError
    except (ValueError,TypeError,OverflowError):e["qty"]="harus integer dan tidak boleh 0"
    return e
