# Padanan Scratch — Pertemuan 02

## Biodata
```text
when green flag clicked
ask [Nama?] and wait
set [nama] to (answer)
ask [Umur?] and wait
set [umur] to (answer)
say (join [Halo ] (nama))
```

## Kalkulator Belanja
Variable: `nama_barang`, `harga`, `jumlah`, `total`.
```text
ask [Nama barang?] and wait
set [nama_barang] to (answer)
ask [Harga satuan?] and wait
set [harga] to (answer)
ask [Jumlah?] and wait
set [jumlah] to (answer)
set [total] to ((harga) * (jumlah))
say (join [Total = ] (total))
```

Bandingkan `ask → input`, `say → print`, `set variable → assignment`, operator Scratch → Python.
