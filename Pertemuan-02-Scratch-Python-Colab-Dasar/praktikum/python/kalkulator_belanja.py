def main():
    nama_barang = input("Nama barang: ").strip()
    harga = float(input("Harga satuan: "))
    jumlah = int(input("Jumlah: "))

    if harga < 0 or jumlah < 0:
        print("Harga dan jumlah tidak boleh negatif.")
        return

    total = harga * jumlah
    print(f"Barang : {nama_barang}")
    print(f"Jumlah : {jumlah}")
    print(f"Total  : Rp{total:,.0f}")

if __name__ == "__main__":
    main()
