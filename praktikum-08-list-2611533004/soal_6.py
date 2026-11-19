LAST_DIGIT = 4
daily_limit = 30000 + LAST_DIGIT * 1000
expenses = []

for hari in range(1, 8):
    nominal = int(input(f"Day {hari}: "))
    expenses.append(nominal)

total_pengeluaran = 0
pengeluaran_tertinggi = expenses[0]
hari_tertinggi = 1
jumlah_hari_lewat_batas = 0

for indeks in range(len(expenses)):
    total_pengeluaran += expenses[indeks]
    if expenses[indeks] > pengeluaran_tertinggi:
        pengeluaran_tertinggi = expenses[indeks]
        hari_tertinggi = indeks + 1
    if expenses[indeks] > daily_limit:
        jumlah_hari_lewat_batas += 1

rata_rata = total_pengeluaran / len(expenses)

print(f"Daily limit: {daily_limit}")
print(f"Total: {total_pengeluaran}")
print(f"Average: {rata_rata:.1f}")
print(f"Highest: day {hari_tertinggi} ({pengeluaran_tertinggi})")
print(f"Days above limit: {jumlah_hari_lewat_batas}")