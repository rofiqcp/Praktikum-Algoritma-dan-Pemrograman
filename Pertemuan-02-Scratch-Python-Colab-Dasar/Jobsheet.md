# Jobsheet Pertemuan 02 — Sequence, Input, Output, dan Variabel

## Identitas

| Item | Isian |
|---|---|
| Nama |  |
| NIM |  |
| Kelas |  |
| Tanggal |  |
| Link notebook Colab |  |

## Environment

**Scratch + Google Colab + Python.** Pada pertemuan ini fokus utama adalah sequence, input, output, variable, tipe data, konversi tipe, dan operator. Percabangan formal dibahas pada Pertemuan 03.

## Target Praktikum

Mahasiswa harus mampu membuat algoritma yang sama di Scratch dan Python, memprediksi output sebelum Run, menjalankan seluruh program inti, dan membaca error dasar.

## Pola Kerja

```text
PREDIKSI → JALANKAN → AMATI → CATAT → UBAH SATU HAL → UJI ULANG → SIMPULKAN
```

## P01 — Scratch ke Python: Input dan Output

1. Rakit contoh pada `praktikum/scratch/README.md`.
2. Identifikasi input, process, output, dan variable.
3. Tulis padanan Python menggunakan `input()` dan `print()`.
4. Bandingkan urutan algoritma, bukan hanya bentuk syntax.

## P02 — Kalkulator Belanja

Jalankan:

```bash
python praktikum/python/02_kalkulator_belanja.py
```

Gunakan minimal tiga set input. Sebelum run, hitung total secara manual.

| Harga | Jumlah | Prediksi total | Actual | Pass |
|---:|---:|---:|---:|:---:|
| 10000 | 3 | 30000 |  | ☐ |
| 12500 | 2 | 25000 |  | ☐ |
| 0 | 5 | 0 |  | ☐ |

## P03 — Luas dan Keliling

Jalankan `praktikum/python/03_luas_persegi_panjang.py`.

Fokus: `float`, operator `*`, `+`, dan prioritas operasi. Catat formula yang digunakan sebelum menjalankan program.

## P04 — Konversi Menit

Jalankan:

```bash
python praktikum/python/03_konversi_waktu.py
```

Uji hubungan `//` dan `%`.

| Total menit | Expected |
|---:|---|
| 0 | 0 jam 0 menit |
| 59 | 0 jam 59 menit |
| 60 | 1 jam 0 menit |
| 61 | 1 jam 1 menit |
| 125 | 2 jam 5 menit |

## P05 — Perhitungan Tiga Item

Jalankan `praktikum/python/05_total_tiga_item.py`. Tulis subtotal setiap item dan total manual sebelum Run.

## P06 — Konversi Suhu

Jalankan:

```bash
python praktikum/python/04_konversi_suhu.py
```

Uji minimal `0`, `25`, dan `100` Celsius. Bandingkan hasil dengan formula yang ditulis di Jobsheet.

## P07 — Estimasi Perjalanan

Jalankan `praktikum/python/06_estimasi_perjalanan_sequence.py`. Gunakan input valid terlebih dahulu. Pemeriksaan kondisi input dibahas pada Pertemuan 03.

## P08 — Operator Dasar

Jalankan:

```bash
python praktikum/python/00_operator_demo.py
python praktikum/python/09_input_angka_demo.py
```

Jelaskan perbedaan `/`, `//`, dan `%`.

## Google Colab

Buka notebook pada folder `praktikum/colab/`. Jalankan dari cell paling atas. Setelah mengubah beberapa cell, gunakan Restart runtime/session lalu Run all agar state notebook konsisten.

## Test Wajib

| Kasus | Expected | Actual | Pass |
|---|---|---|:---:|
| integer valid | program menghitung nilai numerik |  | ☐ |
| float valid | desimal diproses |  | ☐ |
| nilai 0 | hasil mengikuti formula |  | ☐ |
| menit 59/60/61 | boundary `//` dan `%` benar |  | ☐ |
| teks dimasukkan ke `int()` | Python menampilkan `ValueError` |  | ☐ |
| nama variable sengaja salah | Python menampilkan `NameError` |  | ☐ |

## Latihan Membaca Error

Pada **salinan** program, ubah satu hal saja. Catat:

```text
Jenis error:
Baris yang ditunjuk:
Expected:
Actual:
Penyebab:
Perbaikan:
Hasil run ulang:
```

Jangan menambahkan `try/except` sebagai solusi pada sesi ini. Tujuannya adalah belajar membaca error; strategi validasi dan penanganan input akan diperkenalkan bertahap pada pertemuan berikutnya.

## Pertanyaan Analisis

1. Apa padanan `ask` Scratch di Python?
2. Apa padanan `say` Scratch di Python?
3. Mengapa hasil `input()` perlu dikonversi untuk perhitungan?
4. Kapan data cocok menggunakan `int` dan kapan `float`?
5. Apa beda `/`, `//`, dan `%`?
6. Mengapa cell Colab yang dijalankan tidak berurutan dapat menghasilkan state membingungkan?
7. Apakah Scratch dan Python harus memiliki syntax sama agar algoritmanya setara? Jelaskan.

## Deliverable

- project Scratch;
- notebook Colab;
- output seluruh program Python inti;
- tabel expected-versus-actual;
- minimal dua catatan error dan perbaikan;
- satu modifikasi mandiri yang masih menggunakan konsep Pertemuan 02;
- kesimpulan.

## Checklist

- [ ] Versi Scratch dijalankan.
- [ ] Program kalkulator dijalankan.
- [ ] Program geometri dijalankan.
- [ ] Program konversi waktu dijalankan.
- [ ] Program tiga item dijalankan.
- [ ] Program konversi suhu dijalankan.
- [ ] Program estimasi dijalankan.
- [ ] Notebook Colab Run all berhasil.
- [ ] Expected dan actual dicatat.
- [ ] Error dasar dibaca dan diperbaiki.
