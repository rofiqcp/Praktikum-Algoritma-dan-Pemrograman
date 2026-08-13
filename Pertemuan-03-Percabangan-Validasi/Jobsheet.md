# Jobsheet Pertemuan 03 — Percabangan, Operator Logika, dan Validasi

## Identitas

| Item | Isian |
|---|---|
| Nama |  |
| NIM |  |
| Kelas |  |
| Tanggal |  |
| Link Colab |  |

## Environment

Scratch + Google Colab + Python.

## Tujuan

Mahasiswa mampu menerjemahkan aturan keputusan ke condition, menggunakan `if/elif/else`, operator perbandingan dan logika, membedakan validasi dari rule keputusan, serta menguji normal, boundary, dan invalid input.

## Pola Kerja

```text
TULIS RULE → TENTUKAN CONDITION → TENTUKAN BOUNDARY → PREDIKSI → RUN → BANDINGKAN → PERBAIKI → RETEST
```

---

## P01 — Sistem Nilai

Program utama: `praktikum/python/01_sistem_nilai.py` dan notebook Colab.

Rule:

```text
0–100 adalah domain valid
>=90 → A
>=80 → B
>=75 → C/Lulus
<75  → Belum lulus
```

### Boundary test wajib

| Input | Expected | Actual | Pass |
|---:|---|---|:---:|
| -1 | invalid |  | ☐ |
| 0 | belum lulus |  | ☐ |
| 74 | belum lulus |  | ☐ |
| 75 | C/Lulus |  | ☐ |
| 76 | C/Lulus |  | ☐ |
| 79 | C/Lulus |  | ☐ |
| 80 | B |  | ☐ |
| 89 | B |  | ☐ |
| 90 | A |  | ☐ |
| 100 | A |  | ☐ |
| 101 | invalid |  | ☐ |

### Tracing nilai 85

| Condition | True/False | Dieksekusi? |
|---|:---:|:---:|
| nilai < 0 atau > 100 |  |  |
| nilai >= 90 |  |  |
| nilai >= 80 |  |  |
| nilai >= 75 |  |  |
| else |  |  |

---

## P02 — Tarif Parkir

Program: `praktikum/python/02_tarif_parkir.py`.

Sebelum coding, tulis domain durasi, tarif untuk dua jam pertama, tambahan setelah dua jam, dan boundary 1/2/3 jam.

| Durasi | Expected | Actual | Pass |
|---:|---|---|:---:|
| 0 | invalid |  | ☐ |
| 1 | tarif awal |  | ☐ |
| 2 | tarif awal |  | ☐ |
| 3 | tarif awal + satu tambahan |  | ☐ |
| 5 | tarif awal + tiga tambahan |  | ☐ |

---

## P03 — Seleksi Dua Syarat

Program: `praktikum/python/03_seleksi_wahana.py`.

Rule inti:

```text
memenuhi jika syarat usia DAN syarat tinggi keduanya benar
```

| Usia memenuhi | Tinggi memenuhi | Expected | Actual |
|:---:|:---:|---|---|
| Tidak | Tidak | tidak memenuhi |  |
| Tidak | Ya | tidak memenuhi |  |
| Ya | Tidak | tidak memenuhi |  |
| Ya | Ya | memenuhi |  |

Jelaskan mengapa mengganti `and` menjadi `or` mengubah rule.

---

## P04 — Promo dengan `and` dan `or`

Program: `praktikum/python/04_promo_toko.py`.

1. Tuliskan rule promo yang digunakan program.
2. Buat tabel kombinasi status member dan total transaksi.
3. Uji nilai tepat di boundary.
4. Ubah satu operator logika pada salinan program dan jelaskan perubahan hasil.

---

## P05 — Klasifikasi Suhu

Program: `praktikum/python/05_klasifikasi_suhu.py`.

| Suhu | Expected |
|---:|---|
| 17 | dingin |
| 18 | nyaman |
| 27 | nyaman |
| 28 | panas |

Jelaskan mengapa urutan condition memengaruhi hasil bila interval saling tumpang tindih.

---

## P06 — Keputusan Peminjaman Buku Kelas

Sebagai latihan keputusan multi-syarat, gunakan konteks **peminjaman buku/peralatan kelas, bukan kredit atau layanan keuangan**. Contoh syarat: status anggota aktif dan jumlah item yang sedang dipinjam belum mencapai batas kelas.

Langkah:

1. tulis domain input;
2. tulis rule validasi;
3. tulis rule keputusan dengan kalimat biasa;
4. tentukan `and`, `or`, atau nested condition;
5. buat minimal enam test, termasuk satu syarat gagal secara bergantian.

Bagian ini dibuat sebagai latihan penyusunan rule; mahasiswa harus dapat menjelaskan setiap condition.

---

## Scratch ↔ Python

Buka `praktikum/scratch/README.md`. Buat satu versi Scratch dari sistem nilai atau seleksi dua syarat, lalu bandingkan:

| Konsep | Scratch | Python |
|---|---|---|
| keputusan | `if`, `if else` | `if`, `elif`, `else` |
| perbandingan | blok operator | `>=`, `<=`, `==`, dll. |
| logika | `and`, `or`, `not` block | `and`, `or`, `not` |
| nesting | blok di dalam blok | indentasi |

## Debug Challenge

Pada salinan program ubah satu hal per eksperimen:

- `>=` menjadi `>`;
- urutan condition grade ditukar;
- `and` menjadi `or`;
- satu indentasi digeser.

Catat:

```text
Input:
Expected:
Actual:
Condition yang dievaluasi:
Bukti:
Penyebab:
Perubahan:
Retest boundary:
```

## Pertanyaan Analisis

1. Mengapa urutan condition pada sistem grade penting?
2. Apa akibat `>= 75` diganti `> 75`?
3. Kapan memakai `and` dan kapan `or`?
4. Apa beda validasi input dan rule keputusan?
5. Mengapa boundary test penting?
6. Bagaimana indentasi menentukan blok program?
7. Mengapa condition yang terlalu umum di atas dapat membuat cabang bawah tidak pernah tercapai?

## Deliverable

- source program yang dijalankan;
- notebook Colab;
- satu versi Scratch;
- tabel test minimal enam kasus untuk program utama;
- minimal dua catatan perbaikan condition;
- satu rule baru dan dua regression test;
- kesimpulan.

## Checklist

- [ ] P01 diuji lengkap.
- [ ] P02 boundary 1/2/3 diuji.
- [ ] P03 semua kombinasi `and` diuji.
- [ ] P04 kombinasi member/transaksi diuji.
- [ ] P05 boundary suhu diuji.
- [ ] P06 rule konteks buku/peralatan ditulis dan diuji.
- [ ] Scratch dibandingkan dengan Python.
- [ ] Minimal dua kesalahan sengaja diperbaiki dan diretest.
