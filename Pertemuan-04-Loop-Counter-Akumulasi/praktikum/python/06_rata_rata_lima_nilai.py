total = 0

for i in range(1, 6):
    nilai = float(input(f"Nilai ke-{i}: "))
    total += nilai

rata_rata = total / 5
print(f"Total     : {total:.2f}")
print(f"Rata-rata : {rata_rata:.2f}")
