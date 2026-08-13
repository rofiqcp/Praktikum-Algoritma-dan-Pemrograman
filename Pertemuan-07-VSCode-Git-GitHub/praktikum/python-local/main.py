from utils import hitung_diskon
try: total=float(input("Total belanja: "))
except ValueError: print("Harus angka"); raise SystemExit(1)
member=input("Member? y/n: ").lower()=="y"
try: diskon=hitung_diskon(total,member)
except ValueError as e: print(e); raise SystemExit(1)
print("Diskon:",diskon,"Bayar:",total-diskon)
