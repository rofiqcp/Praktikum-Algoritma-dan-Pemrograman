# Praktikum Scratch — Game Tangkap Koin

Pertemuan 1 **hanya menggunakan Scratch**. File `.sb3` tidak dibuat otomatis karena project Scratch
disusun langsung melalui editor visual. Dokumen ini adalah resep blok yang harus dirakit dan dijalankan
di https://scratch.mit.edu/.

## Sprite dan variable

Buat dua sprite:

- `Pemain`
- `Koin`

Buat variable:

- `skor` (untuk semua sprite)
- `target` (untuk semua sprite)

## Script Stage / inisialisasi

```text
when green flag clicked
set [skor v] to (0)
set [target v] to (10)
```

## Script sprite Pemain

```text
when green flag clicked
go to x: (0) y: (-140)

forever
  if <key [left arrow v] pressed?> then
    change x by (-10)
  end
  if <key [right arrow v] pressed?> then
    change x by (10)
  end
end
```

## Script sprite Koin

```text
when green flag clicked
go to [random position v]

forever
  if <touching [Pemain v]?> then
    change [skor v] by (1)
    start sound [Coin v]
    go to [random position v]
  end

  if <(skor) >= (target)> then
    say [Menang!] for (2) seconds
    stop [all v]
  end
end
```

## Yang harus diuji

1. Green flag mengembalikan skor ke 0.
2. Panah kiri/kanan menggerakkan pemain.
3. Menyentuh koin menambah skor tepat 1.
4. Koin pindah ke posisi acak setelah tertangkap.
5. Program berhenti saat target tercapai.

## Challenge

Tambahkan `nyawa`, `timer`, atau satu sprite bahaya. Catat minimal tiga bug yang ditemukan dan
cara memperbaikinya.
