> Diadaptasi langsung dari lampiran/panduan pada buku sumber Edisi Agustus 2026.

# Lampiran G — SQL Cheat Sheet

```sql
CREATE TABLE categories (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL UNIQUE
);

CREATE TABLE products (
  id INTEGER PRIMARY KEY,
  category_id INTEGER NOT NULL,
  name TEXT NOT NULL,
  price REAL NOT NULL,
  FOREIGN KEY(category_id) REFERENCES categories(id)
);

SELECT * FROM products;
INSERT INTO products(category_id,name,price) VALUES (?,?,?);
UPDATE products SET price=? WHERE id=?;
DELETE FROM products WHERE id=?;
```

> Gunakan parameterized query/ORM. Jangan menempel input pengguna langsung ke string SQL.
