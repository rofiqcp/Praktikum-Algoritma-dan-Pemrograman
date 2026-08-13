from app import tambah_item,cari_item,hapus_item,statistik

def main():
    data=[]
    while True:
        print("\n1 Tambah  2 Lihat  3 Cari  4 Hapus  5 Statistik  0 Keluar")
        p=input("Pilih: ").strip()
        try:
            if p=="1": print("Ditambah:",tambah_item(data,input("Nama: "),float(input("Nilai: "))))
            elif p=="2": print(data if data else "Belum ada data")
            elif p=="3": print(cari_item(data,input("Cari nama: ")) or "Tidak ditemukan")
            elif p=="4": print("Terhapus" if hapus_item(data,input("Nama: ")) else "Tidak ditemukan")
            elif p=="5": print(statistik(data))
            elif p=="0": break
            else: print("Pilihan tidak valid")
        except ValueError as e: print("Error:",e)

if __name__ == "__main__": main()
