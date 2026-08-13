# Jobsheet Pertemuan 08 — Project Checkpoint 1

## Identitas Project

| Item | Isian |
|---|---|
| Nama |  |
| NIM |  |
| Kelas |  |
| Project pilihan |  |
| Link repository |  |
| Tanggal demo |  |

## Tujuan

Checkpoint ini mengukur kemampuan mengintegrasikan kompetensi Pertemuan 01–07 menjadi satu program CLI Python lokal yang modular, dapat diuji, terdokumentasi, dan mempunyai Git history yang menunjukkan progres.

## Batasan

Project menggunakan algoritma, Python dasar, condition, loop, list/dictionary sederhana, function, validasi, VS Code, terminal, Git, dan GitHub. Web, API, Node.js, database, serta deployment belum menjadi kebutuhan checkpoint ini.

---

# Tahap 1 — Pilih dan Pahami Soal

1. Pilih tepat satu project dari `Project.md`.
2. Salin nama project ke identitas jobsheet.
3. Tulis masalah dalam 2–4 kalimat menggunakan bahasa sendiri.
4. Identifikasi pengguna program.
5. Jangan mulai coding sebelum requirement minimum selesai ditulis.

### Ringkasan masalah

```text
Masalah:
Pengguna:
Tujuan program:
Batasan:
```

---

# Tahap 2 — Requirement

Pecah soal menjadi requirement yang dapat diuji.

| ID | Requirement | Input/trigger | Expected result |
|---|---|---|---|
| R01 |  |  |  |
| R02 |  |  |  |
| R03 |  |  |  |
| R04 |  |  |  |
| R05 |  |  |  |
| R06 |  |  |  |

Pastikan minimal ada empat operasi menu dan aturan validasi sesuai soal.

---

# Tahap 3 — Input, Process, Output, dan State

Isi rancangan berikut.

### Input
```text
1.
2.
3.
```

### Process
```text
1.
2.
3.
```

### Output
```text
1.
2.
3.
```

### State/Data yang disimpan selama program berjalan
```text
1.
2.
```

---

# Tahap 4 — Rancang Struktur Data

Tentukan list/dictionary yang diperlukan.

| Nama variable | Tipe | Contoh isi | Alasan |
|---|---|---|---|
|  | list/dict |  |  |
|  |  |  |  |

Tuliskan aturan data, misalnya nilai 0–100, stok tidak negatif, nama tidak kosong, atau kapasitas maksimum sesuai project.

---

# Tahap 5 — Function Plan

Buku mewajibkan minimal lima function bermakna.

| Function | Parameter | Return/output | Tanggung jawab |
|---|---|---|---|
| 1. |  |  |  |
| 2. |  |  |  |
| 3. |  |  |  |
| 4. |  |  |  |
| 5. |  |  |  |

Periksa agar satu function tidak mengerjakan seluruh aplikasi.

---

# Tahap 6 — Flowchart/Pseudocode

Buat flowchart menu utama dan minimal satu flow untuk operasi terpenting.

Pseudocode dasar:

```text
START
inisialisasi data
REPEAT
    tampilkan menu
    baca pilihan
    IF pilihan operasi 1
        jalankan operasi 1
    ELSE IF pilihan operasi 2
        jalankan operasi 2
    ELSE IF pilihan operasi 3
        jalankan operasi 3
    ELSE IF pilihan operasi 4
        jalankan operasi 4
    ELSE IF pilihan keluar
        selesai
    ELSE
        tampilkan pilihan tidak valid
UNTIL selesai
END
```

---

# Tahap 7 — Implementasi Bertahap

Gunakan VS Code dan terminal lokal. Setelah satu bagian stabil, buat commit.

Contoh rencana commit:

```text
1. chore: siapkan struktur project
2. feat: tambah data awal dan menu utama
3. feat: tambah operasi inti
4. feat: tambah validasi input
5. fix: perbaiki boundary dan data tidak ditemukan
6. test: lengkapi test case
7. docs: lengkapi README
```

Buku mewajibkan minimal lima commit progres nyata.

### Log commit

| No | Commit/message | Perubahan yang stabil |
|---:|---|---|
| 1 |  |  |
| 2 |  |  |
| 3 |  |  |
| 4 |  |  |
| 5 |  |  |

---

# Tahap 8 — Testing Minimum

Buat minimal delapan test case.

| ID | Req | Precondition/Input | Expected | Actual | Pass |
|---|---|---|---|---|:---:|
| T01 |  |  |  |  | ☐ |
| T02 |  |  |  |  | ☐ |
| T03 |  |  |  |  | ☐ |
| T04 |  |  |  |  | ☐ |
| T05 |  |  |  |  | ☐ |
| T06 |  |  |  |  | ☐ |
| T07 |  |  |  |  | ☐ |
| T08 |  |  |  |  | ☐ |

Wajib mencakup kategori yang relevan:

- normal;
- boundary;
- input salah;
- data tidak ditemukan;
- duplikat bila relevan;
- kapasitas/stok tidak cukup bila relevan.

Setelah memperbaiki satu kasus, jalankan kembali kasus lama yang sebelumnya pass.

---

# Tahap 9 — Review Kualitas

Periksa source:

- [ ] Nama variable menjelaskan isi.
- [ ] Nama function menjelaskan tugas.
- [ ] Minimal lima function bermakna.
- [ ] Tidak ada satu function raksasa untuk semua logic.
- [ ] Tidak ada duplikasi logic berlebihan.
- [ ] List/dictionary dipakai sesuai kebutuhan.
- [ ] Input divalidasi sesuai aturan soal.
- [ ] Pesan untuk input salah mudah dipahami.
- [ ] Menu memiliki minimal empat operasi.
- [ ] Program dapat kembali ke menu setelah operasi selesai.

---

# Tahap 10 — README

README minimal memuat:

1. judul project;
2. deskripsi masalah;
3. fitur;
4. kebutuhan environment;
5. struktur file;
6. cara menjalankan;
7. contoh penggunaan;
8. ringkasan struktur data/function;
9. pengujian;
10. batasan program.

Orang lain harus dapat menjalankan program dengan mengikuti README tanpa penjelasan lisan dari pembuat.

---

# Tahap 11 — Demo 3–5 Menit

Urutan demo yang disarankan:

```text
00:00–00:30  masalah dan tujuan
00:30–01:00  struktur data/function
01:00–02:30  alur normal
02:30–03:30  boundary/invalid/not-found
03:30–04:15  Git history + testing
04:15–05:00  kesimpulan
```

---

# Rubrik Penilaian

| Aspek | Bobot |
|---|---:|
| Analisis soal & flowchart | 15% |
| Fitur berjalan | 30% |
| Struktur function/data | 15% |
| Validasi & error handling | 15% |
| Testing | 10% |
| Git/GitHub & README | 10% |
| Demo & penjelasan | 5% |

---

# Starter untuk Belajar Struktur

```bash
cd praktikum/starter-cli
python main.py
python -m unittest discover -s tests -v
```

Starter hanya menunjukkan pola menu, function, data, dan test. Mahasiswa tetap harus mengembangkan project pilihan sendiri sesuai requirement di `Project.md`.

## Checklist Pengumpulan

- [ ] Source runnable lokal.
- [ ] Requirement selesai.
- [ ] Flowchart/pseudocode selesai.
- [ ] Minimal empat operasi menu.
- [ ] Minimal lima function.
- [ ] Minimal delapan test case.
- [ ] Minimal lima commit progres.
- [ ] README lengkap.
- [ ] Repository dapat diakses pengajar.
- [ ] Demo 3–5 menit siap.
