number_of_rows = 4
seats_per_row = 5

denah_kursi = [["." for _ in range(seats_per_row)] for _ in range(number_of_rows)]
kursi_terisi = 0

while True:
    for baris in range(number_of_rows):
        print(f"Row {baris + 1}:", " ".join(denah_kursi[baris]))
    pilih_baris = int(input("Row (0 to stop): "))
    if pilih_baris == 0:
        break
    pilih_kursi = int(input("Seat: "))

    if not (1 <= pilih_baris <= number_of_rows and 1 <= pilih_kursi <= seats_per_row):
        print("Invalid seat.")
    elif denah_kursi[pilih_baris - 1][pilih_kursi - 1] == "X":
        print("Seat already taken.")
    else:
        denah_kursi[pilih_baris - 1][pilih_kursi - 1] = "X"
        kursi_terisi += 1
        print("Seat booked.")

print(f"Seats taken: {kursi_terisi}")