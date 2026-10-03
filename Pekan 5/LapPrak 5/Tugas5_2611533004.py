# === PROGRAM JAM PASIR KRISTAL PALINDROMIK (PEKAN 5) ===
print("=== PROGRAM JAM PASIR KRISTAL PALINDROMIK (PEKAN 5) ===")

# Input dinamis ukuran skala jam pasir
n_3004 = int(input("Masukkan ukuran skala jam pasir (N): "))

# 1. BINGKAI PEMBATAS ATAS
print("#", end="")
for i_3004 in range(4 * n_3004 + 5):
    print("=", end="")
print("#")

# 2. FASE 1: JAM PASIR ATAS (Dari baris N turun sampai 1)
for baris_3004 in range(n_3004, 0, -1):
    print("| ", end="")  # Sisi kiri: garis tegak dan satu spasi padding
    
    # Spasi penyeimbang kiri: 2 * (N - baris)
    for spasi_3004 in range(2 * (n_3004 - baris_3004)):
        print(" ", end="")
        
    # Deret angka mundur dari baris ke 1 dipisahkan spasi
    for angka_3004 in range(baris_3004, 0, -1):
        print(angka_3004, end=" ")
        
    # Poros kristal tengah
    print("<*>", end="")
    
    # Deret angka maju dari 1 ke baris diawali spasi
    for angka_3004 in range(1, baris_3004 + 1):
        print(" " + str(angka_3004), end="")
        
    # Spasi penyeimbang kanan: 2 * (N - baris)
    for spasi_3004 in range(2 * (n_3004 - baris_3004)):
        print(" ", end="")
        
    print(" |")  # Satu spasi padding dan garis tegak di sisi kanan

# 3. FASE 2: POROS TITIK PUSAT (Singularity)
print("|", end="")  # Garis tegak pembatas kiri
# Spasi penyeimbang kiri: 2 * N + 1
for spasi_3004 in range(2 * n_3004 + 1):
    print(" ", end="")
print("<*>", end="")  # Poros kristal tunggal
# Spasi penyeimbang kanan: 2 * N + 1
for spasi_3004 in range(2 * n_3004 + 1):
    print(" ", end="")
print("|")  # Garis tegak pembatas kanan

# 4. FASE 3: JAM PASIR BAWAH (Dari baris 1 naik sampai N)
for baris_3004 in range(1, n_3004 + 1):
    print("| ", end="")  # Sisi kiri: garis tegak dan satu spasi padding
    
    # Spasi penyeimbang kiri: 2 * (N - baris)
    for spasi_3004 in range(2 * (n_3004 - baris_3004)):
        print(" ", end="")
        
    # Deret angka mundur dari baris ke 1 dipisahkan spasi
    for angka_3004 in range(baris_3004, 0, -1):
        print(angka_3004, end=" ")
        
    # Poros kristal tengah
    print("<*>", end="")
    
    # Deret angka maju dari 1 ke baris diawali spasi
    for angka_3004 in range(1, baris_3004 + 1):
        print(" " + str(angka_3004), end="")
        
    # Spasi penyeimbang kanan: 2 * (N - baris)
    for spasi_3004 in range(2 * (n_3004 - baris_3004)):
        print(" ", end="")
        
    print(" |")  # Satu spasi padding dan garis tegak di sisi kanan

# 5. BINGKAI PEMBATAS BAWAH
print("#", end="")
for i_3004 in range(4 * n_3004 + 5):
    print("=", end="")
print("#")