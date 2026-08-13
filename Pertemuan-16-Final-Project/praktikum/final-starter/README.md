# Final Starter — Node + Python + SQLite

## Architecture
```text
Browser :3000 → Node static UI → fetch → Flask API :5001 → SQLite
                                           categories 1 ── N products
```

## Backend
```bash
cd backend
python -m venv .venv
python -m pip install -r requirements.txt
python app.py
python -m unittest -v test_app.py
```

## Frontend
```bash
cd frontend
npm install
npm start
```

## Scope Starter
- relational categories/products;
- product CRUD;
- filter/search;
- JSON error contract;
- Node frontend loading/empty/error/success;
- unit tests.

Adaptasikan arsitektur, jangan submit starter tanpa desain sendiri.
