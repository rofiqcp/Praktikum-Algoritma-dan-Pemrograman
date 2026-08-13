> Diadaptasi langsung dari lampiran/panduan pada buku sumber Edisi Agustus 2026.

# Panduan AI-Assisted Coding Mulai Pertemuan 9

Mulai pertemuan 9, peserta diperbolehkan dan didorong menggunakan AI sebagai asisten. AI tidak boleh menggantikan proses berpikir. Peserta harus bisa menjelaskan kode yang diserahkan, menyebut perubahan yang dibuat, dan menunjukkan bukti pengujian.

## Format Prompt Teknis 9 Bagian
| Bagian | Isi |
|---|---|
| 1. Context | Apa yang sedang dibangun dan siapa penggunanya. |
| 2. Environment | OS, Python/Node version, framework, database. |
| 3. Structure | Folder/file yang relevan. |
| 4. Current state | Apa yang sudah bekerja. |
| 5. Problem | Gejala spesifik. |
| 6. Expected | Perilaku yang diharapkan. |
| 7. Evidence | Error log, request/response, potongan kode. |
| 8. Constraints | Bagian yang tidak boleh diubah, library yang boleh/tidak. |
| 9. Verification | Tes yang harus dilakukan setelah fix. |

## Contoh Prompt Debugging
```text
Saya membuat aplikasi Flask di Windows menggunakan Python 3.x.
Route / sudah berjalan, tetapi GET /products menghasilkan HTTP 500.
Struktur: app.py, templates/products.html, static/style.css.
Expected: daftar produk tampil. Actual: Internal Server Error.
Berikut traceback lengkap: [tempel].
Tolong (1) identifikasi root cause, (2) jelaskan file/baris yang bermasalah,
(3) usulkan perubahan minimal, (4) jangan ubah route lain,
(5) berikan langkah verifikasi dan test case setelah perbaikan.
```

## Prompt yang Harus Dihindari
- “Buatkan website lengkap.” — terlalu luas, sulit diverifikasi.
- “Error, fix.” — tidak ada environment, gejala, atau log.
- “Ubah semuanya biar bagus.” — berisiko merusak bagian yang sudah bekerja.
- Menempel API key/password ke prompt atau repository.
- Meminta AI menebak error tanpa traceback/log yang tersedia.

## Prosedur Troubleshooting Universal
```text
REPRODUCE → READ LOG → LOCATE LAYER → HYPOTHESIS → SMALL TEST
→ ONE CHANGE → RETEST → REGRESSION → COMMIT
```
Saat aplikasi berlapis, tentukan layer: browser/UI → JavaScript → network/HTTP → API/backend → database → deployment/runtime. 404: fokus URL/route; 500: backend log; connection refused: server/port; data salah tetapi 200: business logic/query.

## Etika dan Keamanan Prompt
- Jangan kirim password, token, API key, data pribadi sensitif, atau file rahasia ke AI.
- Gunakan placeholder seperti `<API_KEY>`.
- Jangan menerima saran instalasi/package tanpa memahami alasan dan sumbernya.
- Bandingkan solusi AI dengan dokumentasi resmi untuk deployment/security/config yang cepat berubah.
- Jika AI menyarankan menghapus file/database, pahami dampak dan buat backup terlebih dahulu.
