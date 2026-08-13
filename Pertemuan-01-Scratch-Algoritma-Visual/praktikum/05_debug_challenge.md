# P05 — Debug Challenge Scratch

## Tujuan
Melatih debugging berbasis bukti: reproduce gejala, membandingkan expected dengan actual, menentukan hipotesis, mengubah satu hal, lalu melakukan retest.

Gunakan **salinan** Game Tangkap Koin yang sudah benar dari `04_game_tangkap_koin.md`. Jangan merusak file/project utama.

## Prosedur
```text
REPRODUCE → EXPECTED vs ACTUAL → PASANG INDIKATOR → HIPOTESIS → UBAH SATU HAL → RETEST → REGRESSION TEST
```

## Kasus 1 — Event Tombol Salah
Pada salinan project, ubah event tombol kanan menjadi tombol lain.

Expected: panah kanan menggerakkan pemain ke kanan.
Actual: catat hasil yang muncul.

Periksa event yang aktif, perbaiki satu blok, lalu uji tombol kanan dan kiri kembali.

## Kasus 2 — Skor Tidak Reset
Hapus sementara `set [skor] to (0)` pada Green Flag. Mainkan sampai skor berubah, kemudian klik Green Flag lagi.

Expected: run baru selalu dimulai dari skor 0.
Actual: catat nilai yang tersisa.

Kembalikan inisialisasi skor dan retest dua kali.

## Kasus 3 — Boundary Menang Salah
Pada salinan, ubah kondisi menang dari `skor >= target` menjadi kondisi yang salah, misalnya `skor > target`.

Uji `target=1`.

Expected: game selesai saat skor tepat mencapai target.
Actual: catat kapan game benar-benar berhenti.

Perbaiki operator, kemudian uji `target-1`, `target`, dan `target+1`.

## Kasus 4 — Collision Terhitung Berulang
Hilangkan sementara `wait (0.15) seconds` setelah collision atau biarkan koin tetap menyentuh pemain.

Amati apakah satu sentuhan dapat menaikkan skor beberapa kali. Tambahkan kembali mekanisme pemisah/penundaan yang tepat dan retest.

## Format Catatan
```text
Kasus:
Langkah reproduce:
Expected:
Actual:
Bukti/indikator:
Hipotesis:
Satu perubahan yang dilakukan:
Retest:
Regression test:
Kesimpulan:
```

Dokumentasikan minimal tiga kasus. Setelah setiap fix, ulangi test inti pada `04_game_tangkap_koin.md` agar perbaikan tidak merusak fitur yang sebelumnya sudah benar.
