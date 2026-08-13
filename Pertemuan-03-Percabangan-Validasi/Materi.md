# Materi Pertemuan 03 — Scratch + Python Google Colab II: Percabangan, Operator Logika, dan Validasi

> **Sumber utama:** *Buku Panduan Praktik: Pemrograman Dasar hingga Full Stack — 16 Pertemuan Terstruktur, Edisi Agustus 2026*.
>
> Fokus pertemuan ini adalah membuat program **mengambil keputusan berdasarkan data**. Materi function belum menjadi fokus; contoh inti ditulis sebagai alur `input → condition → output` agar perhatian mahasiswa berada pada aturan keputusan, urutan kondisi, boundary, dan validasi.

## Target Kompetensi

Mahasiswa mampu:

- membedakan `if`, `if-else`, dan `if-elif-else`;
- menggunakan operator perbandingan `>`, `<`, `>=`, `<=`, `==`, `!=`;
- menggunakan operator logika `and`, `or`, `not`;
- membuat validasi input sederhana;
- menerjemahkan nested `if` Scratch ke struktur Python yang terbaca;
- membuat test normal, boundary, dan invalid.

## Output Pertemuan

1. Program penentuan kategori/kelulusan versi Scratch dan Python.
2. Tabel uji minimal enam kasus.
3. Beberapa program keputusan dari soal cerita.
4. Catatan minimal dua kesalahan condition dan hasil retest.

## Alur 180 Menit

| Tahap | Durasi | Aktivitas |
|---|---:|---|
| Review | 15 menit | tipe data, input, output |
| Condition visual | 25 menit | `if` dan `if-else` di Scratch |
| Operator | 25 menit | perbandingan, `and`, `or`, `not` |
| Python branching | 35 menit | `if/elif/else` dan indentasi |
| Praktik | 45 menit | sistem nilai dan aturan keputusan |
| Test cases | 20 menit | normal, boundary, invalid |
| Debug | 15 menit | indentation dan condition salah |

---

## 1. Mental Model Keputusan

Sebelum menulis `if`, tulis aturan dengan kalimat biasa:

```text
JIKA kondisi X benar
    lakukan A
JIKA TIDAK
    lakukan B
```

Contoh kelulusan:

```text
Jika nilai minimal 75, status lulus.
Jika nilai di bawah 75, status belum lulus.
```

Setelah aturan jelas, tentukan nilai tepat di batas. Untuk `nilai >= 75`, data penting adalah `74`, `75`, dan `76`.

## 2. Boolean dan Condition

Condition harus dapat dievaluasi menjadi `True` atau `False`.

```python
nilai = 80
print(nilai >= 75)   # True
print(nilai < 75)    # False
```

### Operator perbandingan

| Operator | Makna | Contoh |
|---|---|---|
| `>` | lebih besar | `usia > 17` |
| `<` | lebih kecil | `usia < 12` |
| `>=` | lebih besar atau sama | `nilai >= 75` |
| `<=` | lebih kecil atau sama | `stok <= 5` |
| `==` | sama dengan | `pilihan == "y"` |
| `!=` | tidak sama dengan | `status != "selesai"` |

**Penting:** `=` adalah assignment, sedangkan `==` adalah perbandingan.

---

## 3. `if`

Gunakan `if` jika aksi hanya perlu dilakukan saat condition benar.

```python
nilai = float(input("Nilai: "))

if nilai >= 75:
    print("Lulus")
```

Jika condition false, isi blok tidak dijalankan.

## 4. `if-else`

Gunakan bila ada dua jalur yang saling melengkapi.

```python
nilai = float(input("Nilai: "))

if nilai >= 75:
    print("Lulus")
else:
    print("Belum lulus")
```

## 5. `if-elif-else`

Gunakan bila terdapat beberapa kategori yang saling eksklusif.

```python
nilai = float(input("Nilai akhir: "))

if nilai < 0 or nilai > 100:
    print("Nilai tidak valid")
elif nilai >= 90:
    print("A")
elif nilai >= 80:
    print("B")
elif nilai >= 75:
    print("C / Lulus")
else:
    print("Belum lulus")
```

Urutan kondisi penting. Jika `nilai >= 75` ditempatkan sebelum `nilai >= 90`, nilai 95 akan berhenti pada cabang 75 dan kategori A tidak pernah tercapai.

---

## 6. Indentasi Python

Python menggunakan indentasi untuk menandai blok.

Benar:

```python
if nilai >= 75:
    print("Lulus")
    print("Selamat")
print("Program selesai")
```

Baris terakhir tidak lagi berada dalam `if`.

Kesalahan indentasi dapat menghasilkan `IndentationError` atau menghasilkan alur yang berbeda dari yang dimaksud.

---

## 7. Operator Logika

### `and`

Semua condition harus true.

```python
usia >= 10 and tinggi_cm >= 130
```

### `or`

Cukup salah satu condition true.

```python
nilai < 0 or nilai > 100
```

### `not`

Membalik nilai boolean.

```python
not aktif
```

### Tabel kebenaran singkat

| A | B | `A and B` | `A or B` |
|:---:|:---:|:---:|:---:|
| F | F | F | F |
| F | T | F | T |
| T | F | F | T |
| T | T | T | T |

Sebelum menggabungkan condition, tuliskan syarat dalam bahasa biasa agar operator logika tidak dipilih hanya berdasarkan tebakan.

---

## 8. Validasi vs Business Rule

**Validasi** memeriksa apakah data masuk berada pada domain yang diperbolehkan.

```python
if nilai < 0 or nilai > 100:
    print("Nilai tidak valid")
```

**Business rule** menentukan keputusan setelah data valid.

```python
elif nilai >= 75:
    print("Lulus")
```

Pemisahan mental ini membantu mahasiswa memahami mengapa input dapat “valid” tetapi hasil keputusannya tetap “tidak memenuhi syarat”.

---

## 9. Boundary Value

Boundary adalah nilai tepat di sekitar perubahan rule.

| Rule | Bawah batas | Tepat batas | Atas batas |
|---|---:|---:|---:|
| `nilai >= 75` | 74 | 75 | 76 |
| `nilai >= 90` | 89 | 90 | 91 |
| `usia < 12` | 11 | 12 | 13 |
| `tinggi >= 130` | 129 | 130 | 131 |

Kesalahan `>` dan `>=` sering tidak terlihat bila hanya menguji nilai yang jauh dari batas.

---

## 10. Praktik 1 — Sistem Nilai

Program inti tersedia di `praktikum/python/01_sistem_nilai.py`.

Uji minimal:

- `-1` → invalid;
- `0` → valid, belum lulus;
- `74` → belum lulus;
- `75` → lulus;
- `76` → lulus;
- `89` dan `90` → pergantian grade;
- `100` → A;
- `101` → invalid.

## 11. Praktik 2 — Tarif Parkir

Soal cerita: ada tarif awal untuk dua jam pertama dan tarif tambahan setelahnya. Sebelum menulis Python, mahasiswa harus menuliskan rule secara eksplisit.

Fokus:

- validasi durasi;
- boundary 1, 2, 3 jam;
- perhitungan tambahan hanya bila durasi melewati batas.

## 12. Praktik 3 — Seleksi Wahana

Rule contoh:

```text
Boleh masuk jika usia minimal 10 DAN tinggi minimal 130 cm.
```

Uji kombinasi:

| Usia memenuhi | Tinggi memenuhi | Expected |
|:---:|:---:|---|
| Tidak | Tidak | tidak memenuhi |
| Tidak | Ya | tidak memenuhi |
| Ya | Tidak | tidak memenuhi |
| Ya | Ya | memenuhi |

## 13. Praktik 4 — Promo Toko

Gunakan data status member dan total transaksi untuk membandingkan efek `and` dan `or`. Jangan menulis rule sebelum aturan promosi dinyatakan jelas dalam kalimat.

## 14. Praktik 5 — Klasifikasi Suhu

Contoh kategori:

```text
suhu < 18        → dingin
18 <= suhu <= 27 → nyaman
suhu > 27        → panas
```

Uji `17`, `18`, `27`, `28`.

## 15. Praktik 6 — Kelayakan Peminjaman

Gunakan beberapa syarat seperti usia, status anggota, dan jumlah pinjaman aktif. Tujuan latihan bukan domain pinjamannya, tetapi kemampuan menerjemahkan beberapa syarat menjadi condition yang jelas dan dapat diuji.

---

## 16. Scratch ↔ Python

Scratch sering memakai nested `if` untuk beberapa keputusan. Python dapat memakai `if/elif/else` jika kategori bersifat berurutan dan saling eksklusif.

Saat menerjemahkan:

1. tulis rule dalam kalimat;
2. buat daftar condition;
3. tentukan urutan condition;
4. tentukan boundary;
5. baru susun blok Scratch/Python.

---

## 17. Troubleshooting

| Gejala | Kemungkinan penyebab | Pemeriksaan |
|---|---|---|
| `IndentationError` | blok tidak konsisten | gunakan 4 spasi per level |
| Semua masuk cabang pertama | condition terlalu umum diletakkan di atas | cek urutan condition |
| Nilai tepat batas salah | `>` tertukar `>=` | uji nilai boundary |
| `and/or` membingungkan | rule belum ditulis jelas | buat tabel kombinasi True/False |
| Input valid dianggap invalid | validasi domain salah | cek batas minimum/maksimum |
| Cabang terakhir tidak pernah tercapai | condition sebelumnya sudah mencakup semua nilai | tracing dari atas ke bawah |

## 18. Debugging dengan Tracing

Untuk satu input, baca condition dari atas ke bawah dan tulis hasilnya.

Contoh `nilai=85`:

| Condition | Hasil |
|---|:---:|
| `<0 or >100` | False |
| `>=90` | False |
| `>=80` | True → stop di cabang ini |
| `>=75` | tidak diperiksa lagi |

Tracing membuat urutan keputusan terlihat tanpa menebak.

## 19. Rangkuman

- `if` membuat keputusan.
- `elif` menambah alternatif condition.
- `else` menangani sisa kasus.
- urutan condition memengaruhi hasil;
- boundary test wajib untuk rule `>`, `<`, `>=`, `<=`;
- validasi memeriksa domain input, sedangkan business rule menentukan hasil keputusan;
- `and`, `or`, `not` harus berasal dari rule yang jelas.

## Exit Ticket

- [ ] Saya dapat membedakan `if`, `elif`, `else`.
- [ ] Saya dapat menjelaskan `=` dan `==`.
- [ ] Saya dapat membuat test 74/75/76 untuk rule `>=75`.
- [ ] Saya dapat menjelaskan kapan memakai `and` dan `or`.
- [ ] Saya dapat membedakan validasi dan rule keputusan.
- [ ] Saya dapat melakukan tracing condition dari atas ke bawah.
