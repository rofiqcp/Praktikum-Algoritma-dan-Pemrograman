def main():
    try:
        hari=int(input("Berapa hari menabung? "))
        setoran=float(input("Setoran per hari: "))
    except ValueError:
        print("Input harus angka"); return
    if hari <= 0 or setoran < 0:
        print("Input tidak valid"); return
    saldo=0.0
    for i in range(1,hari+1):
        saldo += setoran
        print(f"Hari {i}: Rp{saldo:,.0f}")
    print(f"Saldo akhir: Rp{saldo:,.0f}")
if __name__=="__main__": main()
