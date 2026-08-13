# Project Pertemuan 16 — Final Full Stack Node.js + Python + Database

> Pilih **satu** dari 30 variasi. Semua project mempunyai bobot inti setara. Starter hanya referensi arsitektur; mahasiswa tetap harus merancang fitur, ERD, validation, test, Git history, dan dokumentasi sendiri.

## Requirement Wajib Semua Final Project
- Node.js/Express web layer dengan minimal 4 screen/section.
- Python REST API terstruktur dan mempunyai validation.
- Database minimal 2 tabel berelasi dan operasi JOIN/filter.
- CRUD resource utama + search/filter.
- UI mempunyai loading, empty, success, dan error state.
- Environment variable untuk konfigurasi service/database.
- Minimal 15 test case dan satu regression test setelah bug fix.
- Git history bertahap.
- ERD/schema, API docs, README setup/run, dan deployment/public demo sesuai platform.

## Rubrik
| Aspek | Bobot |
|---|---:|
| Analisis & desain/ERD | 10 |
| Node web/UI | 15 |
| Python API/business logic | 20 |
| Database & relasi | 15 |
| Integrasi end-to-end | 15 |
| Validation/error/security basics | 10 |
| Testing/troubleshooting | 7 |
| Git/docs/deploy | 5 |
| Demo & pemahaman | 3 |

## 1. Sistem Inventori dan Kategori
Dashboard produk yang dikelompokkan kategori. Admin membuat kategori, menambah/edit/hapus produk, mencari produk, dan melihat stok rendah. Relasi utama: category memiliki banyak products.

## 2. Perpustakaan dan Peminjaman
Kelola books dan loans (opsional members), tampilkan ketersediaan, buat peminjaman/pengembalian, cari buku, dan cegah peminjaman saat buku tidak tersedia.

## 3. Manajemen Kursus dan Peserta
Kelola courses dan enrollments/peserta. Lihat kursus, tambah/batalkan peserta, tampilkan jumlah peserta, dan validasi kapasitas.

## 4. Reservasi Meja Restoran
Kelola tables dan reservations. Tampilkan meja/kapasitas/status, booking, pembatalan, pencarian tanggal/nama, dan cegah double booking slot sama.

## 5. Sistem Laundry dan Item Pesanan
Kelola customers/orders atau orders/order_items. Buat order, tambah layanan/item, hitung total di backend, ubah status, dan cari order.

## 6. Bengkel Servis dan Riwayat Kendaraan
Kelola vehicles dan service_records. Daftarkan kendaraan, buat catatan servis, ubah status, lihat riwayat per kendaraan, dan cari nomor kendaraan.

## 7. Klinik Antrian Non-Medis
Sistem administrasi patients/queue_entries tanpa diagnosis. Daftar nama, buat nomor antrian, panggil berikutnya, ubah status, dan tampilkan antrean aktif.

## 8. Event dan Registrasi Peserta
Kelola events dan registrations. Lihat event, daftar/batal, hitung peserta, cegah registrasi duplikat dan kapasitas terlampaui.

## 9. Rental Sepeda dan Transaksi
Kelola bicycles dan rentals. Tampilkan unit tersedia, buat/tutup sewa, hitung biaya dari durasi input, dan riwayat per sepeda.

## 10. Hotel Mini dan Booking
Kelola rooms dan bookings. Cari kamar, booking tanggal, pembatalan, status, dan validasi overlap tanggal sederhana.

## 11. Toko Buku dan Pesanan
Kelola books/categories/orders (opsional order_items). Browsing buku, buat pesanan simulasi, kurangi stok lewat backend, dan tampilkan order history.

## 12. Kafe: Menu dan Pesanan
Kelola menu_items dan orders/order_items. Tampilkan menu, buat order multi-item, backend menghitung total, dan status new → preparing → done.

## 13. Laboratorium: Alat dan Peminjaman
Kelola equipments dan borrowings. Lihat stok, pinjam jumlah tertentu, pengembalian, riwayat, dan low-stock warning.

## 14. Sekolah: Kelas dan Tugas
Kelola classes dan assignments (opsional submissions). Tampilkan tugas per kelas, status deadline, filter, dan validasi relasi/tanggal.

## 15. Helpdesk Ticketing
Kelola tickets/comments (users opsional). Buat tiket, tambah komentar, ubah status/prioritas, cari, dan tampilkan riwayat perubahan sederhana.

## 16. Manajemen Gudang dan Mutasi Stok
Kelola products dan stock_movements. Stok dihitung dari mutasi masuk/keluar, UI menampilkan stok saat ini dan riwayat mutasi; gunakan transaction untuk menjaga konsistensi.

## 17. Sistem Donasi Barang
Kelola donors dan donations/items tanpa data sensitif berlebihan. Catat donor, barang, status distribusi, dan laporan jumlah per kategori.

## 18. Agenda Organisasi dan Kehadiran
Kelola meetings/events dan attendances. Buat kegiatan, catat kehadiran, tampilkan persentase, dan filter tanggal/kegiatan.

## 19. Pet Shop: Hewan dan Perawatan
Kelola pets dan care_records/customers untuk administrasi non-medis sederhana: jadwal perawatan, status selesai, dan riwayat per hewan.

## 20. Koperasi Mini: Produk dan Transaksi
Kelola products dan transactions/transaction_items. Buat transaksi, hitung total backend, kurangi stok, dan laporan transaksi sederhana.

## 21. Jadwal Ruangan dan Booking
Kelola rooms dan bookings. Lihat kapasitas, cari slot, booking/batal, dan cegah overlap waktu.

## 22. Asset IT dan Penugasan
Kelola assets dan assignments. Tampilkan perangkat/status/pemegang, proses assign/return, dan riwayat singkat.

## 23. Sistem Paket dan Tracking Status
Kelola packages dan tracking_events. Buat paket, tambah status perjalanan, cari kode tracking, dan tampilkan timeline per paket.

## 24. Manajemen Proyek dan Task
Kelola projects dan tasks. Buat project, tambah task, ubah status/prioritas, filter, dan hitung progres berdasarkan task selesai.

## 25. Penyewaan Peralatan Acara
Kelola equipments dan rentals/rental_items. Cek ketersediaan, buat sewa, kembalikan barang, dan hitung biaya.

## 26. Katalog Wisata dan Itinerary
Kelola destinations dan itinerary_items. Simpan destinasi, buat itinerary harian, urutkan kunjungan, dan lihat rencana berdasarkan tanggal.

## 27. Sistem Pesanan Catering
Kelola menus dan orders. Pilih paket/menu, jumlah porsi/tanggal, backend menghitung total dan validasi minimum order, admin mengubah status.

## 28. Manajemen Kebun dan Catatan Panen
Kelola plots/crops dan harvest_records. Tampilkan petak, buat catatan panen, hitung total per petak, dan filter periode.

## 29. Sistem Klub dan Keanggotaan
Kelola clubs dan memberships/members. Buat klub, tambah anggota, ubah status membership, dan hitung anggota per klub.

## 30. Pusat Pelatihan: Kelas dan Sertifikat Simulasi
Kelola classes dan participants/completions. Daftarkan peserta, catat status penyelesaian, dan hasilkan tampilan sertifikat simulasi bagi peserta yang memenuhi syarat internal project.

## Uji Wajib
Setiap pilihan harus mencakup normal case, boundary, invalid input, not-found/capacity bila relevan, relationship/FK, duplicate/conflict, UI failure state, backend unavailable, dan regression setelah bug fix hingga minimal 15 test case.
