# Jobsheet Pertemuan 01 — Scratch: Belajar Berpikir seperti Programmer

## Identitas Praktikum

| Item | Isian |
|---|---|
| Nama |  |
| NIM |  |
| Kelas |  |
| Tanggal |  |
| Repository/Folder |  |

## Tujuan

Setelah praktikum, mahasiswa harus mampu menjelaskan konsep utama pertemuan, menjalankan seluruh contoh program, memodifikasi program secara mandiri, membuat test case, dan mendokumentasikan proses debugging.

## Environment

**Scratch Web (`https://scratch.mit.edu/`)**

## Persiapan

- Buat akun/masuk Scratch jika ingin menyimpan project.
- Buka `praktikum/README.md` dan siapkan sprite Pemain dan Koin.
- Aktifkan monitor variable `skor` agar perubahan state terlihat.

## Pola Kerja Wajib

```text
PREDIKSI → JALANKAN → AMATI → CATAT → UBAH SATU HAL → UJI ULANG → SIMPULKAN
```

## Daftar Percobaan Wajib

| No | Percobaan | Aktivitas |
|---:|---|---|
| 1 | **P01 — Sequence & Event** | Rakit gerak awal sprite menggunakan `when green flag clicked`, lalu event panah kiri/kanan. Prediksi posisi sebelum menjalankan. |
| 2 | **P02 — Variable & Input** | Buat variable `skor`, `target`, dan satu input pengguna dengan `ask ... and wait`. |
| 3 | **P03 — Condition & Loop** | Gunakan `forever` + `if touching` untuk collision koin. |
| 4 | **P04 — Game Tangkap Koin** | Integrasikan gerak, skor, random position, suara, target menang, dan `stop all`. |
| 5 | **P05 — Debug Challenge** | Sengaja buat event/condition salah, catat gejala, reproduksi, lalu perbaiki satu perubahan. |

## Cara Menjalankan

Jalankan dengan **Green Flag**. Untuk setiap perubahan, klik Stop lalu Green Flag kembali agar state awal dapat diuji.

## Tabel Pengujian Wajib

| No | Kasus Uji | Expected | Actual | Pass |
|---:|---|---|---|:---:|
| 1 | Pemain merespons panah kiri/kanan |  |  | ☐ |
| 2 | Skor mulai dari 0 pada setiap Green Flag |  |  | ☐ |
| 3 | Skor bertambah tepat 1 per koin |  |  | ☐ |
| 4 | Koin berpindah setelah collision |  |  | ☐ |
| 5 | Game berhenti saat target tercapai |  |  | ☐ |

Tambahkan minimal dua test case buatan sendiri.

## Log Debugging

| Waktu/Step | Gejala | Bukti/Error | Hipotesis | Perubahan | Hasil Retest |
|---|---|---|---|---|---|
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |

## Pertanyaan Analisis

1. Apa beda sequence dan event pada game?
2. Mengapa pemeriksaan collision perlu loop?
3. State apa saja yang disimpan variable?
4. Bagaimana membuktikan bug berasal dari event, condition, atau variable?

## Challenge Mandiri

Tambahkan satu fitur yang mengubah alur program, buat dua test case, lalu pastikan fitur lama tetap bekerja.

## Bukti yang Dikumpulkan

- Screenshot/rekaman program benar-benar dijalankan.
- Source/project hasil perubahan sendiri.
- Tabel expected vs actual.
- Minimal tiga catatan debugging.
- Jawaban analisis dan kesimpulan.

## Checklist Selesai

- [ ] Semua program wajib sudah dijalankan.
- [ ] Semua test utama memiliki expected dan actual.
- [ ] Saya dapat menjelaskan alur tanpa membaca blok satu per satu.
- [ ] Saya melakukan minimal satu modifikasi mandiri.
- [ ] Saya mempunyai bukti error dan retest.
