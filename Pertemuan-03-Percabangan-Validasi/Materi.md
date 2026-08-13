# Materi Pertemuan 03 — Scratch + Python Google Colab II: Percabangan, Operator Logika, dan Validasi

> Sumber utama: buku panduan 16 pertemuan, Edisi Agustus 2026. Contoh runnable ada di `praktikum/`.

Fokus sesi ini adalah membuat program yang dapat mengambil keputusan berdasarkan data.

## Target Kompetensi
- Membedakan `if`, `if-else`, dan `if-elif-else`.
- Menggunakan operator perbandingan dan logika.
- Membuat validasi input sederhana.
- Menerjemahkan nested if Scratch ke struktur Python yang terbaca.

## Output
- Program penentuan kategori/kelulusan versi Scratch dan Python.
- Tabel uji minimal enam kasus.

## Alur 180 Menit
| Tahap | Durasi | Aktivitas |
|---|---:|---|
| Review | 15 | Tipe data, input, output |
| Condition visual | 25 | if dan if-else di Scratch |
| Operator | 25 | `> < >= <= == !=`, `and`, `or`, `not` |
| Python branching | 35 | `if/elif/else` dan indentasi |
| Praktik | 45 | Sistem nilai/tarif |
| Test cases | 20 | Boundary dan invalid input |
| Debug | 15 | IndentationError dan condition salah |

## 3.1 Cara Berpikir Kondisi
Sebelum menulis `if`, tulis kalimat: **Jika kondisi X benar, lakukan A; jika tidak, lakukan B.** Tentukan data tepat di batas.

| Tujuan | Condition | Data batas |
|---|---|---|
| Lulus | `nilai >= 75` | 74, 75, 76 |
| Diskon member | `member == True` | True, False |
| Usia tiket anak | `usia < 12` | 11, 12 |
| Grade A | `nilai >= 90` | 89, 90, 100 |

## 3.2 Sistem Nilai
```python
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

## 3.3 Latihan
- Tarif parkir.
- Seleksi wahana usia + tinggi.
- Promo toko member + transaksi.
- Klasifikasi suhu.
- Kelayakan peminjaman.

## 3.4 Pengujian
Uji normal, boundary, dan tidak valid. Kesalahan paling umum adalah operator batas salah, misalnya `> 75` sehingga nilai 75 gagal.

## Troubleshooting
| Gejala | Penyebab | Perbaikan |
|---|---|---|
| `IndentationError` | Blok tidak konsisten | 4 spasi per level |
| Semua masuk cabang pertama | Kondisi terlalu umum di atas | Kondisi spesifik/tinggi lebih dulu |
| Boundary salah | `>` vs `>=` | Uji nilai tepat di batas |
| `and/or` membingungkan | Kalimat logika belum jelas | Tulis syarat dalam bahasa biasa |
