# Jobsheet Pertemuan 12 — Checkpoint Web + API + Deployment

## 1. Analisis Sebelum Coding
- Pilih satu project dari `Project.md`.
- Buat user flow dan page map minimal 3 halaman.
- Definisikan minimal 6 komponen UI.
- Tulis endpoint internal: method, path, request, response, status code.
- Pilih external/mock API; tulis timeout, failure state, dan fallback yang aman.

## 2. Implementasi Bertahap
1. Skeleton Flask + templates/static.
2. Halaman utama/list/form.
3. Internal REST API.
4. External/mock API client.
5. Loading/empty/error/success states.
6. Test.
7. Git commit per milestone.
8. Deployment.

## 3. Testing Minimum
Minimal 10 test case, termasuk:
- page 200;
- page 404;
- GET API;
- POST valid;
- POST invalid;
- not-found;
- duplicate/conflict bila relevan;
- external API sukses;
- external API timeout/failure;
- public URL regression test.

## 4. Deployment Evidence
Public URL, `/health` bila tersedia, screenshot build/runtime log, environment variable tanpa secret, serta test dari perangkat/browser lain.

## Starter
```bash
cd praktikum/starter-web-api
python -m pip install -r requirements.txt
python app.py
python -m unittest -v test_app.py
```
