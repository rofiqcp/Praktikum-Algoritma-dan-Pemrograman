def main():
    total=0.0; jumlah_item=0
    print("Masukkan harga barang. Ketik 0 untuk selesai.")
    while True:
        try: harga=float(input("Harga: "))
        except ValueError:
            print("Harga harus angka."); continue
        if harga == 0: break
        if harga < 0:
            print("Harga tidak boleh negatif."); continue
        total += harga; jumlah_item += 1
    print(f"Item: {jumlah_item}; total: Rp{total:,.0f}")

if __name__ == "__main__": main()
