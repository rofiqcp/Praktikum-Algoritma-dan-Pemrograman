# Materi Pertemuan 03 — Percabangan, Operator Logika, dan Validasi

## Target Kompetensi
- Membedakan `if`, `if-else`, dan `if-elif-else`.
- Menggunakan operator perbandingan dan `and`, `or`, `not`.
- Membuat validasi input dan menguji boundary value.
- Menerjemahkan condition Scratch ke Python.

## Mental Model
Sebelum menulis kode, tulis aturan: **Jika kondisi X benar lakukan A; jika tidak lakukan B.** Tentukan data tepat di batas, misalnya syarat lulus `nilai >= 75` diuji dengan 74, 75, 76.

## Contoh Sistem Nilai
Urutan kondisi harus dari yang paling tinggi/spesifik. Nilai di luar 0–100 ditolak. Implementasi runnable tersedia pada `praktikum/python/sistem_nilai.py` dan notebook Colab.

## Debugging
- `IndentationError`: rapikan blok empat spasi.
- Semua data masuk cabang pertama: kondisi terlalu umum diletakkan di atas.
- Boundary salah: bedakan `>` dan `>=`.
- Logika `and/or` membingungkan: tulis dulu dalam bahasa biasa.
