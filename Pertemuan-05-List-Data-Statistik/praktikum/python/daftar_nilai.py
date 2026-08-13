def statistik(data):
    if not data: return None
    return {"rata":sum(data)/len(data),"max":max(data),"min":min(data),"lulus":sum(n>=75 for n in data)}

def main():
    try: jumlah=int(input("Jumlah siswa: "))
    except ValueError: print("Harus integer"); return
    if jumlah<=0: print("Harus > 0"); return
    data=[]
    for i in range(jumlah):
        while True:
            try: n=float(input(f"Nilai {i+1}: "))
            except ValueError: print("Harus angka"); continue
            if 0<=n<=100: data.append(n); break
            print("Nilai 0-100")
    print(data, statistik(data))
if __name__=="__main__": main()
