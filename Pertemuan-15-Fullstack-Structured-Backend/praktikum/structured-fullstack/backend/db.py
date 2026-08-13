import sqlite3
from pathlib import Path
DB_PATH=Path(__file__).with_name('app.db')
def connect():
    c=sqlite3.connect(DB_PATH); c.row_factory=sqlite3.Row; c.execute('PRAGMA foreign_keys=ON'); return c
def init_db():
    with connect() as c:
        c.executescript('CREATE TABLE IF NOT EXISTS categories(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL UNIQUE);CREATE TABLE IF NOT EXISTS products(id INTEGER PRIMARY KEY AUTOINCREMENT,category_id INTEGER NOT NULL,name TEXT NOT NULL,price REAL NOT NULL CHECK(price>=0),stock INTEGER NOT NULL CHECK(stock>=0),FOREIGN KEY(category_id) REFERENCES categories(id));')
        c.execute("INSERT OR IGNORE INTO categories(id,name) VALUES(1,'Umum')"); c.commit()
