angka1_3004 = int(input("Input angka-1_3004: "))
angka2_3004 = int(input("Input angka-2_3004: "))

#Penjumlahan
hasil_3004= angka1_3004 + angka2_3004
print("\nOperator Penjumlahan",)
print("Hasil_3004 = ", hasil_3004)

#pengurangan
hasil_3004= angka1_3004 - angka2_3004
print("\nOperator Pengurangan",)
print("Hasil_3004 = ", hasil_3004)

#perkalian
hasil_3004= angka1_3004 * angka2_3004
print("\nOperator Perkalian",)
print("Hasil_3004 = ", hasil_3004)

#pembagian,pembagian bulat, dan sisa bagi
if angka2_3004 != 0:
    hasil_3004= angka1_3004 / angka2_3004
    print("\nOperator Pembagian",)
    print("Hasil_3004 = ", hasil_3004)

    hasil_3004= angka1_3004 // angka2_3004
    print("\nOperator Pembagian Bulat",)
    print("Hasil_3004 = ", hasil_3004)

    hasil_3004= angka1_3004 % angka2_3004
    print("\nOperator sisa bagi",)
    print("Hasil_3004 = ", hasil_3004)
else:
    print("Angka-2_3004 tidak boleh nol untuk operasi pembagian, pembagian bulat, dan sisa bagi.")  

#Pangkat
hasil_3004= angka1_3004 ** angka2_3004
print("\nOperator pangkat",)
print("Hasil_3004 = ", hasil_3004)