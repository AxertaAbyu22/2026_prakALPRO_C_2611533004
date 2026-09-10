is_lulus_3004 = True
is_cumlaude_3004 = True

# menggunakan Boolean
nilai_3004= 85
batas_lulus_3004= 75

# menggunakan nilai Boolean dari kondisi
status_kelulusan_3004 = nilai_3004 >= batas_lulus_3004 # Hasilnya akan True

print("=== cek kelulusan ===")
print("Nilai:", nilai_3004)
print("Apakah lulus?:", status_kelulusan_3004)
if is_lulus_3004 and is_cumlaude_3004:
    print("Selamat, anda lulus dengan predikat cumlaude!")