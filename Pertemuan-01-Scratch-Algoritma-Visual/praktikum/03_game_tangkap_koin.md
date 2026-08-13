# P03 — Game Tangkap Koin

## Sprite Pemain
```text
when green flag clicked
go to x: (0) y: (-140)

when [right arrow] key pressed
change x by (15)

when [left arrow] key pressed
change x by (-15)
```

## Variable Global
`skor`, `target`, `gameAktif`.

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

```text
when I receive [MENANG]
say [MENANG!] for (2) seconds
stop [all]
```

Challenge: nyawa, timer, level, atau benda berbahaya. Uji target 1 lebih dulu untuk memverifikasi kondisi akhir.
