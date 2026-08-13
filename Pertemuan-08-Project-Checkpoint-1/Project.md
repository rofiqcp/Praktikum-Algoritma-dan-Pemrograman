# Project Pertemuan 08 — Checkpoint Algoritma + Python Lokal + GitHub

> Pilih **satu** dari 30 soal cerita berikut. Seluruh project memakai kompetensi Pertemuan 01–07 saja. Starter pada `praktikum/` hanya kerangka teknis dan tidak boleh dianggap sebagai jawaban project.

## Ketentuan Umum dari Buku Panduan

Semua pilihan memiliki bobot inti setara:

- CLI Python lokal dengan menu utama minimal **4 operasi**;
- menggunakan condition, loop, list/dictionary, function, dan validasi input;
- minimal **5 function bermakna**;
- minimal **8 test case** yang mencakup normal, boundary, invalid input, dan not-found/capacity bila relevan;
- minimal **5 commit Git** yang menunjukkan progres nyata;
- data in-memory sudah cukup; penyimpanan file merupakan bonus, bukan syarat;
- nama function/variable harus menjelaskan maksud dan logic tidak boleh diduplikasi berlebihan.

## Deliverable untuk Semua Project

1. Source code Python pada repository GitHub.
2. README: masalah, fitur, cara menjalankan, struktur, contoh penggunaan, dan cara test.
3. Flowchart atau pseudocode.
4. Tabel expected-vs-actual minimal delapan kasus.
5. Git history progres minimal lima commit.
6. Demo 3–5 menit.

## Rubrik

| Aspek | Bobot |
|---|---:|
| Analisis soal & flowchart | 15 |
| Fitur berjalan | 30 |
| Struktur function/data | 15 |
| Validasi & error handling | 15 |
| Testing | 10 |
| Git/GitHub & README | 10 |
| Demo & penjelasan | 5 |

---

# Bank 30 Project

## 1. Kasir Kantin Sekolah
Kantin sekolah ingin mengurangi kesalahan hitung saat jam istirahat. Buat aplikasi kasir terminal yang mempunyai daftar menu, menerima beberapa item pesanan, menghitung subtotal, diskon sederhana berdasarkan aturan yang diberikan pengajar, dan mengeluarkan ringkasan pembayaran. Program harus dapat menangani menu yang tidak ada, jumlah tidak valid, dan pilihan untuk menambah pesanan lagi.

**Kasus penting:** kode menu tidak ada, jumlah nol/negatif, beberapa item dalam satu transaksi, dan kondisi tepat pada batas diskon.

## 2. Rekap Nilai Kelas
Wali kelas ingin melihat hasil belajar tanpa menghitung manual. Program menerima beberapa nama dan nilai, menentukan status lulus, menampilkan nilai tertinggi/terendah/rata-rata, dan dapat mencari seorang siswa berdasarkan nama. Nilai di luar 0–100 harus ditolak dan program harus tetap berjalan.

**Kasus penting:** nilai 0, 74, 75, 100, -1, 101, siswa ditemukan, dan siswa tidak ditemukan.

## 3. Peminjaman Buku Kelas
Sudut baca kelas mempunyai koleksi buku terbatas. Program dapat melihat daftar buku dan status ketersediaan, meminjam, mengembalikan, dan mencari buku. Program harus mencegah peminjaman buku yang sedang dipinjam serta menolak pengembalian buku yang sebenarnya tersedia.

**Kasus penting:** pinjam buku tersedia, pinjam buku yang sudah dipinjam, kembali buku terpinjam, kembali buku yang sudah tersedia, dan buku tidak ditemukan.

## 4. Antrian Klinik Sekolah
UKS membutuhkan simulasi antrian pasien. Program dapat menambah pasien, menampilkan urutan, memanggil pasien berikutnya, dan mencari posisi pasien. Tambahkan kategori prioritas sederhana sehingga kasus prioritas dapat didahulukan berdasarkan aturan yang jelas.

**Kasus penting:** antrian kosong, tambah normal, tambah prioritas, panggil berikutnya, dan cari nama yang tidak ada.

## 5. Tabungan Mingguan
Sebuah kelompok belajar ingin mencatat target tabungan. Program menerima setoran beberapa anggota, menghitung total dan rata-rata, membandingkan dengan target, dan menampilkan anggota dengan setoran tertinggi. Input negatif harus ditolak.

**Kasus penting:** setoran nol, negatif, tepat target, di bawah target, di atas target, dan data anggota kosong.

## 6. Rental Alat Olahraga
Gudang olahraga menyewakan bola, raket, dan alat lain. Program menampilkan stok, memproses peminjaman dan pengembalian, menghitung jumlah stok tersisa, dan mencegah stok menjadi negatif. Pengguna dapat mencari alat berdasarkan nama.

**Kasus penting:** jumlah pinjam sama dengan stok, lebih dari stok, pengembalian, stok nol, dan alat tidak ditemukan.

## 7. Voting Ketua Kelas
Kelas akan memilih ketua dari beberapa kandidat. Program menerima daftar kandidat dan suara pemilih, menolak pilihan yang tidak terdaftar, menghitung perolehan suara, serta menampilkan pemenang atau kondisi seri.

**Kasus penting:** pilihan valid, pilihan tidak terdaftar, kandidat tanpa suara, pemenang tunggal, dan seri.

## 8. Perencana Anggaran Study Tour
Panitia membutuhkan kalkulator anggaran sederhana. Pengguna memasukkan jumlah peserta dan beberapa komponen biaya. Program menghitung total, biaya per peserta, membandingkan dengan batas anggaran, dan memberi rekomendasi apakah perlu penghematan.

**Kasus penting:** peserta nol, biaya negatif, total tepat anggaran, di bawah, dan melebihi anggaran.

## 9. Sistem Parkir Mini
Buat simulasi parkir yang mencatat kendaraan masuk secara sederhana menggunakan nomor kendaraan dalam list. Fitur: masuk, keluar, cari kendaraan, jumlah slot tersedia, dan tarif berdasarkan lama simulatif yang dimasukkan pengguna. Kendaraan yang sama tidak boleh masuk dua kali.

**Kasus penting:** kendaraan baru, nomor duplikat, parkir penuh, kendaraan keluar yang tidak ada, durasi tidak valid.

## 10. Toko Buah
Pemilik toko ingin kasir terminal. Data buah mempunyai nama, harga, dan stok. Pengguna dapat melihat katalog, membeli beberapa jenis buah, dan melihat total. Program mengurangi stok dan menolak pembelian jika stok tidak cukup.

**Kasus penting:** beli satu, beli beberapa, jumlah sama dengan stok, lebih dari stok, buah tidak ada, jumlah tidak valid.

## 11. Jadwal Piket Kelas
Ketua kelas membutuhkan program untuk menyusun dan melihat jadwal piket. Program menyimpan nama anggota per hari, dapat mencari jadwal seorang siswa, mengganti anggota tertentu, dan memastikan nama tidak kosong.

**Kasus penting:** pencarian ada/tidak ada, nama kosong, ganti anggota valid, dan anggota target tidak ada.

## 12. Skor Turnamen Mini
Panitia turnamen ingin mencatat skor beberapa peserta/tim. Program dapat menambah hasil pertandingan, menghitung total poin, menampilkan klasemen sederhana, serta menangani kondisi poin seri.

**Kasus penting:** hasil valid, tim tidak ada, poin seri, data pertandingan kosong, dan beberapa pertandingan.

## 13. Laundry Kiloan
Laundry membutuhkan kalkulator pesanan. Pengguna memilih layanan, memasukkan berat, menghitung harga, menambah biaya layanan khusus bila dipilih, dan menampilkan ringkasan. Berat nol/negatif harus ditolak.

**Kasus penting:** berat positif, nol, negatif, layanan tidak ada, layanan tambahan aktif/nonaktif.

## 14. Bengkel Servis Sederhana
Bengkel mencatat daftar jasa dan biaya. Program menerima beberapa pekerjaan servis untuk satu kendaraan, menghitung total, memberi diskon berdasarkan total tertentu, dan mencetak ringkasan. Jasa tidak dikenal harus ditolak.

**Kasus penting:** satu jasa, beberapa jasa, jasa tidak dikenal, tepat batas diskon, di bawah/di atas batas.

## 15. Pemesanan Tiket Acara
Panitia mempunyai kapasitas kursi terbatas. Program menampilkan sisa kursi, menerima pemesanan, membatalkan pemesanan, dan mencari nama pemesan. Jumlah pesanan tidak boleh melebihi kapasitas.

**Kasus penting:** pesan normal, tepat sisa kapasitas, melebihi kapasitas, batal nama tidak ada, dan kapasitas habis.

## 16. Pencatat Konsumsi Listrik
Pengguna memasukkan data pemakaian harian beberapa hari. Program menghitung total, rata-rata, hari tertinggi, dan memperingatkan jika pemakaian melewati ambang tertentu.

**Kasus penting:** satu hari, beberapa hari, tepat ambang, di atas ambang, dan input tidak valid sesuai aturan project.

## 17. Pengelola Stok Apotek Mini
Program mengelola beberapa nama obat bebas sebagai latihan data, **bukan nasihat medis**: lihat stok, tambah stok, kurangi stok karena transaksi, dan cari obat. Stok tidak boleh negatif dan nama kosong harus ditolak.

**Kasus penting:** tambah stok, kurangi tepat stok, kurangi melebihi stok, nama kosong, dan obat tidak ditemukan.

## 18. Daftar Kehadiran Kegiatan
Panitia ingin memasukkan peserta hadir/tidak hadir, menghitung persentase kehadiran, mencari status nama tertentu, dan menampilkan daftar yang belum hadir. Nama duplikat harus ditangani.

**Kasus penting:** hadir, tidak hadir, duplikat, pencarian tidak ada, dan data kosong sebelum persentase dihitung.

## 19. Perencana Menu Kafe
Kafe kecil ingin menyusun menu dan transaksi. Program menyimpan nama minuman, harga, stok, menerima pesanan beberapa item, menghitung total, dan menampilkan item terlaris berdasarkan jumlah simulatif yang dibeli.

**Kasus penting:** multi-item, stok tepat habis, stok tidak cukup, item tidak ada, dan kondisi jumlah pembelian sama.

## 20. Kalkulator Ongkir Paket
Kurir lokal menentukan ongkir berdasarkan berat dan zona. Program meminta data paket, memvalidasi berat, memilih zona, menghitung biaya dasar dan tambahan, serta menampilkan ringkasan beberapa paket.

**Kasus penting:** berat positif minimum menurut aturan pengajar, nol/negatif, zona valid/tidak valid, dan beberapa paket.

## 21. Penyewaan Sepeda
Tempat wisata mempunyai sejumlah sepeda. Program mencatat ketersediaan, proses sewa/kembali, durasi sewa yang dimasukkan pengguna, dan biaya. Sepeda yang sedang disewa tidak dapat disewa lagi.

**Kasus penting:** sewa tersedia, sewa ulang sepeda aktif, kembali, kembali sepeda yang tersedia, durasi tidak valid.

## 22. Manajemen Kamar Penginapan Mini
Penginapan kecil ingin melihat daftar nomor kamar dan statusnya. Program dapat check-in, check-out, mencari tamu, dan menghitung biaya berdasarkan malam yang dimasukkan. Check-in ke kamar terisi harus ditolak.

**Kasus penting:** check-in tersedia, kamar terisi, malam nol/negatif, check-out, dan tamu tidak ditemukan.

## 23. Kalkulator Gaji Harian
Sebuah usaha ingin menghitung upah beberapa pekerja dari jam kerja. Program menghitung upah normal dan lembur berdasarkan aturan, menolak jam tidak valid, lalu menampilkan total biaya tenaga kerja dan rata-rata.

**Kasus penting:** tepat batas jam normal, lembur, jam negatif, beberapa pekerja, dan data kosong.

## 24. Pemilihan Paket Internet
Program membantu pengguna memilih paket berdasarkan kuota, anggaran, dan kebutuhan. Simpan beberapa paket dalam list/dictionary, filter paket yang sesuai, lalu tampilkan pilihan dan alasan sederhana.

**Kasus penting:** satu pilihan cocok, beberapa cocok, tidak ada yang cocok, anggaran tepat harga paket, dan kuota tepat kebutuhan.

## 25. Pencatat Hasil Panen
Kelompok tani memasukkan hasil panen beberapa petak. Program menghitung total, rata-rata, petak tertinggi/terendah, dan mengelompokkan hasil di atas/bawah target.

**Kasus penting:** tepat target, di atas/bawah target, satu petak, beberapa petak, dan data kosong.

## 26. Koleksi Film Pribadi
Program terminal menyimpan daftar judul, genre, dan status sudah/belum ditonton. Pengguna dapat menambah, mencari, menandai sudah ditonton, dan menampilkan daftar berdasarkan genre.

**Kasus penting:** tambah film, judul kosong sesuai validasi project, cari ada/tidak ada, ubah status, dan genre tanpa hasil.

## 27. Peminjaman Alat Laboratorium
Laboratorium membutuhkan pencatatan alat. Program melihat stok, meminjamkan jumlah tertentu, menerima pengembalian, dan menampilkan alat yang stoknya di bawah batas minimum.

**Kasus penting:** pinjam normal, sama dengan stok, lebih dari stok, pengembalian, dan stok tepat batas minimum.

## 28. Reservasi Meja Restoran
Restoran memiliki beberapa meja dengan kapasitas berbeda. Program menampilkan meja tersedia, melakukan reservasi berdasarkan jumlah tamu, membatalkan reservasi, dan mencari reservasi berdasarkan nama.

**Kasus penting:** kapasitas tepat jumlah tamu, meja tidak cukup, semua meja terisi, pembatalan nama tidak ada, dan pencarian reservasi.

## 29. Perencana Belanja Bulanan
Pengguna memiliki anggaran bulanan. Program menerima daftar kebutuhan dan biaya, menghitung total, menampilkan sisa anggaran, dan menandai item terbesar. Jika melebihi anggaran, program menyarankan jumlah yang perlu dikurangi.

**Kasus penting:** total tepat anggaran, di bawah, di atas, biaya negatif sesuai validasi, dan daftar kosong.

## 30. Jadwal Bus Sederhana
Program menyimpan daftar rute, waktu, dan tarif. Pengguna dapat mencari berdasarkan tujuan, menampilkan semua jadwal, memilih perjalanan, dan menghitung total biaya untuk jumlah penumpang.

**Kasus penting:** tujuan ada/tidak ada, penumpang satu, jumlah nol/negatif, dan pilihan perjalanan tidak tersedia.

---

# Uji Wajib Per Project

Untuk project yang dipilih, siapkan setidaknya:

1. satu kasus normal;
2. satu nilai tepat di boundary;
3. satu input salah;
4. satu data tidak ditemukan atau kapasitas/stok habis bila relevan;
5. test tambahan hingga minimal delapan kasus total.

Gunakan `Jobsheet.md` untuk mengubah requirement project menjadi tabel pengujian.

---

# Panduan Implementasi Tambahan

> Bagian berikut adalah **panduan pengerjaan tambahan**, bukan persyaratan baru dari buku panduan.

Agar project mudah ditinjau, gunakan pola sederhana:

```text
project/
├── main.py
├── README.md
└── tests/            # opsional jika menggunakan unittest
```

Untuk project kecil, seluruh source boleh berada di `main.py` selama tetap dipecah menjadi function yang jelas. Jika program mulai terlalu panjang, mahasiswa boleh memisahkan helper ke file lain, tetapi checkpoint ini tidak menilai arsitektur framework atau design pattern tingkat lanjut.

## Pertanyaan sebelum coding

- Apa empat operasi utama saya?
- Data apa yang harus disimpan selama program berjalan?
- Apa lima function minimum yang masuk akal?
- Input apa yang dapat salah?
- Boundary paling penting berada di mana?
- Kondisi not-found atau capacity apa yang wajib diuji?

## Definition of Done

Project dianggap siap diserahkan jika source dapat dijalankan dari README, semua requirement inti dapat didemokan, minimal delapan test case sudah dicatat, minimal lima commit progres terlihat, dan mahasiswa dapat menjelaskan alur program dengan kata-katanya sendiri.
