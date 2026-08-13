def tambah_stok(stok, jumlah):
    if jumlah < 0:
        raise ValueError("jumlah harus nol atau positif")
    return stok + jumlah


def buat_ringkasan(nama, stok):
    return f"{nama}: stok {stok}"


if __name__ == "__main__":
    stok_awal = 5
    stok_baru = tambah_stok(stok_awal, 3)
    print(buat_ringkasan("Mouse", stok_baru))
    print("Stok awal tetap:", stok_awal)
