def bilangan_genap(awal, akhir):
    if awal > akhir:
        awal, akhir = akhir, awal
    return [n for n in range(awal, akhir + 1) if n % 2 == 0]

if __name__ == "__main__":
    a=int(input("Awal: ")); b=int(input("Akhir: "))
    print("Bilangan genap:", *bilangan_genap(a,b))
