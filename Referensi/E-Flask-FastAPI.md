> Diadaptasi langsung dari lampiran/panduan pada buku sumber Edisi Agustus 2026.

# Lampiran E — Flask dan FastAPI Ringkas

## Flask
```python
from flask import Flask,jsonify
app=Flask(__name__)

@app.get("/api/health")
def health():
    return jsonify({"status":"ok"})
```

## FastAPI
```python
from fastapi import FastAPI
app=FastAPI()

@app.get("/api/health")
def health():
    return {"status":"ok"}
```

Pilih satu framework untuk project, jangan menggabungkan Flask dan FastAPI tanpa alasan. Flask baik untuk memahami web/template sederhana; FastAPI nyaman untuk API dengan type hints/schema. Fokus pembelajaran adalah konsep HTTP dan backend, bukan fanatisme framework.
