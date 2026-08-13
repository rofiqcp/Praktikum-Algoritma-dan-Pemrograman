def tambah_item(data,nama,nilai):
    nama=nama.strip()
    if not nama: raise ValueError("nama wajib diisi")
    if nilai < 0: raise ValueError("nilai tidak boleh negatif")
    if any(x["nama"].lower()==nama.lower() for x in data): raise ValueError("data duplikat")
    item={"nama":nama,"nilai":nilai}; data.append(item); return item

def cari_item(data,nama):
    return next((x for x in data if x["nama"].lower()==nama.strip().lower()),None)

def hapus_item(data,nama):
    item=cari_item(data,nama)
    if item is None: return False
    data.remove(item); return True

def statistik(data):
    if not data: return {"jumlah":0,"total":0,"rata":0}
    total=sum(x["nilai"] for x in data)
    return {"jumlah":len(data),"total":total,"rata":total/len(data)}
