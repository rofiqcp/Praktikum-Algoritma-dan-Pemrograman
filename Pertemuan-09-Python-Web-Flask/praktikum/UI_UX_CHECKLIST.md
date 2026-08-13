# Checklist UI/UX Praktikum Pertemuan 09

Checklist ini digunakan untuk memeriksa apakah antarmuka Flask dapat dipahami, dioperasikan, dan memberikan umpan balik yang jelas. Fokusnya adalah fungsi dan keterpakaian dasar, bukan dekorasi visual.

## Struktur dan Hierarki
- [ ] Setiap halaman mempunyai satu judul utama yang jelas.
- [ ] Aksi utama mudah ditemukan.
- [ ] Navigasi menggunakan istilah yang konsisten pada semua halaman.
- [ ] Informasi penting tidak tertutup oleh elemen lain pada layar sempit.

## Form dan Input
- [ ] Setiap input mempunyai `label` yang terhubung melalui atribut `for` dan `id`.
- [ ] Tipe input sesuai dengan data yang diminta.
- [ ] Nilai yang sudah diketik tetap terlihat ketika validasi gagal.
- [ ] Pesan kesalahan ditempatkan dekat field yang bermasalah.
- [ ] Validasi di server tetap dilakukan meskipun HTML memakai `required` atau tipe input tertentu.

## State dan Umpan Balik
- [ ] State normal dapat dikenali.
- [ ] Focus keyboard terlihat.
- [ ] Data kosong menampilkan empty state, bukan tabel kosong yang membingungkan.
- [ ] Pencarian tanpa hasil dibedakan dari kondisi belum ada data.
- [ ] Aksi berhasil memberikan umpan balik yang terlihat.
- [ ] Kesalahan memberikan pesan yang membantu pengguna memperbaiki input.
- [ ] Warna bukan satu-satunya cara membedakan status.

## Navigasi dan Aksesibilitas Dasar
- [ ] Semua link dan tombol dapat dicapai dengan keyboard.
- [ ] Urutan fokus masuk akal.
- [ ] Teks link menjelaskan tujuan aksi.
- [ ] Elemen navigasi memiliki label yang sesuai bila diperlukan.
- [ ] Gambar, jika digunakan untuk menyampaikan informasi, mempunyai teks alternatif.

## Responsive
- [ ] Halaman tetap dapat digunakan pada lebar sekitar 360–400 px.
- [ ] Form tidak keluar dari layar.
- [ ] Tabel atau daftar tetap dapat dibaca pada layar kecil.
- [ ] Tombol utama tetap mudah ditekan.
- [ ] Tidak ada teks penting yang terpotong.

## Bukti Audit
Catat minimal satu temuan dan satu perbaikan.

```text
Halaman/komponen :
Masalah awal     :
Dampak ke pengguna:
Perubahan        :
Cara verifikasi  :
Hasil retest     :
```

> Pengayaan Implementasi Repository: checklist ini memperluas prinsip UI/UX dasar pada buku menjadi langkah verifikasi praktis untuk project contoh.
