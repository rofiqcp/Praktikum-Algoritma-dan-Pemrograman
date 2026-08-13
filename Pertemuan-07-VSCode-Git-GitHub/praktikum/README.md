# Praktikum Pertemuan 07

```bash
cd python-local
python -m venv .venv
# aktifkan sesuai OS
python main.py
python -m unittest discover -s tests -v
```

Setelah program stabil:
```bash
git init
git add .
git commit -m "feat: tambah kalkulator diskon"
git commit -m "test: tambah boundary diskon"
git commit -m "docs: tambah petunjuk menjalankan"
```

Jangan commit `.venv/`, `.env`, cache, atau credential.
