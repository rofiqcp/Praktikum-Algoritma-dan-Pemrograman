# Starter Web/API — Pertemuan 12

Starter ini adalah kerangka checkpoint. Sesuaikan nama resource, halaman, field, dan aturan dengan project yang dipilih dari `Project.md`.

## Run
```bash
python -m pip install -r requirements.txt
python app.py
```

## Test
```bash
python -m unittest -v test_app.py
```

Halaman utama: `/`, `/plans`, dan `/external`.

API contoh: `/api/health`, `/api/plans`, `/api/plans/<id>`, serta `/api/external-preview`.

Integrasi mock dapat diuji dengan `mode=success`, `mode=empty`, `mode=timeout`, dan `mode=error`. Logika mock dipisahkan ke `external_client.py` agar kondisi berhasil dan gagal dapat diuji secara konsisten.

File `.env.example`, `.gitignore`, `TEST_PLAN.md`, dan `mock_external.json` disediakan sebagai contoh kelengkapan project. Data internal masih berada di memori dan kembali ke kondisi awal ketika server dimulai ulang.
