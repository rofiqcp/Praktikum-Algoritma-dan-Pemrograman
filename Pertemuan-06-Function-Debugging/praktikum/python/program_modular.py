def hitung_total(harga,jumlah): return harga*jumlah
def hitung_diskon(total,member): return total*0.10 if member and total>=100_000 else 0.0
def format_rupiah(n): return f"Rp{n:,.0f}"
def main():
    try:
        harga=float(input("Harga: ")); jumlah=int(input("Jumlah: "))
    except ValueError: print("Input invalid"); return
    if harga<0 or jumlah<0: print("Tidak boleh negatif"); return
    member=input("Member? y/n: ").lower()=="y"
    total=hitung_total(harga,jumlah); diskon=hitung_diskon(total,member)
    print("Subtotal",format_rupiah(total)); print("Diskon",format_rupiah(diskon)); print("Bayar",format_rupiah(total-diskon))
if __name__=="__main__": main()
