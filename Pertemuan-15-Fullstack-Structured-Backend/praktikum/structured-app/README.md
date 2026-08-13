# Structured Full-stack Preparation

## Architecture
```text
Node static UI :3000
  → Browser fetch
Python Flask :5001
  routes → services → repositories → SQLite
                     ↘ schema validation
```

## Backend
```bash
cd backend
python -m pip install -r requirements.txt
python main.py
python -m unittest -v test_backend.py
```

## Frontend
```bash
cd frontend
npm install
npm start
```

`app.db` dibuat otomatis dan tidak perlu di-commit.
