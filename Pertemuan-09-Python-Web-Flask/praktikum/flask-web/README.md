# Flask Web — Pertemuan 09

## Setup & Run
```bash
python -m venv .venv
python -m pip install -r requirements.txt
python app.py
```
Buka `http://127.0.0.1:5000`.

## Test
```bash
python -m unittest -v test_app.py
```

Routes: `/`, `/about`, `/products`, `/products/new`; ada custom 404. Data masih in-memory sehingga restart server mengembalikan data awal.
