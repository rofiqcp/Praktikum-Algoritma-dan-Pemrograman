produk=[{"nama":"Keyboard","harga":250000,"stok":10},{"nama":"Mouse","harga":120000,"stok":6},{"nama":"Kabel","harga":50000,"stok":20}]

def cari(nama):
    return next((p for p in produk if p["nama"].lower()==nama.lower()),None)

def main():
    for p in produk: print(p)
    q=input("Cari nama barang: ").strip(); p=cari(q)
    print(p if p else "Barang tidak ditemukan")

if __name__ == "__main__": main()
