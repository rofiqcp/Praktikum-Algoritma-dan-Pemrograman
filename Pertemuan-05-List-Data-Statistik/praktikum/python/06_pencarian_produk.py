PRODUK = [
    {"nama": "Keyboard", "harga": 250000, "stok": 10},
    {"nama": "Mouse", "harga": 120000, "stok": 5},
    {"nama": "Headset", "harga": 300000, "stok": 4},
]


def cari_produk(data, keyword):
    keyword = keyword.strip().lower()
    for item in data:
        if item["nama"].lower() == keyword:
            return item
    return None


if __name__ == "__main__":
    keyword = input("Cari nama produk: ")
    hasil = cari_produk(PRODUK, keyword)
    if hasil is None:
        print("Produk tidak ditemukan.")
    else:
        print("Nama :", hasil["nama"])
        print("Harga:", hasil["harga"])
        print("Stok :", hasil["stok"])
