angka1_3004 = int(input("Input angka-1_3004: "))
angka2_3004 = int(input("Input angka-2_3004: "))

print("\nNilai angka-1_3004 =", angka1_3004)
print("Nilai angka-2_3004 =", angka2_3004)  

#Assignment biasa
hasil_3004 = angka1_3004
print("\nAssignment biasa (=)",)
print("Hasil_3004 = ", hasil_3004)

#Asignment penjumlahan
hasil_3004 += angka2_3004
print("\nAssigment penjumlahan (+=)",)
print("Hasil_3004 = ", hasil_3004)

#Assignment pengurangan
hasil_3004 -= angka2_3004
print("\nAssigment pengurangan (-=)",)
print("Hasil_3004 = ", hasil_3004)

#Assignment perkalian
hasil_3004 *= angka1_3004
hasil_3004 *= angka2_3004
print("\nAssigment perkalian (*=)",)
print("Hasil_3004 = ", hasil_3004)

#Assignment pembagian, pembagian bulat, dan sisa bagi
if angka2_3004 !=0:
  hasil_3004= angka1_3004
  hasil_3004/= angka2_3004
  print("\nAssigment pembagian (/=)",)
  print("Hasil_3004 = ", hasil_3004)
  #operator tambahan
  hasil_3004= angka1_3004
  hasil_3004//= angka2_3004
  print("\nAssigment pembagian bulat (//=)",)
  print("Hasil_3004 = ", hasil_3004)
  hasil_3004= angka1_3004
  hasil_3004 %= angka2_3004
  print("\nAssigment sisa bagi (%=)",)
  print("Hasil_3004 = ", hasil_3004)
else:
  print("\nPembagian tidak dapat dilakukan .")  
  print("Angka kedua tidak boleh nol untuk operasi pembagian, pembagian bulat, dan sisa bagi.")

# Operator tambahan: assignment perpangkatan
hasil_3004= angka1_3004
hasil_3004 **= angka2_3004
print("\nAssignment perpanggkatan (**=)")
print("Hasil_3004 =" , hasil_3004)