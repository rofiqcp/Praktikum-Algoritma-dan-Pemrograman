# Materi Pertemuan 06 — Scratch + Python Google Colab V: Function, Dekomposisi, dan Debugging

> Sumber utama: buku panduan 16 pertemuan, Edisi Agustus 2026. Seluruh contoh runnable berada di folder `praktikum/`.

Pertemuan ini adalah sesi terakhir fase Scratch–Colab. Fokusnya mengubah kebiasaan dari menulis satu rangkaian langkah panjang menjadi memecah program menjadi bagian kecil yang dapat dipanggil kembali, diuji secara terpisah, dan digabungkan menjadi program utuh.

## Target Kompetensi

Mahasiswa mampu:

- memecah masalah menjadi submasalah;
- menggunakan My Blocks Scratch;
- membuat function Python dengan `def`;
- membedakan parameter, argument, function call, dan return value;
- membedakan `print()` dengan `return`;
- memahami scope lokal secara dasar;
- membuat function dengan satu tanggung jawab utama;
- menguji function kecil sebelum integrasi;
- melakukan debugging secara sistematis menggunakan bukti;
- melakukan refactor lalu memastikan perilaku lama tetap benar.

## Output

1. Program modular versi Scratch.
2. Program modular versi Python/Colab.
3. Menu program berbasis beberapa function.
4. Tracing table satu kasus bug.
5. Hasil unit test sederhana.
6. Checklist debugging pribadi.

---

# 6.1 Mental Model Dekomposisi

```text
MASALAH BESAR → FITUR → FUNGSI KECIL → TEST PER FUNGSI → INTEGRASI
```

Contoh aplikasi nilai dapat dipecah menjadi:

```text
baca input
validasi nilai
hitung rata-rata
tentukan grade
tampilkan laporan
```

Keuntungannya: satu bagian dapat diuji tanpa menjalankan seluruh aplikasi, kode lebih mudah dibaca, dan logic tidak perlu diulang.

---

# 6.2 Function Python

```python
def hitung_total(harga, jumlah):
    return harga * jumlah


def format_rupiah(nilai):
    return f"Rp{nilai:,.0f}"
```

Function belum berjalan hanya karena sudah didefinisikan. Function perlu dipanggil:

```python
total = hitung_total(10000, 3)
print(format_rupiah(total))
```

## Anatomi

| Istilah | Makna | Contoh |
|---|---|---|
| Function | blok kode bernama | `hitung_total` |
| Parameter | nama input pada definisi | `harga`, `jumlah` |
| Argument | nilai aktual saat dipanggil | `10000`, `3` |
| Return value | hasil yang dikirim kembali | `30000` |
| Function call | pemanggilan function | `hitung_total(10000, 3)` |

---

# 6.3 `print()` vs `return`

```python
def salam(nama):
    print("Halo", nama)
```

Function tersebut menampilkan output langsung.

Bandingkan:

```python
def buat_salam(nama):
    return "Halo " + nama

pesan = buat_salam("Ayu")
print(pesan)
```

`return` membuat hasil function dapat dipakai lagi oleh bagian program lain.

---

# 6.4 My Blocks Scratch

Pada Scratch, ide function diperkenalkan menggunakan **My Blocks**. Buat custom block seperti:

```text
hitung total (harga) (jumlah)
```

Bandingkan konsep:

| Scratch | Python |
|---|---|
| My Blocks | function |
| input pada block | parameter |
| memanggil block | function call |
| variable hasil | return value/pengembalian hasil |

Tujuan My Blocks bukan sekadar membuat script pendek, tetapi memisahkan satu tugas agar dapat digunakan kembali.

---

# 6.5 Satu Function, Satu Tujuan Utama

Contoh struktur yang lebih baik:

```python
def validasi_nilai(nilai):
    return 0 <= nilai <= 100


def hitung_rata_rata(data):
    if len(data) == 0:
        return None
    return sum(data) / len(data)


def tentukan_status(nilai):
    if nilai >= 75:
        return "Lulus"
    return "Belum lulus"
```

Jika sebuah function membaca semua input, memvalidasi, menghitung, mengubah data, dan mencetak seluruh laporan sekaligus, function tersebut terlalu banyak tanggung jawab.

---

# 6.6 Scope Lokal

Variable di dalam function umumnya bersifat lokal. Pada tahap ini, biasakan mengirim data melalui parameter dan mengembalikan hasil melalui `return`.

```python
def tambah_stok(stok, jumlah):
    return stok + jumlah
```

Pola ini lebih mudah diuji dibanding function yang bergantung pada banyak global variable.

---

# 6.7 Program Menu Modular

Mental model:

```text
main
├── tampilkan_menu
├── tambah_data
├── tampilkan_data
├── cari_data
└── hitung_ringkasan
```

`main()` bertugas mengatur alur, sedangkan function lain menyelesaikan pekerjaan kecil yang jelas.

---

# 6.8 Debugging sebagai Proses

Gunakan urutan dari buku panduan:

```text
REPRODUCE → READ → LOCATE → HYPOTHESIZE → TEST SMALL
→ CHANGE ONE THING → RETEST → DOCUMENT
```

1. **Reproduce** — pastikan masalah dapat diulang dengan langkah yang jelas.
2. **Read** — baca pesan error atau output yang tidak sesuai.
3. **Locate** — tentukan function/baris yang terlibat.
4. **Hypothesize** — tulis dugaan sebelum mengubah source.
5. **Test small** — uji function dengan data kecil.
6. **Change one thing** — ubah satu hal agar efek perubahan dapat diketahui.
7. **Retest** — jalankan kasus gagal dan kasus lama yang sudah benar.
8. **Document** — catat penyebab dan solusi.

---

# 6.9 Bug Hunt dan Tracing

Contoh dari buku:

```python
def rata_rata(data):
    total = 0
    for nilai in data:
        total = nilai
    return total / len(data)
```

Buat tracing table:

| Iterasi | nilai | total sebelum | total sesudah |
|---:|---:|---:|---:|
| 1 | 80 | 0 | 80 |
| 2 | 90 | 80 | 90 |
| 3 | 70 | 90 | 70 |

Terlihat bahwa `total` selalu diganti. Jika tujuan program adalah akumulasi, operasi yang diperlukan adalah penambahan ke total.

---

# 6.10 Refactoring

Refactoring adalah memperbaiki struktur internal tanpa sengaja mengubah perilaku program yang sudah benar. Setelah memecah kode menjadi function, lakukan regression test dengan input yang sama seperti sebelum refactor.

## Contoh test sederhana

```python
def hitung_total(harga, jumlah):
    return harga * jumlah

assert hitung_total(10000, 3) == 30000
assert hitung_total(0, 3) == 0
```

---

# 6.11 Praktikum Wajib

Jalankan seluruh contoh:

```text
praktikum/python/01_kalkulator_modular.py
praktikum/python/02_sistem_nilai_modular.py
praktikum/python/03_menu_modular.py
praktikum/python/04_bug_hunt.py
praktikum/python/program_modular.py
praktikum/colab/latihan_pertemuan06.ipynb
praktikum/colab/program_modular.ipynb
praktikum/tests/test_functions.py
```

Scratch dikerjakan melalui `praktikum/scratch/README.md`.

---

# 6.12 Masalah Umum

| Gejala | Kemungkinan penyebab | Pemeriksaan |
|---|---|---|
| function menghasilkan `None` | jalur tidak mengembalikan nilai | periksa seluruh jalur `return` |
| variable tidak dikenali | scope lokal/global | kirim data melalui parameter |
| hasil salah setelah loop | operasi state tidak sesuai | buat tracing table |
| function terlalu panjang | terlalu banyak tanggung jawab | pecah menjadi function kecil |
| hasil berubah setelah refactor | perilaku tidak diuji ulang | jalankan regression test |

## Checklist Function

- [ ] Nama function menjelaskan tujuan.
- [ ] Parameter jelas.
- [ ] Return value jelas bila dibutuhkan.
- [ ] Function mempunyai satu tanggung jawab utama.
- [ ] Function dapat diuji secara terpisah.
- [ ] Tidak bergantung pada global variable tanpa alasan.
- [ ] Tidak ada duplikasi logic berlebihan.

## Exit Ticket

- [ ] Saya dapat memecah masalah menjadi minimal empat function.
- [ ] Saya memahami parameter, argument, dan return.
- [ ] Saya tahu beda `print()` dan `return`.
- [ ] Saya dapat membuat My Blocks Scratch.
- [ ] Saya dapat menguji function kecil.
- [ ] Saya menggunakan debugging sistematis, bukan menebak.
- [ ] Saya siap menjalankan project secara lokal pada Pertemuan 07.
