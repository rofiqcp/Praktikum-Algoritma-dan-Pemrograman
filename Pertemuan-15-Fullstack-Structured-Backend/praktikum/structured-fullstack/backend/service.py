import repository
def validate_product(b):
    e={}; name=str(b.get('name','')).strip(); cid=b.get('category_id'); price=b.get('price'); stock=b.get('stock')
    if not name:e['name']='wajib'
    if not isinstance(cid,int):e['category_id']='harus integer'
    elif not repository.category_exists(cid):e['category_id']='tidak ditemukan'
    if not isinstance(price,(int,float)) or isinstance(price,bool) or price<0:e['price']='angka >=0'
    if not isinstance(stock,int) or isinstance(stock,bool) or stock<0:e['stock']='integer >=0'
    return (None,e) if e else ({'name':name,'category_id':cid,'price':float(price),'stock':stock},None)
