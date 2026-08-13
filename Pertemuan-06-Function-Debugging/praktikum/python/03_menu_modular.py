def luas_persegi_panjang(p,l): return p*l

def konversi_celsius(c): return c*9/5+32,c+273.15

def menu():
    while True:
        print("\n1 Luas  2 Suhu  0 Keluar")
        p=input("Pilih: ")
        try:
            if p=="1": print("Luas:",luas_persegi_panjang(float(input("Panjang: ")),float(input("Lebar: "))))
            elif p=="2": print("F, K:",*konversi_celsius(float(input("Celsius: "))))
            elif p=="0": break
            else: print("Pilihan tidak valid")
        except ValueError: print("Input angka tidak valid")

if __name__ == "__main__": menu()
