# Project Pertemuan 08 — Checkpoint Algoritma + Python Lokal + GitHub

> Pilih **satu** dari 30 soal cerita berikut. Semua project memakai kompetensi pertemuan 1–7 saja. Starter pada `praktikum/` hanya kerangka teknis dan tidak boleh dianggap sebagai jawaban project.

## Target dan Ketentuan Umum
- CLI Python lokal dengan menu utama minimal 4 operasi.
- Menggunakan condition, loop, list/dictionary, function, dan validasi.
- Minimal 5 function bermakna.
- Minimal 8 test case: normal, boundary, invalid input, serta not-found/capacity bila relevan.
- Minimal 5 commit Git yang menunjukkan progres.
- Data in-memory cukup; penyimpanan file bonus.

## Deliverable untuk Semua Project
- Source code Python di repository GitHub.
- README: masalah, fitur, cara menjalankan, struktur, contoh penggunaan, cara test.
- Flowchart/pseudocode.
- Tabel expected-vs-actual minimal 8 kasus.
- Git history progres dan demo 3–5 menit.

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

## 1. Kasir Kantin Sekolah
Kantin sekolah ingin mengurangi kesalahan hitung saat jam istirahat. Buat aplikasi kasir terminal yang mempunyai daftar menu, menerima beberapa item pesanan, menghitung subtotal, diskon sederhana sesuai aturan pengajar, dan ringkasan pembayaran. Tangani menu tidak ada, jumlah tidak valid, dan pilihan menambah pesanan lagi.

## 2. Rekap Nilai Kelas
Program menerima beberapa nama dan nilai, menentukan status lulus, menampilkan nilai tertinggi/terendah/rata-rata, dan mencari siswa berdasarkan nama. Nilai di luar 0–100 harus ditolak tanpa menghentikan program.

## 3. Peminjaman Buku Kelas
Kelola daftar buku dan status ketersediaan: lihat, cari, pinjam, dan kembalikan. Cegah peminjaman buku yang sudah dipinjam dan tolak pengembalian buku yang sebenarnya tersedia.

## 4. Antrian Klinik Sekolah
Simulasikan antrian UKS: tambah pasien, tampilkan urutan, panggil pasien berikutnya, dan cari posisi. Tambahkan kategori prioritas sederhana dengan aturan yang jelas.

## 5. Tabungan Mingguan
Catat setoran beberapa anggota, hitung total/rata-rata, bandingkan dengan target, dan tampilkan anggota dengan setoran tertinggi. Input negatif harus ditolak.

## 6. Rental Alat Olahraga
Tampilkan stok, proses peminjaman/pengembalian, hitung stok tersisa, dan cari alat. Stok tidak boleh negatif.

## 7. Voting Ketua Kelas
Terima daftar kandidat dan suara, tolak pilihan tidak terdaftar, hitung perolehan, lalu tampilkan pemenang atau kondisi seri.

## 8. Perencana Anggaran Study Tour
Masukkan jumlah peserta dan komponen biaya, hitung total dan biaya per peserta, bandingkan dengan batas anggaran, lalu tampilkan rekomendasi penghematan bila over-budget.

## 9. Sistem Parkir Mini
Catat kendaraan masuk menggunakan nomor kendaraan dalam list. Fitur: masuk, keluar, cari, slot tersedia, dan tarif dari lama simulatif. Kendaraan sama tidak boleh masuk dua kali.

## 10. Toko Buah
Data buah memiliki nama, harga, dan stok. Pengguna melihat katalog, membeli beberapa jenis buah, menghitung total, dan stok berkurang. Tolak pembelian bila stok tidak cukup.

## 11. Jadwal Piket Kelas
Simpan anggota per hari, cari jadwal seorang siswa, ganti anggota tertentu, dan validasi nama tidak kosong.

## 12. Skor Turnamen Mini
Tambah hasil pertandingan, hitung total poin, tampilkan klasemen sederhana, dan tangani kondisi poin seri.

## 13. Laundry Kiloan
Pilih layanan, masukkan berat, hitung harga, tambahkan biaya layanan khusus bila dipilih, dan tampilkan ringkasan. Berat nol/negatif ditolak.

## 14. Bengkel Servis Sederhana
Simpan daftar jasa/biaya, terima beberapa pekerjaan servis, hitung total dan diskon berdasarkan aturan. Jasa tidak dikenal harus ditolak.

## 15. Pemesanan Tiket Acara
Kelola kapasitas kursi: tampilkan sisa, pesan, batal, dan cari pemesan. Pesanan tidak boleh melebihi kapasitas.

## 16. Pencatat Konsumsi Listrik
Masukkan pemakaian harian beberapa hari, hitung total/rata-rata/hari tertinggi, dan beri peringatan bila melewati ambang.

## 17. Pengelola Stok Apotek Mini
Sebagai latihan data, kelola beberapa nama obat bebas: lihat, tambah, kurangi stok karena transaksi, dan cari. Stok tidak boleh negatif; ini latihan pemrograman, bukan rekomendasi medis.

## 18. Daftar Kehadiran Kegiatan
Catat peserta hadir/tidak hadir, hitung persentase, cari status nama, tampilkan yang belum hadir, dan tangani nama duplikat.

## 19. Perencana Menu Kafe
Simpan nama minuman, harga, stok, terima pesanan multi-item, hitung total, dan tampilkan item terlaris berdasarkan transaksi simulatif.

## 20. Kalkulator Ongkir Paket
Tentukan ongkir berdasarkan berat dan zona. Validasi berat, pilih zona, hitung biaya dasar/tambahan, dan ringkas beberapa paket.

## 21. Penyewaan Sepeda
Catat ketersediaan, sewa/kembali, durasi simulatif, dan biaya. Sepeda yang sedang disewa tidak boleh disewa lagi.

## 22. Manajemen Kamar Penginapan Mini
Tampilkan nomor kamar/status, proses check-in/check-out, cari tamu, dan hitung biaya berdasarkan malam. Tolak check-in ke kamar terisi.

## 23. Kalkulator Gaji Harian
Hitung upah beberapa pekerja dari jam kerja, normal dan lembur sesuai aturan. Tolak jam tidak valid, tampilkan total biaya tenaga kerja dan rata-rata.

## 24. Pemilihan Paket Internet
Simpan beberapa paket dalam list/dictionary, filter berdasarkan kuota, anggaran, dan kebutuhan, kemudian tampilkan pilihan yang sesuai beserta alasan sederhana.

## 25. Pencatat Hasil Panen
Masukkan hasil beberapa petak, hitung total/rata-rata, petak tertinggi/terendah, dan kelompokkan di atas/bawah target.

## 26. Koleksi Film Pribadi
Simpan judul, genre, dan status sudah/belum ditonton. Fitur: tambah, cari, tandai sudah ditonton, dan filter berdasarkan genre.

## 27. Peminjaman Alat Laboratorium
Lihat stok, pinjamkan jumlah tertentu, terima pengembalian, dan tampilkan alat dengan stok di bawah batas minimum.

## 28. Reservasi Meja Restoran
Simpan meja dengan kapasitas berbeda, tampilkan yang tersedia, lakukan/batalkan reservasi, pilih meja sesuai jumlah tamu, dan cari berdasarkan nama.

## 29. Perencana Belanja Bulanan
Masukkan kebutuhan dan biaya, hitung total/sisa anggaran, tandai item terbesar, dan bila over-budget tampilkan jumlah yang perlu dikurangi.

## 30. Jadwal Bus Sederhana
Simpan daftar rute, waktu, dan tarif. Pengguna mencari berdasarkan tujuan, melihat semua jadwal, memilih perjalanan, dan menghitung biaya untuk jumlah penumpang.

## Uji Wajib Per Project
Untuk project yang dipilih, siapkan setidaknya: satu kasus normal, satu nilai tepat di batas, satu input salah, satu data tidak ditemukan atau kapasitas/stok habis jika relevan, serta test tambahan hingga minimal delapan kasus total.
