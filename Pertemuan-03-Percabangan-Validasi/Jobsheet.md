# Jobsheet Pertemuan 03 — Percabangan dan Validasi

## Environment
Scratch + Google Colab + Python.

## Wajib
1. Sistem nilai.
2. Tarif parkir.
3. Seleksi wahana.
4. Promo toko.
5. Klasifikasi suhu.

Jalankan Scratch → semua file `praktikum/python/` → `praktikum/colab/latihan_pertemuan03.ipynb`.

## Test Boundary
| Kasus | Expected | Actual | Pass |
|---|---|---|:---:|
| nilai 74 | belum lulus |  | ☐ |
| nilai 75 | lulus |  | ☐ |
| nilai 76 | lulus |  | ☐ |
| nilai 89/90 | B/A sesuai rule |  | ☐ |
| -1/101 | invalid |  | ☐ |
| kombinasi True/False | sesuai `and/or` |  | ☐ |

## Analisis
1. Mengapa urutan kondisi penting?
2. Apa akibat `>=` diganti `>`?
3. Kapan nested if sebaiknya dihindari?
4. Apa beda validation dan business rule?

## Debug Log
Catat minimal tiga: gejala, bukti/error, hipotesis, perubahan, retest.

## Challenge
Tambahkan satu rule baru, dua test case, lalu regression test rule lama.
