def main():
    items=[]
    while True:
        print("\n1 Tambah  2 Lihat  3 Cari  4 Hapus  0 Keluar")
        p=input("Pilih: ").strip()
        if p=="1":
            nama=input("Item: ").strip()
            if nama: items.append(nama)
        elif p=="2": print(items if items else "Daftar kosong")
        elif p=="3":
            q=input("Cari: ").strip().lower(); hasil=[x for x in items if q in x.lower()]; print(hasil or "Tidak ditemukan")
        elif p=="4":
            nama=input("Hapus item persis: ").strip()
            try: items.remove(nama)
            except ValueError: print("Item tidak ditemukan")
        elif p=="0": break
        else: print("Pilihan tidak valid")

if __name__ == "__main__": main()
