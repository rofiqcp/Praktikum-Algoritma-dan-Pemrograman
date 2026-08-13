def pola(n):
    for baris in range(1,n+1):
        for _ in range(baris):
            print("*", end="")
        print()

if __name__ == "__main__":
    n=int(input("Jumlah baris: "))
    if n <= 0: print("Jumlah baris harus > 0")
    else: pola(n)
