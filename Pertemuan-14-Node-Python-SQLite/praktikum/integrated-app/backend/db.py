import sqlite3
from pathlib import Path
DB_PATH=Path(__file__).with_name("app.db")

def connect():
    c=sqlite3.connect(DB_PATH); c.row_factory=sqlite3.Row; return c

def init_db():
    with connect() as c:
        c.execute("""CREATE TABLE IF NOT EXISTS products(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL UNIQUE,price REAL NOT NULL CHECK(price>=0),stock INTEGER NOT NULL CHECK(stock>=0))""")
        if c.execute("SELECT COUNT(*) FROM products").fetchone()[0]==0:
            c.executemany("INSERT INTO products(name,price,stock) VALUES(?,?,?)",[("Keyboard",250000,10),("Mouse",120000,6)])

def rows(sql,args=()):
    with connect() as c: return [dict(x) for x in c.execute(sql,args).fetchall()]

def row(sql,args=()):
    with connect() as c:
        x=c.execute(sql,args).fetchone(); return dict(x) if x else None
