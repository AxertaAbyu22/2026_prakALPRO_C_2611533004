# Masukan nilai boolean
# Input tidak peka terhadap huruf besar dan kecil
a1_3004 = input("Masukan nilai boolean (True/False): ").strip().lower() == "true" 
a2_3004 = input("Masukan nilai boolean (True/False): ").strip().lower() == "true" 
# Menghapus spasi dan mengubah ke huruf kecil
print("\nA1_3004 =", a1_3004)
print("A2_3004 =", a2_3004)

#Kongjungsi bernilai True jika kedua operand bernilai True
hasil_3004 = a1_3004 and a2_3004
print("\nKongjungsi (AND):")
print("A1_3004 AND A2_3004 =", hasil_3004)  

#Disjungsi bernilai True jika salah satu operand bernilai True
hasil_3004 = a1_3004 or a2_3004
print("\nDisjungsi (OR):")
print("A1_3004 OR A2_3004 =", hasil_3004)

#Negasi a1_3004 membalikkan nilai a1
hasil_3004 = not a1_3004
print("\nNegasi A1_3004 (NOT):")
print("NOT A1_3004 =", hasil_3004)

#Negasi A2_3004 membalikan nilai a2
hasil_3004 = not a2_3004
print("\nNegasi A2_3004 (NOT):")
print("NOT A2_3004 =", hasil_3004)

#XOR: bernilai true jika kedua nilai berbeda
hasil_3004 = a1_3004 != a2_3004
print("\nDisjungsi Ekslusif (XOR)")
print("A1 XOR A2 =", hasil_3004)