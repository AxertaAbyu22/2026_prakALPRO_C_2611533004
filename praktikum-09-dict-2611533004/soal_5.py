n = int(input())
kas = {}

for i in range(n):
    nama, nominal = input().split()
    nominal = int(nominal)
    
    if nama in kas:
        kas[nama] = kas[nama] + nominal
    else:
        kas[nama] = nominal

total_kas = 0
nama_terbesar = ""
nominal_terbesar = 0

for nama, total in kas.items():
    print(f"{nama}: {total}")
    total_kas = total_kas + total
    if total > nominal_terbesar:
        nama_terbesar = nama
        nominal_terbesar = total

print(f"Total cash: {total_kas}")
print(f"Top contributor: {nama_terbesar} ({nominal_terbesar})")