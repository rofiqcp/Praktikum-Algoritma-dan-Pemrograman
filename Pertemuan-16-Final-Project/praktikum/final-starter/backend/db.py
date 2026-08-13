import sqlite3,os
from pathlib import Path
DB=Path(os.getenv("DATABASE_PATH",Path(__file__).with_name("final.db")))

def connect():
    c=sqlite3.connect(DB); c.row_factory=sqlite3.Row; c.execute("PRAGMA foreign_keys=ON"); return c

def init_db():
    with connect() as c:
        c.executescript("""
        CREATE TABLE IF NOT EXISTS categories(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL UNIQUE);
        CREATE TABLE IF NOT EXISTS products(id INTEGER PRIMARY KEY AUTOINCREMENT,category_id INTEGER NOT NULL REFERENCES categories(id),name TEXT NOT NULL UNIQUE,price REAL NOT NULL CHECK(price>=0),stock INTEGER NOT NULL CHECK(stock>=0));
        """)
        if c.execute("SELECT COUNT(*) FROM categories").fetchone()[0]==0:c.executemany("INSERT INTO categories(name) VALUES(?)",[("Peripheral",),("Display",)])
        if c.execute("SELECT COUNT(*) FROM products").fetchone()[0]==0:c.executemany("INSERT INTO products(category_id,name,price,stock) VALUES(?,?,?,?)",[(1,"Keyboard",250000,10),(2,"Monitor",1800000,4)])

def all_rows(sql,args=()):
    with connect() as c:return [dict(x) for x in c.execute(sql,args)]
def one(sql,args=()):
    with connect() as c:
        r=c.execute(sql,args).fetchone();return dict(r) if r else None
