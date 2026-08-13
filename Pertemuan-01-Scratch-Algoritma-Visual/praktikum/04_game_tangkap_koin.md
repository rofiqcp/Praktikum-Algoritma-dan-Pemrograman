# P04 — Game Tangkap Koin Lengkap

## Tujuan

Mengintegrasikan sequence, event, variable/state, condition, loop, sensing, random position, feedback, broadcast, dan kondisi selesai.

## Komponen

- Sprite `Pemain` dan `Koin`.
- Variable global `skor`, `target`, `gameAktif`.
- Message `MENANG`.

## Sprite Pemain

```text
when green flag clicked
go to x: (0) y: (-140)
point in direction (90)

when [right arrow] key pressed
if <(gameAktif) = (1)> then
  change x by (15)
end

when [left arrow] key pressed
if <(gameAktif) = (1)> then
  change x by (-15)
end
```

## Sprite Koin

```text
when green flag clicked
set [skor] to (0)
set [target] to (10)
set [gameAktif] to (1)
go to x: (pick random (-200) to (200)) y: (pick random (-80) to (150))

forever
  if <(gameAktif) = (1)> then
    if <touching [Pemain] ?> then
      change [skor] by (1)
      start sound [pop]
      go to x: (pick random (-200) to (200)) y: (pick random (-80) to (150))
      wait (0.15) seconds
    end

    if <(skor) >= (target)> then
      set [gameAktif] to (0)
      broadcast [MENANG]
    end
  end
end
```

## Respons MENANG

```text
when I receive [MENANG]
say [MENANG!] for (2) seconds
stop [all]
```

## Urutan Verifikasi

1. Green Flag: `skor=0`, `gameAktif=1`.
2. Uji kanan dan kiri.
3. Uji posisi acak koin.
4. Uji collision satu kali.
5. Ubah `target=1` dan buktikan kondisi selesai.
6. Kembalikan `target=10`.
7. Selesaikan permainan.
8. Green Flag kembali dan pastikan state reset.

## Test Minimum

| ID | Skenario | Expected |
|---|---|---|
| T01 | Green Flag | state awal benar |
| T02 | kanan 1× | x pemain +15 |
| T03 | kiri 1× | x pemain -15 |
| T04 | tidak touching | skor tetap |
| T05 | touching | skor +1 dan koin pindah |
| T06 | skor target-1 | game masih aktif |
| T07 | skor mencapai target | pesan MENANG dan selesai |
| T08 | run ulang | state reset |

## Pengayaan

Tambahkan satu fitur baru yang mengubah state atau aturan game. Jelaskan variable/condition yang berubah, buat dua test baru, lalu ulangi test inti agar fitur lama tetap bekerja.
