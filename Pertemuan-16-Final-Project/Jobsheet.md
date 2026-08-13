# Jobsheet Pertemuan 16 — Final Project

## Milestone 1 — Requirement & Architecture
- Pilih project dari `Project.md`.
- Tulis scope fitur, non-scope, user flow, service diagram.
- Buat ERD minimal 2 tabel one-to-many.
- Tulis API contract sebelum coding.
- Tulis test strategy minimal 15 kasus.

## Milestone 2 — Database & Python API
- Buat schema/seed/migration strategy sederhana.
- CRUD resource utama.
- JOIN/detail/filter.
- Validation/error contract.
- Parameterized query dan transaction bila operasi multi-step.
- Backend test.

## Milestone 3 — Node Web/UI
- Minimal 4 screen/section.
- Loading, empty, success, error state.
- Form create/update.
- Search/filter.
- Integrasi fetch ke Python API.

## Milestone 4 — Integration & Failure Drill
Uji backend mati, API 404, validation 400, conflict 409, DB constraint, dan data kosong. Catat minimal satu bug asli: reproduce → evidence → root cause → fix → regression test.

## Milestone 5 — Git/Docs/Deploy
Git history harus menunjukkan setup, backend, DB, frontend, integration, fix, test, docs. README harus dapat dipakai orang lain untuk menjalankan dari clone bersih.

## Final Demo 7–10 Menit
1. Problem & requirement.
2. Architecture + ERD.
3. Demo user flow end-to-end.
4. API/DB evidence.
5. Error state/test.
6. Bug yang ditemukan dan diperbaiki.
7. Kesimpulan.

## Starter
```bash
# Terminal 1
cd praktikum/final-starter/backend
python -m pip install -r requirements.txt
python app.py

# Terminal 2
cd ../frontend
npm install
npm start
```
Starter bukan jawaban salah satu project bank.
