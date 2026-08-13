from db import connect
def list_products():
    with connect() as c: rows=c.execute('SELECT p.id,p.name,p.price,p.stock,p.category_id,c.name category_name FROM products p JOIN categories c ON c.id=p.category_id ORDER BY p.id').fetchall()
    return [dict(r) for r in rows]
def category_exists(i):
    with connect() as c: return c.execute('SELECT 1 FROM categories WHERE id=?',(i,)).fetchone() is not None
def create_product(d):
    with connect() as c: cur=c.execute('INSERT INTO products(category_id,name,price,stock) VALUES(?,?,?,?)',(d['category_id'],d['name'],d['price'],d['stock'])); c.commit(); return cur.lastrowid
