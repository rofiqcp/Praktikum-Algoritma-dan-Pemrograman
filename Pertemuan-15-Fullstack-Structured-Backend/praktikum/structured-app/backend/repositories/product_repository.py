from db.connection import connect

def list_categories():
    with connect() as c:return [dict(x) for x in c.execute("SELECT id,name FROM categories ORDER BY name")]

def category_exists(cid):
    with connect() as c:return c.execute("SELECT 1 FROM categories WHERE id=?",(cid,)).fetchone() is not None

def list_products(search="",category_id=None):
    sql="""SELECT p.id,p.name,p.price,p.stock,p.category_id,c.name category_name FROM products p JOIN categories c ON c.id=p.category_id WHERE p.name LIKE ?"""; args=[f"%{search}%"]
    if category_id is not None: sql += " AND p.category_id=?"; args.append(category_id)
    sql += " ORDER BY p.name"
    with connect() as c:return [dict(x) for x in c.execute(sql,args)]

def get_product(pid):
    with connect() as c:
        r=c.execute("""SELECT p.id,p.name,p.price,p.stock,p.category_id,c.name category_name FROM products p JOIN categories c ON c.id=p.category_id WHERE p.id=?""",(pid,)).fetchone(); return dict(r) if r else None

def create_product(data):
    with connect() as c:
        cur=c.execute("INSERT INTO products(category_id,name,price,stock) VALUES(?,?,?,?)",(data["category_id"],data["name"],data["price"],data["stock"])); return cur.lastrowid

def update_product(pid,data):
    with connect() as c:c.execute("UPDATE products SET category_id=?,name=?,price=?,stock=? WHERE id=?",(data["category_id"],data["name"],data["price"],data["stock"],pid))

def delete_product(pid):
    with connect() as c:return c.execute("DELETE FROM products WHERE id=?",(pid,)).rowcount

def apply_stock_movement(pid,qty,note=""):
    with connect() as c:
        r=c.execute("SELECT stock FROM products WHERE id=?",(pid,)).fetchone()
        if not r:return "NOT_FOUND",None
        new_stock=r["stock"]+qty
        if new_stock<0:return "INSUFFICIENT_STOCK",None
        c.execute("UPDATE products SET stock=? WHERE id=?",(new_stock,pid))
        c.execute("INSERT INTO stock_movements(product_id,qty,note) VALUES(?,?,?)",(pid,qty,note))
        return "OK",new_stock
