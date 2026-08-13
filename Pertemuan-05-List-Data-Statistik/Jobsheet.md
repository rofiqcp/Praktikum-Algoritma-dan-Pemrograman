# Jobsheet Pertemuan 05 — List, Data, Pencarian, dan Statistik

## Tujuan
Mahasiswa mampu membuat dan memodifikasi list, melakukan loop dan pencarian, menghitung statistik sederhana, menggunakan dictionary serta list of dictionaries, membandingkan implementasi Scratch dengan Python/Colab, dan menguji kasus data kosong maupun data tidak ditemukan.

## Urutan Praktikum
1. Kerjakan latihan Scratch pada `praktikum/scratch/README.md`.
2. Jalankan `praktikum/colab/latihan_pertemuan05.ipynb` dengan Run all.
3. Jalankan seluruh program Python berikut secara berurutan.
4. Catat state data sebelum dan sesudah operasi.
5. Jalankan unit test.
6. Kerjakan challenge mandiri dan tambahkan test sendiri.

## P01 — Operasi List
Gunakan lima nilai awal. Lakukan akses elemen pertama/terakhir, update, append, remove/pop, dan pengukuran panjang list. Bandingkan index Scratch dengan index Python yang dimulai dari 0.

## P02 — Statistik Nilai
Jalankan:
```bash
python praktikum/python/01_statistik_nilai.py
```
Catat jumlah data, total, minimum, maksimum, rata-rata, dan jumlah nilai yang memenuhi batas lulus. Hitung manual sebelum menjalankan program. Uji juga satu elemen dan list kosong melalui function/test yang tersedia.

## P03 — Daftar Belanja
Jalankan:
```bash
python praktikum/python/02_daftar_belanja.py
```
Uji tambah, tampil, perubahan isi list, data tersedia, dan data tidak tersedia.

## P04 — Dictionary/Stok
Jalankan:
```bash
python praktikum/python/03_stok_barang.py
```
Identifikasi key `nama`, `harga`, dan `stok`. Tambahkan satu record buatan sendiri, baca key yang tersedia, lalu jelaskan perbedaan akses berdasarkan index dan berdasarkan key.

## P05 — Suhu Harian
Jalankan:
```bash
python praktikum/python/04_suhu_harian.py
```
Uji beberapa nilai positif, nol, negatif, dan satu data saja. Catat minimum, maksimum, dan rata-rata bila tersedia pada program.

## P06 — Voting
Jalankan:
```bash
python praktikum/python/05_voting.py
```
Identifikasi penggunaan list, loop, condition, dan counter. Uji beberapa komposisi suara dan kondisi hasil sama bila relevan.

## P07 — Pencarian Produk
Jalankan:
```bash
python praktikum/python/06_pencarian_produk.py
```
Uji huruf besar/kecil, spasi tambahan, produk tersedia, dan produk tidak tersedia. Jelaskan mengapa normalisasi input membantu pencarian.

## P08 — List of Dictionaries
Jalankan:
```bash
python praktikum/python/07_list_dictionary_summary.py
```
Identifikasi struktur list sebagai kumpulan record dan dictionary sebagai satu record. Jelaskan kapan struktur ini lebih tepat daripada beberapa list terpisah.

## P09 — Unit Test
Dari folder pertemuan jalankan:
```bash
cd praktikum
python -m unittest discover -s tests -v
```
Kembali ke folder pertemuan setelah selesai bila melanjutkan pekerjaan lain.

Catat nama test, kondisi yang diuji, expected, actual, dan status. Baca `praktikum/TESTING.md` untuk panduan tambahan.

## Pengujian Minimum
Siapkan minimal 10 test case manual/otomatis. Setiap baris harus mempunyai fitur, input/state, expected, actual, dan status pass/fail. Wajib mencakup:
- data normal;
- satu elemen;
- nilai batas;
- list kosong;
- pencarian berhasil;
- pencarian tidak berhasil;
- variasi huruf/spasi untuk pencarian;
- key/record yang benar;
- perubahan data sebelum/sesudah operasi;
- satu regression test setelah modifikasi.

## Challenge
Pilih satu: jumlah nilai di atas rata-rata, penanda stok rendah, fitur hapus data, menu mini tambah/tampil/cari/hapus/keluar, atau ringkasan list of dictionaries. Tambahkan minimal tiga test case untuk challenge.

## Pertanyaan Analisis
1. Mengapa list lebih scalable daripada variable terpisah?
2. Mengapa index dimulai dari 0 penting di Python?
3. Apa beda list dan dictionary?
4. Mengapa rata-rata membutuhkan pemeriksaan data kosong?
5. Bagaimana loop dan condition dari pertemuan sebelumnya digunakan kembali?
6. Kapan list of dictionaries lebih tepat digunakan?
7. Mengapa pencarian sebaiknya diuji untuk found dan not-found?
8. Mengapa test lama perlu dijalankan lagi setelah challenge ditambahkan?

## Bukti Pengumpulan
Project/screenshot Scratch, notebook Colab, output seluruh Python, hasil unit test, tabel expected-versus-actual, source challenge, jawaban analisis, dan kesimpulan.

## Checklist
- [ ] Scratch dijalankan.
- [ ] Notebook Colab Run all berhasil.
- [ ] Program 01–07 dijalankan.
- [ ] Unit test lulus.
- [ ] Kasus kosong dan not-found diuji.
- [ ] Minimal 10 test case dicatat.
- [ ] Challenge dibuat dan diretest.
