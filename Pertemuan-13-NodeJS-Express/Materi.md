# Materi Pertemuan 13 — Node.js: JavaScript di Luar Browser dan Web Lokal dengan Express

> Sumber utama: *Buku Panduan Praktik: Pemrograman Dasar hingga Full Stack — 16 Pertemuan Terstruktur, Edisi Agustus 2026*.

Node.js diperkenalkan setelah peserta memahami web Python, sehingga konsep server, route, request, dan response sudah familiar. Fokus sesi: runtime Node, npm, modules, Express, dan web lokal.

## Target Kompetensi
- Menjelaskan perbedaan JavaScript browser dan Node.js runtime.
- Menggunakan `node` dan `npm`.
- Membaca `package.json` dan memahami dependency.
- Membuat Express server, route, static files, dan middleware dasar.
- Menggunakan `fetch` di frontend untuk memanggil endpoint lokal.

## Output
- Node/Express web lokal pada localhost.
- Project dengan `public/` dan route API sederhana.
- `package.json` dan Git commit.

## Mental Model
```text
Browser JavaScript: DOM, event UI, fetch
Node.js JavaScript : filesystem/runtime/server/npm
Express            : routing + middleware + response
```

## npm dan package.json
```bash
node --version
npm --version
npm init -y
npm install express
npm start
```
`package.json` menjelaskan metadata, scripts, dependency, dan batas runtime bila ditetapkan.

## Express Minimum
```javascript
const express = require('express');
const app = express();
app.use(express.json());
app.use(express.static('public'));
app.get('/api/status', (req,res) => res.json({status:'ok'}));
app.listen(3000);
```

## Middleware
Middleware berada di jalur request. Contoh: JSON parser, logger, authentication checker, CORS middleware. Middleware dapat memodifikasi request/response atau menghentikan request.

## Frontend Fetch
```javascript
const response = await fetch('/api/items');
if (!response.ok) throw new Error(`HTTP ${response.status}`);
const data = await response.json();
```
UI perlu loading, empty, success, dan error state.

## Struktur Project
```text
node-express/
├── package.json
├── app.js
├── server.js
├── public/
│   ├── index.html
│   ├── app.js
│   └── style.css
└── test/
    └── app.test.js
```

## Troubleshooting
| Gejala | Fokus |
|---|---|
| `Cannot find module` | `npm install`, dependency/package name |
| `EADDRINUSE` | port sudah dipakai |
| `req.body` undefined | `express.json()` atau Content-Type |
| Static 404 | path `express.static` |
| fetch gagal parse JSON | status/Content-Type/response body |
| perubahan tidak muncul | restart process/cache browser |
