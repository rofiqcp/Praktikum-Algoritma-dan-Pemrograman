# Jobsheet Pertemuan 06 — Function, Dekomposisi, dan Debugging

## Tujuan

Mahasiswa mampu memecah masalah menjadi function kecil, menggunakan parameter dan return, membandingkan My Blocks Scratch dengan function Python, menguji function secara terpisah, serta melakukan debugging berbasis bukti.

## Urutan Praktikum

```text
SCRATCH MY BLOCKS → COLAB → PYTHON FUNCTION → TEST → DEBUG → REFACTOR
```

## P01 — My Blocks Scratch

Buka `praktikum/scratch/README.md`. Buat minimal dua custom block dan gunakan input/parameter pada block. Jelaskan bagian script mana yang dipindahkan menjadi My Blocks dan mengapa.

## P02 — Kalkulator Modular

Jalankan:

```bash
python praktikum/python/01_kalkulator_modular.py
```

Identifikasi function, parameter, argument, function call, dan hasil yang dikembalikan.

## P03 — Sistem Nilai Modular

Jalankan:

```bash
python praktikum/python/02_sistem_nilai_modular.py
```

Buat diagram pemecahan:

```text
program utama
├── validasi
├── hitung
└── tampilkan hasil
```

Tambahkan satu function kecil yang relevan tanpa menggabungkan seluruh logic ke satu tempat.

## P04 — Menu Modular

Jalankan:

```bash
python praktikum/python/03_menu_modular.py
```

Catat function mana yang mengatur menu dan function mana yang mengolah data.

## P05 — Tracing Program

Jalankan `04_bug_hunt.py`. Sebelum mengubah source, buat tracing table nilai variable utama pada setiap iterasi. Tuliskan:

- input yang digunakan;
- expected result;
- actual result;
- function/baris terkait;
- dugaan penyebab;
- satu perubahan;
- hasil retest.

## P06 — Program Modular Lengkap

Jalankan:

```bash
python praktikum/python/program_modular.py
```

Identifikasi minimal tiga function dan jelaskan tanggung jawab masing-masing.

## P07 — Google Colab

Buka dan jalankan:

```text
praktikum/colab/latihan_pertemuan06.ipynb
praktikum/colab/program_modular.ipynb
```

Gunakan Run all agar urutan state notebook jelas.

## P08 — Unit Test Sederhana

Dari folder pertemuan:

```bash
python -m unittest discover -s praktikum/tests -v
```

Catat test yang dijalankan, expected, actual, dan status pass/fail.

## P09 — Refactor

Pilih satu program dari P02–P04. Pecah satu bagian menjadi function baru tanpa mengubah output yang benar. Jalankan test/input lama sebelum dan sesudah refactor.

## Tabel Analisis Function

| Function | Parameter | Return | Tanggung jawab | Test utama |
|---|---|---|---|---|
| 1 |  |  |  |  |
| 2 |  |  |  |  |
| 3 |  |  |  |  |
| 4 |  |  |  |  |
| 5 |  |  |  |  |

## Test Case Minimum

Siapkan minimal delapan test case untuk function yang dipelajari: normal, nol, boundary, data kosong bila relevan, serta variasi input yang membuat jalur condition berbeda.

## Challenge

Buat program CLI kecil dengan minimal lima function: satu function menu, satu validasi, satu pencarian/perhitungan, satu pengolahan data, dan satu output/ringkasan. Program harus memiliki minimal enam test case.

## Pertanyaan Analisis

1. Apa beda parameter dan argument?
2. Apa beda `print()` dan `return`?
3. Mengapa function kecil lebih mudah diuji?
4. Kapan penggunaan global variable membuat program sulit dipahami?
5. Mengapa tracing dilakukan sebelum perubahan?
6. Apa yang dimaksud regression test setelah refactor?
7. Apa hubungan My Blocks Scratch dengan function Python?

## Bukti Pengumpulan

Project/screenshot Scratch, notebook Colab, output semua Python, tracing table, hasil unit test, source hasil refactor, challenge, jawaban analisis, dan kesimpulan.

## Checklist

- [ ] My Blocks selesai.
- [ ] Semua contoh Python dijalankan.
- [ ] Notebook Colab dijalankan.
- [ ] Unit test dijalankan.
- [ ] Saya dapat menjelaskan parameter dan return.
- [ ] Saya membuat tracing sebelum memperbaiki hasil.
- [ ] Saya melakukan satu refactor dan retest.
