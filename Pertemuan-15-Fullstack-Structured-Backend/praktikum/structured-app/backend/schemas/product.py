def validate_product(payload,partial=False):
    e={}
    if not partial or "name" in payload:
        if not str(payload.get("name","")).strip(): e["name"]="wajib diisi"
    if not partial or "category_id" in payload:
        try:
            if int(payload.get("category_id",0))<=0: raise ValueError
        except (ValueError,TypeError): e["category_id"]="harus integer > 0"
    for k,cast in [("price",float),("stock",int)]:
        if not partial or k in payload:
            try:
                if cast(payload.get(k,0))<0: raise ValueError
            except (ValueError,TypeError): e[k]="harus >= 0"
    return e

def validate_movement(payload):
    try:
        qty=int(payload.get("qty"));
        if qty==0: raise ValueError
    except (ValueError,TypeError): return {"qty":"harus integer dan tidak boleh 0"}
    return {}
