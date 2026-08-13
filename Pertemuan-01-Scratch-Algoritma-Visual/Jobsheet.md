# Jobsheet Pertemuan 01 — Scratch: Belajar Berpikir seperti Programmer

## Identitas

| Item | Isian |
|---|---|
| Nama |  |
| NIM |  |
| Kelas |  |
| Tanggal |  |
| File Scratch |  |

## Tujuan

Mahasiswa mampu menjelaskan input–process–output, sequence, event, variable, condition, loop, dan sensing; membangun mini game Scratch; menguji expected-versus-actual; dan mendokumentasikan proses debugging.

## Environment dan Persiapan

Pertemuan ini hanya memakai Scratch Web di `https://scratch.mit.edu/`.

1. Buat project baru.
2. Siapkan sprite `Pemain` dan `Koin`.
3. Kenali Stage, Block Palette, Code Area, Costumes, dan Sounds.
4. Simpan project sebagai `P01_NIM_Nama.sb3` bila diminta pengajar.

Gunakan pola kerja berikut pada semua percobaan:

```text
PREDIKSI → RAKIT → JALANKAN → AMATI → CATAT → UBAH SATU HAL → RETEST → SIMPULKAN
```

---

## P01 — Sequence dan Event

Panduan: `praktikum/01_sequence_event.md`.

1. Pada Green Flag, atur pemain ke `(0,-120)`, arah 90, lalu tampilkan `Siap!`.
2. Buat event panah kanan `change x by 10`.
3. Buat event panah kiri `change x by -10`.
4. Prediksi posisi sebelum menekan tombol, kemudian bandingkan dengan actual.

| Aksi | Prediksi | Actual | Pass |
|---|---|---|:---:|
| Green Flag |  |  | ☐ |
| kanan 1× |  |  | ☐ |
| kanan 3× |  |  | ☐ |
| kiri 2× |  |  | ☐ |

**Analisis:** jelaskan mana yang merupakan sequence dan mana yang merupakan event. Apa yang terjadi bila posisi awal tidak di-reset?

---

## P02 — Variable dan Input

Panduan: `praktikum/02_variable_input.md`.

1. Buat variable `nama`, `skor`, `target`.
2. Set `skor=0` dan `target=5` pada Green Flag.
3. Gunakan `ask` dan simpan `answer` ke `nama`.
4. Tampilkan sapaan dengan `join`.
5. Aktifkan monitor variable di Stage.
6. Ubah skor saat eksperimen, lalu Green Flag kembali. Pastikan skor kembali 0.

| Kasus | Expected | Actual | Pass |
|---|---|---|:---:|
| nama normal | sapaan sesuai input |  | ☐ |
| run ulang | skor=0 |  | ☐ |
| target diubah | monitor mengikuti nilai baru |  | ☐ |

**Analisis:** apa perbedaan `answer` dan variable `nama`? Mengapa state awal perlu diinisialisasi?

---

## P03 — Condition, Loop, dan Sensing

Panduan: `praktikum/03_condition_loop.md`.

1. Pada sprite Koin buat `forever`.
2. Di dalamnya tambahkan `if <touching [Pemain]?>`.
3. Pada kondisi true tampilkan pesan singkat.
4. Uji ketika sprite terpisah dan ketika menyentuh.
5. Setelah condition terbukti bekerja, tambahkan perubahan `skor`.

| Kondisi | Expected | Actual | Pass |
|---|---|---|:---:|
| tidak touching | skor tetap |  | ☐ |
| touching | skor bertambah |  | ☐ |
| touching cukup lama | amati frekuensi perubahan skor |  | ☐ |

**Analisis:** mengapa pemeriksaan `touching` perlu berada dalam loop? Apa perbedaan tugas `if` dan `forever`?

---

## P04 — Game Tangkap Koin

Panduan: `praktikum/04_game_tangkap_koin.md`.

Fitur minimum: gerak kiri/kanan, reset `skor`, `target`, `gameAktif`, posisi koin acak, collision, sound feedback, condition menang, broadcast `MENANG`, dan kondisi selesai.

### Urutan verifikasi

1. Gerak pemain.
2. Posisi koin acak.
3. Collision dengan indikator visual.
4. Perubahan skor.
5. Uji `target=1`.
6. Uji target normal.
7. Run ulang setelah game selesai.

| ID | Skenario | Expected | Actual | Pass |
|---|---|---|---|:---:|
| T01 | Green Flag | skor=0, gameAktif=1 |  | ☐ |
| T02 | kanan 1× | posisi x bertambah satu step |  | ☐ |
| T03 | kiri 1× | posisi x berkurang satu step |  | ☐ |
| T04 | tidak touching | skor tetap |  | ☐ |
| T05 | touching sekali | skor +1 dan koin pindah |  | ☐ |
| T06 | skor target-1 | game masih aktif |  | ☐ |
| T07 | skor mencapai target | pesan MENANG dan selesai |  | ☐ |
| T08 | Green Flag setelah selesai | state kembali awal |  | ☐ |

Tambahkan minimal dua test case sendiri.

---

## P05 — Debug Challenge

Panduan: `praktikum/05_debug_challenge.md`.

Buat salinan project yang sudah benar. Ubah **satu bagian pada satu waktu**, reproduce gejala, catat expected dan actual, pasang indikator, tulis hipotesis, lakukan satu perbaikan, lalu retest.

Latihan yang disarankan: event tombol salah, skor tidak di-reset, condition target keliru, collision terhitung berulang, atau kondisi stop ditempatkan terlalu awal.

| Kasus | Reproduce | Expected | Actual | Bukti | Hipotesis | Perbaikan | Retest |
|---|---|---|---|---|---|---|---|
| 1 |  |  |  |  |  |  |  |
| 2 |  |  |  |  |  |  |  |
| 3 |  |  |  |  |  |  |  |

Minimal tiga kasus didokumentasikan lengkap.

---

## Flowchart dan Challenge

Gunakan `praktikum/flowchart.md`. Flowchart harus menunjukkan Green Flag, inisialisasi state, loop, keputusan touching, perubahan skor, keputusan target, dan kondisi akhir.

Untuk challenge, pilih satu pengembangan seperti nyawa, timer, objek pengganggu, atau level. Jelaskan variable/condition baru dan buat dua test baru. Setelah itu ulangi test inti untuk memastikan fitur lama tetap bekerja.

## Pertanyaan Analisis Akhir

1. Jelaskan Game Tangkap Koin sebagai input–process–output.
2. Mengapa event keyboard dan loop collision dapat berada pada script berbeda?
3. Apa perbedaan sequence, event, condition, dan loop pada project?
4. State apa saja yang harus di-reset pada Green Flag?
5. Mengapa satu collision dapat terhitung lebih dari satu kali?
6. Bukti apa yang digunakan untuk memastikan condition benar-benar true?
7. Mengapa satu perubahan per eksperimen mempermudah debugging?

## Bukti yang Dikumpulkan

- file project bila diminta;
- screenshot blok dan Stage;
- flowchart;
- tabel expected-versus-actual;
- minimal tiga catatan debugging;
- challenge dan dua test tambahan;
- kesimpulan 5–8 kalimat.

## Checklist

- [ ] P01 selesai dan diuji.
- [ ] P02 selesai dan diuji.
- [ ] P03 selesai dan diuji.
- [ ] P04 game lengkap berjalan.
- [ ] P05 debugging selesai.
- [ ] Flowchart dibuat.
- [ ] Dua test tambahan dibuat.
- [ ] Challenge diuji.
- [ ] Video siap sesuai `TugasVideo.md`.
