import random

def main():
    rahasia=random.randint(1,10); percobaan=0
    while True:
        try: tebakan=int(input("Tebak 1-10: "))
        except ValueError:
            print("Masukkan bilangan bulat."); continue
        percobaan += 1
        if tebakan == rahasia:
            print(f"Benar dalam {percobaan} percobaan!"); break
        print("Terlalu kecil." if tebakan < rahasia else "Terlalu besar.")

if __name__ == "__main__": main()
