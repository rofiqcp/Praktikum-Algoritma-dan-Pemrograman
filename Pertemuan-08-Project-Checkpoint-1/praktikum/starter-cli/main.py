MENU={"nasi goreng":15000,"mie":12000,"teh":5000}
keranjang=[]
def tampilkan_menu():
    for nama,harga in MENU.items(): print(f"- {nama}: Rp{harga:,.0f}")
def tambah():
    nama=input("Item: ").strip().lower()
    if nama not in MENU: print("Tidak ditemukan"); return
    try: jumlah=int(input("Jumlah: "))
    except ValueError: print("Harus integer"); return
    if jumlah<=0: print("Harus >0"); return
    keranjang.append({"nama":nama,"jumlah":jumlah,"harga":MENU[nama]})
def ringkasan():
    total=0
    for x in keranjang:
        sub=x["jumlah"]*x["harga"]; total+=sub; print(x["nama"],x["jumlah"],sub)
    print("TOTAL",total)
def main():
    while True:
        p=input("\n1 Menu 2 Tambah 3 Ringkasan 4 Keluar: ")
        if p=="1": tampilkan_menu()
        elif p=="2": tambah()
        elif p=="3": ringkasan()
        elif p=="4": break
        else: print("Pilihan invalid")
if __name__=="__main__": main()
