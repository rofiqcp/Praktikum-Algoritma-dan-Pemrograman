from utils import hitung_diskon,hitung_bayar,format_rupiah

def main():
    try:
        total=float(input("Total belanja: "))
        member=input("Member? (y/n): ").strip().lower()=="y"
        print("Diskon:",format_rupiah(hitung_diskon(total,member)))
        print("Bayar :",format_rupiah(hitung_bayar(total,member)))
    except ValueError as e:
        print("Input tidak valid:",e)

if __name__ == "__main__": main()
