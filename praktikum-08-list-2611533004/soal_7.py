menus = ["Nasi Goreng", "Mie Ayam", "Soto"]
number_of_days = 3
sales = []

for hari in range(1, number_of_days + 1):
    baris_penjualan = []
    for nama_menu in menus:
        jumlah_porsi = int(input(f"Day {hari}, {nama_menu}: "))
        baris_penjualan.append(jumlah_porsi)
    sales.append(baris_penjualan)

print("Total per day:")
for indeks_hari in range(number_of_days):
    total_harian = 0
    for indeks_menu in range(len(menus)):
        total_harian += sales[indeks_hari][indeks_menu]
    print(f"Day {indeks_hari + 1}: {total_harian}")

menu_totals = []
for indeks_menu in range(len(menus)):
    total_per_menu = 0
    for indeks_hari in range(number_of_days):
        total_per_menu += sales[indeks_hari][indeks_menu]
    menu_totals.append((menus[indeks_menu], total_per_menu))

print("Total per menu:", menu_totals)

menu_terlaris, porsi_terbanyak = menu_totals[0]
for name, total in menu_totals:
    if total > porsi_terbanyak:
        menu_terlaris = name
        porsi_terbanyak = total

print(f"Best seller: {menu_terlaris} ({porsi_terbanyak})")