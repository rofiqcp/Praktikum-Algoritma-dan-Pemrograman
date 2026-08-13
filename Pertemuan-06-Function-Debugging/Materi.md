# Materi Pertemuan 06 — Scratch + Python Google Colab V: Function, Dekomposisi, dan Debugging

> Sumber utama: buku panduan 16 pertemuan, Edisi Agustus 2026. Contoh runnable ada di `praktikum/`.

Sesi terakhir fase Scratch–Colab mengubah peserta dari “menulis langkah panjang” menjadi “memecah program menjadi bagian yang dapat digunakan kembali”.

## Target Kompetensi
- Memecah masalah menjadi submasalah.
- Menggunakan My Blocks Scratch dan function Python.
- Mengerti parameter dan return value.
- Melakukan debugging sistematis menggunakan bukti.

## Output
- Program modular versi Scratch dan Python.
- Checklist debugging pribadi.

## Alur 180 Menit
| Tahap | Durasi | Aktivitas |
|---|---:|---|
| Review | 15 | List dan loop |
| Dekomposisi | 20 | Pecah fitur menjadi fungsi |
| My Blocks | 25 | Custom block Scratch |
| Function Python | 35 | `def`, parameter, return |
| Praktik | 45 | Menu program modular |
| Debug lab | 25 | Bug hunt sengaja |
| Refleksi | 15 | Siap pindah ke VS Code |

## 6.1 Dekomposisi
```text
MASALAH BESAR → FITUR → FUNGSI KECIL → TEST PER FUNGSI → INTEGRASI
```
Contoh aplikasi nilai dapat dipecah menjadi: baca input, validasi nilai, hitung rata-rata, tentukan grade, dan tampilkan laporan.

## 6.2 Function Python
```python
def hitung_total(harga, jumlah):
    return harga * jumlah

def format_rupiah(nilai):
    return f"Rp{nilai:,.0f}"
```

## 6.3 Parameter vs Return
| Istilah | Analogi | Contoh |
|---|---|---|
| Parameter | Bahan yang diberikan ke mesin | `harga`, `jumlah` |
| Return value | Hasil yang dikembalikan | `total` |
| Function call | Menyalakan mesin | `hitung_total(10000,3)` |

## 6.4 Debugging sebagai Proses
1. **Reproduce:** bug dapat diulang.
2. **Read:** baca error paling spesifik/terakhir.
3. **Locate:** tentukan file/baris/fungsi/blok.
4. **Hypothesize:** tulis dugaan sebelum mengubah.
5. **Test small:** uji fungsi/data kecil.
6. **Change one thing:** satu perubahan.
7. **Retest:** kasus gagal + regression.
8. **Document:** catat penyebab dan solusi.

## 6.5 Bug Hunt
```python
def rata_rata(data):
    total = 0
    for nilai in data:
        total = nilai  # BUG: harus akumulasi
    return total / len(data)
```
Jangan langsung memperbaiki. Buat tracing `total` per iterasi dan buktikan root cause.

## Troubleshooting
| Gejala | Penyebab | Perbaikan |
|---|---|---|
| Function menghasilkan `None` | Tidak ada `return` pada jalur yang perlu | Cek semua jalur |
| Variable tidak dikenali | Scope lokal vs global | Kirim data lewat parameter |
| Function terlalu panjang | Terlalu banyak tanggung jawab | Pisahkan satu tujuan per fungsi |
| Bug setelah refactor | Perilaku berubah tanpa test | Bandingkan input-output sebelum/sesudah |
