# P02 — Variable, Input, dan Condition

Buat variable `nama`, `skor`, dan `target`.

```text
when green flag clicked
set [skor] to (0)
set [target] to (5)
ask [Siapa nama kamu?] and wait
set [nama] to (answer)
say (join [Halo ] (nama)) for (2) seconds

if <(nama) = []> then
  say [Nama tidak boleh kosong] for (2) seconds
end
```

Uji nama normal, input kosong, dan perubahan target.
