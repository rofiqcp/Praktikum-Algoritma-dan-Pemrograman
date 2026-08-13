from utils import hitung_diskon
assert hitung_diskon(200_000,True)==20_000
assert hitung_diskon(50_000,True)==0
assert hitung_diskon(200_000,False)==0
try: hitung_diskon(-1,True)
except ValueError: pass
else: raise AssertionError("negatif harus ditolak")
print("Semua test lulus")
