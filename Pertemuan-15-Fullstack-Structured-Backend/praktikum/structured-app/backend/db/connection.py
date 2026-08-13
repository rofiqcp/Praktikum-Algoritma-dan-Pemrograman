import sqlite3
from pathlib import Path
DB=Path(__file__).resolve().parents[1]/"app.db"

def connect():
    c=sqlite3.connect(DB); c.row_factory=sqlite3.Row; c.execute("PRAGMA foreign_keys=ON"); return c

def init_db():
    with connect() as c:
        c.executescript("""
        CREATE TABLE IF NOT EXISTS categories(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL UNIQUE);
        CREATE TABLE IF NOT EXISTS products(id INTEGER PRIMARY KEY AUTOINCREMENT,category_id INTEGER NOT NULL REFERENCES categories(id),name TEXT NOT NULL UNIQUE,price REAL NOT NULL CHECK(price>=0),stock INTEGER NOT NULL CHECK(stock>=0));
        CREATE TABLE IF NOT EXISTS stock_movements(id INTEGER PRIMARY KEY AUTOINCREMENT,product_id INTEGER NOT NULL REFERENCES products(id) ON DELETE CASCADE,qty INTEGER NOT NULL,note TEXT NOT NULL DEFAULT '',created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP);
        """)
        if c.execute("SELECT COUNT(*) FROM categories").fetchone()[0]==0:
            c.executemany("INSERT INTO categories(name) VALUES(?)",[("Peripheral",),("Display",)])
        if c.execute("SELECT COUNT(*) FROM products").fetchone()[0]==0:
            c.executemany("INSERT INTO products(category_id,name,price,stock) VALUES(?,?,?,?)",[(1,"Keyboard",250000,10),(1,"Mouse",120000,6),(2,"Monitor",1800000,4)])
