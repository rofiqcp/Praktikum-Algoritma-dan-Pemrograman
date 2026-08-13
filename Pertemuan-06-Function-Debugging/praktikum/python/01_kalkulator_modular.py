def hitung_total(harga,jumlah):
    if harga < 0 or jumlah < 0: raise ValueError("harga/jumlah tidak boleh negatif")
    return harga*jumlah

def format_rupiah(nilai): return f"Rp{nilai:,.0f}"

if __name__ == "__main__":
    try:
        harga=float(input("Harga: ")); jumlah=int(input("Jumlah: "))
        print(format_rupiah(hitung_total(harga,jumlah)))
    except ValueError as e: print("Input tidak valid:",e)
