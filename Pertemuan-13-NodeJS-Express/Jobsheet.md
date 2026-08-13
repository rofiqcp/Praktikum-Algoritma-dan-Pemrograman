# Jobsheet Pertemuan 13 — Node.js + Express

## Setup
```bash
cd praktikum/node-express
node --version
npm --version
npm install
npm start
```
Buka `http://127.0.0.1:3000`.

## Percobaan Wajib
1. `GET /api/status`.
2. `GET /api/items`.
3. `POST /api/items` valid/invalid.
4. Static `public/index.html`.
5. Frontend `fetch` menampilkan data dan error state.
6. Logger middleware.
7. Jalankan test Node.

## Test
```bash
npm test
```
Uji server status, JSON collection, validation 400, create 201, dan static page.

## Analisis
1. Apa beda JS browser dan Node?
2. Apa fungsi `package.json` vs `node_modules`?
3. Mengapa `node_modules` tidak perlu di-commit?
4. Apa urutan middleware dan route?
