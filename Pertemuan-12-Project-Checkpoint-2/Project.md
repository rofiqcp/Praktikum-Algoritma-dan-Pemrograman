# Project Pertemuan 12 — Python Web + API + Deployment

> Pilih **satu** project. Semua project berasal dari bank checkpoint buku panduan dan wajib menggabungkan kompetensi pertemuan 9–11. Starter hanyalah kerangka teknis.

## Requirement Setara untuk Semua Project
- Flask sebagai backend web utama dan template HTML.
- Minimal 3 halaman dan 6 komponen UI.
- REST API internal dengan response JSON dan status code sesuai.
- Satu integrasi external/mock API dengan timeout dan error handling.
- Environment variable untuk konfigurasi/credential sensitif.
- Dapat dideploy dari GitHub dan mempunyai public URL.
- Tabel minimal 10 test case termasuk API failure.

## Deliverable Umum
- GitHub repo + README + endpoint documentation.
- Public URL yang diuji dari perangkat lain.
- Screenshot/log bukti deployment berhasil.
- Test report expected-vs-actual.

## Rubrik
| Aspek | Bobot |
|---|---:|
| UI & alur pengguna | 15 |
| Backend Flask | 20 |
| API sendiri | 20 |
| Integrasi API external/mock | 10 |
| Validation & error state | 10 |
| Deployment & config | 15 |
| Dokumentasi/testing/demo | 10 |

## 1. Dashboard Cuaca Kegiatan
Panitia kegiatan luar ruang memilih kota dan menyimpan rencana kegiatan. Website memanggil API cuaca publik/mock, menampilkan sukses/gagal, serta menyediakan API internal untuk daftar rencana kegiatan.

## 2. Konverter Mata Uang Perjalanan
Traveler memasukkan nominal dan mata uang asal/tujuan. Ambil kurs dari API publik/mock, tampilkan hasil, simpan riwayat konversi, dan sediakan endpoint pembacaan riwayat.

## 3. Pencari Buku dan Reading List
Cari buku melalui API katalog publik/mock, tampilkan hasil sebagai card, lalu tambah/hapus judul pada reading list yang dikelola API internal.

## 4. Papan Info Film
Cari film melalui API publik/mock, tampilkan detail, kelola watchlist, dan tampilkan loading/error/no-result state.

## 5. Dashboard Negara
Cari negara, tampilkan ibu kota/populasi/region dari API publik/mock, dan kelola daftar negara favorit melalui API internal.

## 6. Perencana Menu dan Resep
Cari resep melalui API publik/mock, tampilkan ringkasan, lalu kelola daftar rencana masak dengan REST API internal.

## 7. Pencari Fakta Angkasa
Ambil data astronomi/space berdasarkan tanggal/kategori dari API publik/mock dan simpan catatan observasi melalui API internal.

## 8. Dashboard Gempa Edukasi
Tampilkan data gempa publik/mock sebagai latihan data, filter sederhana, dan daftar kejadian untuk dipelajari. Fokus pemrograman/data, bukan klaim keselamatan real-time.

## 9. Daftar Tugas + Quote API
Aplikasi todo Flask memiliki CRUD REST internal dan menampilkan quote dari API publik/mock. Kegagalan API quote tidak boleh membuat fitur todo utama gagal.

## 10. Katalog Produk Simulasi
Ambil katalog dari mock product API, sediakan pencarian/filter, lalu kelola wishlist internal beserta dokumentasi endpoint.

## 11. Dashboard Harga Crypto Edukasi
Ambil harga aset publik/mock sebagai latihan visualisasi, tanpa rekomendasi investasi. Kelola watchlist dengan API internal.

## 12. Pencari Universitas
Cari universitas berdasarkan negara/kata kunci dari API publik/mock, simpan shortlist, dan buat halaman pencarian, shortlist, serta about/API docs.

## 13. Generator Profil Karakter
Ambil random user/character dari API publik/mock, tampilkan card, dan kelola favorit internal.

## 14. Dashboard Kualitas Udara Demo
Tampilkan data kualitas udara publik/mock sebagai latihan integrasi. Tampilkan sumber/timestamp bila tersedia, jangan diubah menjadi nasihat medis, dan kelola lokasi favorit.

## 15. Agenda Event Lokal Simulasi
Gunakan mock event API, filter kategori, tampilkan event, dan kelola daftar event pilihan.

## 16. Pencari Museum/Koleksi
Gunakan API museum/collection publik atau dataset mock, tampilkan pencarian, dan kelola koleksi favorit.

## 17. Dashboard Hari Libur
Pilih negara/tahun, ambil hari libur dari API publik/mock, tampilkan list, dan simpan rencana kegiatan pada tanggal tertentu melalui endpoint internal.

## 18. Kamus Mini Online
Kirim kata ke dictionary API publik/mock, tampilkan arti/contoh bila tersedia, dan kelola daftar kosakata yang dipelajari.

## 19. Pencari Lokasi Kode Pos
Masukkan kode pos/area, ambil informasi lokasi publik/mock, tampilkan card, simpan favorit, dan tangani kode tidak ditemukan dengan jelas.

## 20. Dashboard GitHub Repository Publik
Masukkan username/repository publik, panggil GitHub public API sesuai batas yang berlaku, tampilkan data umum, dan simpan repo favorit. Tugas dasar tidak meminta token pribadi.

## 21. Papan Berita Teknologi Mock
Baca feed/API berita mock yang disediakan pengajar, tampilkan card, dan kelola bookmark. Fokus API, bukan scraping situs.

## 22. Pencari Nama dan Statistik
Gunakan API statistik nama/mock untuk latihan query parameter, tampilkan hasil, dan simpan pencarian favorit.

## 23. Dashboard Transportasi Mock
Gunakan API transportasi simulasi dari pengajar untuk jadwal/rute dan kelola daftar perjalanan pilihan.

## 24. Pencari Game Publik
Gunakan API game publik/mock, cari game, tampilkan detail ringkas, dan sediakan CRUD wishlist.

## 25. Dashboard Open Data Kota
Gunakan endpoint open data/mock dari pengajar, filter dataset, tampilkan tabel, dan simpan filter preset melalui API internal.

## 26. Pencari Foto Edukasi
Gunakan API gambar legal atau mock metadata, tampilkan thumbnail/metadata dan koleksi favorit. API key jika ada wajib berada pada environment variable.

## 27. Catatan Belajar + Trivia
Aplikasi catatan mempunyai CRUD internal dan mengambil trivia dari API publik/mock. Jika trivia gagal, catatan utama tetap dapat digunakan.

## 28. Dashboard Kursus Online Mock
Baca daftar kursus dari API mock, filter topik, dan kelola daftar kursus target.

## 29. Planner Workout Edukasi
Gunakan dataset/API latihan mock; pengguna memilih kategori aktivitas, melihat gerakan, lalu membuat rencana latihan pribadi. Fokus pemrograman, bukan rekomendasi kesehatan.

## 30. Dashboard Statistik Olahraga Mock
Gunakan API/dataset mock skor/statistik, tampilkan data dan watchlist tim. Hindari ketergantungan data live yang berubah saat penilaian; pengajar dapat menyediakan mock response.

## Uji Wajib
Setiap project wajib memiliki kasus normal, boundary, invalid input, not-found bila relevan, serta external/mock API failure/timeout, hingga minimal 10 test case.
