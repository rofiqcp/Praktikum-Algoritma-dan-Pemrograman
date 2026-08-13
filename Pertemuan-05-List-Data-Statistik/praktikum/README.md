# Praktikum Pertemuan 05 — List, Data, Pencarian, Statistik

Urutan belajar wajib: **Scratch → Colab → Python → testing → challenge**.

## 1. Scratch
Rakit latihan pada `scratch/README.md`. Fokus pada List `Nilai`, operasi add/delete/item/length, loop pada list, pencarian, dan perhitungan total/rata-rata.

## 2. Google Colab
Buka `colab/latihan_pertemuan05.ipynb`, kemudian gunakan **Run all** dari awal. Notebook `colab/daftar_nilai.ipynb` dapat digunakan sebagai contoh tambahan. Jangan menjalankan cell secara acak karena state list dapat berbeda.

## 3. Python
Jalankan berurutan dari folder `praktikum`:

```bash
python python/01_statistik_nilai.py
python python/02_daftar_belanja.py
python python/03_stok_barang.py
python python/04_suhu_harian.py
python python/05_voting.py
python python/06_pencarian_produk.py
python python/07_list_dictionary_summary.py
```

## 4. Unit Test
Dari folder `praktikum` jalankan:

```bash
python -m unittest discover -s tests -v
```

Baca juga `TESTING.md` untuk pola pengujian data kosong, satu elemen, boundary, pencarian berhasil, dan pencarian tidak ditemukan.

## 5. Yang Harus Diamati
Untuk setiap program catat input, isi list/dictionary sebelum proses, isi sesudah proses, output, expected, actual, dan hasil pengujian.

Lihat `../Materi.md` untuk teori dan `../Jobsheet.md` untuk urutan eksperimen lengkap.
