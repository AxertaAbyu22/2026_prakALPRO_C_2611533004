# Soal: Buatlah program untuk menampilkan output dibawah menggunakan perulangan for
# Ex: Masukkan tinggi segitiga: 5
# Output:
#     *
#    * *
#   * * *
#  * * * *
# * * * * *

tinggi_3004 = int(input("Masukkan tinggi segitiga: "))

for i_3004 in range(1, tinggi_3004 + 1):
    for j_3004 in range(tinggi_3004 - i_3004):
        print(" ", end="")
    for k_3004 in range(i_3004):
        print("* ", end="")
    print()