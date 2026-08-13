# P01 — Sequence dan Event

## Sprite
Gunakan satu sprite `Pemain`.

```text
when green flag clicked
go to x: (0) y: (-120)
point in direction (90)
say [Siap!] for (1) seconds

when [right arrow] key pressed
change x by (10)

when [left arrow] key pressed
change x by (-10)
```

## Challenge
Tambahkan panah atas/bawah tetapi batasi sprite agar tidak keluar Stage.

## Test
- Green Flag selalu mengembalikan pemain ke `(0,-120)`.
- Kanan menambah x tepat 10.
- Kiri mengurangi x tepat 10.
