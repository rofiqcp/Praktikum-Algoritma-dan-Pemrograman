# Materi Pertemuan 13 — Node.js, npm, Express, dan Web Lokal

Node.js menjalankan JavaScript di luar browser. Pada sesi ini konsep server/route/request/response yang sudah dipahami dari Flask dipetakan ke Node + Express.

## Target
- Membedakan JavaScript browser dan Node runtime.
- Menggunakan `node`, `npm`, `package.json`, dependency dan script.
- Membuat Express server, route, static files dan middleware dasar.
- Menggunakan `fetch()` frontend ke endpoint lokal.

## Mental Model
`browser → Express middleware → route → response`. Middleware berada di jalur request dan dapat membaca/mengubah request-response atau menghentikannya.

Troubleshooting: `Cannot find module` → `npm install`; port in use → hentikan proses/ganti port; route 404 → cek path; JSON undefined → pastikan parser/method/header; frontend fetch gagal → cek Network tab/server log.
