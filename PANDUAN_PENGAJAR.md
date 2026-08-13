# Panduan Pengajar

Dokumen ini merangkum pola penggunaan repository berdasarkan buku panduan 16 pertemuan.

## Filosofi
Jangan mengejar banyak syntax dalam satu sesi. Ukur kemajuan dari kemampuan peserta menjelaskan alur program, memprediksi output, memecah masalah, menjalankan pengujian, menemukan letak error, menjaga source dengan Git, dan menggunakan AI sebagai asisten tanpa kehilangan pemahaman. Kode singkat yang dipahami lebih bernilai daripada aplikasi besar hasil copy-paste.

## Alokasi 180 Menit
| Bagian | Waktu | Tujuan |
|---|---:|---|
| Review & apersepsi | 15 | Hubungkan materi sebelumnya |
| Konsep inti | 30 | Mental model sebelum syntax |
| Demo pengajar | 25 | Masalah → solusi |
| Praktik terpandu | 55 | Jalankan dan modifikasi |
| Challenge mandiri | 30 | Variasi tanpa menyalin |
| Debugging & refleksi | 15 | Baca error, bandingkan solusi |
| Exit ticket | 10 | Verifikasi target |

## Penilaian Umum
| Aspek | Bobot |
|---|---:|
| Pemahaman algoritma | 25% |
| Implementasi | 25% |
| Kualitas kode | 15% |
| Pengujian & troubleshooting | 15% |
| Dokumentasi | 10% |
| Presentasi & penjelasan | 10% |

## Fase Pembelajaran
- **P1:** Scratch sepenuhnya; jangan memaksa Python.
- **P2–P6:** Scratch terlebih dahulu lalu Python/Colab; bandingkan struktur algoritma, bukan hanya syntax.
- **P7:** tekankan editor vs interpreter vs terminal vs GitHub, venv, dan source dari terminal.
- **P8:** checkpoint CLI; pilih satu dari 30 project; nilai proses, test, Git history, README.
- **P9–P11:** web/API/deployment berdasarkan layer dan bukti log.
- **P12:** checkpoint web/API/deploy; external API boleh dimock agar penilaian reproducible.
- **P13–P15:** mental model multi-service bertahap; jangan menambah layer hanya agar terlihat enterprise.
- **P16:** integrasi end-to-end; fokus tanggung jawab layer, relasi data, validation, security minimum, testing, dan demo.

## AI-Assisted Coding
Mulai P9, ajarkan prompt teknis terstruktur dari `Referensi/AI-Assisted-Coding.md`. AI tidak menggantikan requirement, expected behavior, test, log, code review, atau kemampuan menjelaskan kode sendiri.

## Exit Ticket Umum
1. Apa input program?
2. Apa proses/keputusan utama?
3. Di mana state/data disimpan?
4. Bagaimana output dihasilkan?
5. Test apa yang membuktikan program benar?
6. Bug apa yang ditemukan?
7. Bukti apa yang menunjukkan fix benar?
