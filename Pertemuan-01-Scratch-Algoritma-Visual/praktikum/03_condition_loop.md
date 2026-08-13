# P03 — Condition, Loop, dan Sensing

## Tujuan

Membuktikan bahwa `if` hanya menjalankan aksi saat kondisi true dan `forever` membuat kondisi diperiksa terus-menerus.

## Persiapan

Gunakan sprite `Pemain` dan `Koin`. Aktifkan monitor variable `skor`.

## Tahap 1 — Condition tanpa skor

Pada sprite `Koin`:

```text
when green flag clicked
forever
  if <touching [Pemain] ?> then
    say [TERTANGKAP!] for (0.3) seconds
  end
end
```

Uji dua keadaan:

1. sprite terpisah → pesan tidak muncul;
2. sprite menyentuh → pesan muncul.

## Tahap 2 — Tambahkan state

```text
when green flag clicked
set [skor] to (0)
forever
  if <touching [Pemain] ?> then
    change [skor] by (1)
    say [TERTANGKAP!] for (0.15) seconds
  end
end
```

Amati apakah satu overlap dapat menaikkan skor beberapa kali. Catat sebagai hasil pengamatan loop.

## Tahap 3 — Pisahkan satu kejadian tangkap

Setelah collision tambahkan:

```text
go to x: (pick random (-200) to (200)) y: (pick random (-80) to (150))
wait (0.15) seconds
```

Dengan memindahkan koin, kondisi `touching` kembali false dan tangkapan berikutnya menjadi kejadian baru.

## Tabel Uji

| Kondisi | Expected | Actual | Pass |
|---|---|---|:---:|
| tidak touching | skor tetap |  | ☐ |
| touching | skor bertambah |  | ☐ |
| koin dipindah | posisi berubah |  | ☐ |
| touching berikutnya | skor bertambah lagi |  | ☐ |

## Pertanyaan

1. Mengapa `touching` perlu diperiksa berulang?
2. Apa tugas `if` dan apa tugas `forever`?
3. Mengapa memindahkan koin membantu membedakan satu collision dari collision berikutnya?
