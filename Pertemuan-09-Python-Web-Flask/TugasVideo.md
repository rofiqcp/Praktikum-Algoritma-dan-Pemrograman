# Tugas Video — Pertemuan 09

## Tema
**Dari Program Terminal menjadi Website Flask yang Bisa Dipakai dan Diuji**

Durasi rekomendasi: **15–25 menit**.

Video bukan sekadar merekam layar saat program berjalan. Mahasiswa harus menjelaskan hubungan browser, HTTP request, route Flask, Python logic, template, dan response sambil menunjukkan bukti bahwa aplikasi benar-benar diuji.

## Struktur Video Wajib

### 1. Pembukaan — 1 menit
Sebutkan nama, kelas, repository, dan tujuan aplikasi.

### 2. Mental Model Web — 2–3 menit
Jelaskan dengan kata sendiri:

```text
Browser → Request → Flask Route → Python Logic → Template/Response → Browser
```

Tunjukkan contoh route dari `app.py` dan halaman yang dihasilkan.

### 3. Struktur Project — 2 menit
Tunjukkan:

- `app.py`;
- `templates/`;
- `static/`;
- `requirements.txt`;
- `test_app.py`.

Jelaskan fungsi masing-masing.

### 4. Demo Halaman dan UI/UX — 3–4 menit
Wajib menunjukkan:

- Home;
- About;
- Products/list data;
- form tambah produk;
- navigation;
- responsive/empty state atau feedback state.

Jelaskan minimal empat istilah UI/UX: hierarchy, consistency, focus, validation, loading/error/success, atau empty state.

### 5. Demo GET/POST dan Validasi — 4–5 menit
Tunjukkan minimal:

1. submit data valid;
2. nama kosong;
3. harga negatif/nonangka;
4. stok non-integer;
5. satu boundary seperti stok `0`.

Jelaskan mengapa validasi server-side tetap diperlukan walaupun form HTML menggunakan `required`.

### 6. Search/Filter — 1–2 menit
Bila project contoh memiliki search, demonstrasikan query yang menghasilkan data dan query yang menghasilkan no-result/empty state.

### 7. Debugging — 2–3 menit
Tunjukkan satu bug yang dapat direproduksi, misalnya:

- 404;
- `TemplateNotFound`;
- field form tidak terbaca;
- static CSS salah path.

Format penjelasan:

```text
Gejala → Bukti → Root Cause → Perubahan → Retest
```

### 8. Automated Test — 2 menit
Jalankan:

```bash
python -m unittest -v test_app.py
```

Tunjukkan hasil test dan jelaskan minimal dua assertion.

### 9. Modifikasi Mandiri — 2 menit
Tunjukkan minimal satu fitur/perbaikan yang bukan sekadar mengganti teks/warna, misalnya detail route, filter, badge stok, validasi duplikat, kategori, atau sort.

## Bukti yang Harus Terlihat
- URL lokal Flask.
- Terminal server.
- Source code route yang sedang dijelaskan.
- Form valid dan invalid.
- Satu error state dan satu success state.
- Hasil automated test.
- Git commit yang berkaitan dengan perubahan.

## Rubrik 100 Poin
| Aspek | Bobot |
|---|---:|
| Mental model client-server/request-response | 15 |
| Flask route/template/static | 20 |
| Form & server-side validation | 20 |
| UI/UX & state | 15 |
| Testing & debugging | 15 |
| Modifikasi mandiri | 10 |
| Penyampaian | 5 |

## Ketentuan
- Jangan menampilkan password, token, API key, atau credential pada video.
- Jangan hanya membaca `Materi.md`; jelaskan dengan contoh program.
- Jika video diedit, alur pengujian tetap harus dapat diikuti.
- Program pada akhir video harus berada dalam kondisi berjalan dan test lulus.
