def diskon(total, member):
    if total < 0: raise ValueError("Total tidak boleh negatif")
    if member and total >= 200_000: return .15
    if member or total >= 200_000: return .10
    if total >= 100_000: return .05
    return 0

if __name__ == "__main__":
    total=float(input("Total belanja: ")); member=input("Member? (y/n): ").lower()=="y"
    r=diskon(total,member); print(f"Diskon {r:.0%}; bayar Rp{total-total*r:,.0f}")
