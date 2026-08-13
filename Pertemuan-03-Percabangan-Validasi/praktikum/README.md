# Praktikum Pertemuan 03 — Percabangan dan Validasi

## Urutan Praktikum

1. Rakit satu keputusan pada `scratch/README.md`.
2. Jalankan `python/01_sistem_nilai.py` sampai `python/05_klasifikasi_suhu.py`.
3. Jalankan `python/06_boundary_demo.py` dan `python/07_logika_and_or.py` sebagai demo tambahan.
4. Buka `colab/latihan_pertemuan03.ipynb` dan Run all.
5. Isi boundary test pada `../Jobsheet.md` sebelum membuat variasi sendiri.

## Fokus Setiap Program

| Program | Fokus |
|---|---|
| `01_sistem_nilai.py` | urutan `if/elif/else`, validasi domain, boundary |
| `02_tarif_parkir.py` | keputusan bertingkat dan boundary durasi |
| `03_seleksi_wahana.py` | dua syarat dengan `and` |
| `04_promo_toko.py` | kombinasi condition dan operator logika |
| `05_klasifikasi_suhu.py` | interval dan urutan condition |
| `06_boundary_demo.py` | perbedaan tepat pada batas |
| `07_logika_and_or.py` | tabel perilaku `and`, `or`, `not` |

## Pola Uji

Untuk setiap program:

```text
Tulis rule → tentukan boundary → prediksi → Run → catat actual → trace condition → retest
```

Minimal satu program harus diuji dengan data di bawah batas, tepat batas, di atas batas, serta data di luar domain bila relevan.

## Catatan Scope

Beberapa contoh menggunakan function sebagai pengayaan struktur kode. Kompetensi inti Pertemuan 03 tetap berada pada logika `input → condition → output`; modularisasi function dibahas lebih dalam pada Pertemuan 06.
