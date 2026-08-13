def ringkasan(data):
    if not data: return None
    return min(data),max(data),sum(data)/len(data)

if __name__ == "__main__":
    data=[]
    try:
        for i in range(7): data.append(float(input(f"Suhu hari {i+1}: ")))
    except ValueError: print("Input harus angka.")
    hasil=ringkasan(data)
    if hasil:
        mn,mx,av=hasil; print(f"Min={mn:.1f}, Max={mx:.1f}, Rata={av:.1f}")
