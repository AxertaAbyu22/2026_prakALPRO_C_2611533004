# Buat file dengan nama multi_if2_2611533004.py
# Buat program untuk kondisional if
# Nama variabel ditambah 4 digit NIM terakhir contoh: total_belanja_3004
# program ini menggunakan fungsi input()
# Program Menghitung Diskon Belanja

# Input dari user
total_belanja_3004 = float(input("Input Total Belanja Anda (Rp): "))

# Input status member (mengecek apakah user mengetik 'y' atau 'ya')
input_member_3004 = input("Apakah Anda member? (y/t): ").strip().lower()
is_member_3004 = input_member_3004 in ["y", "ya"]

# Input status kode promo (mengecek apakah user mengetik 'y' atau 'ya')
input_promo_3004 = input("Apakah kode promo valid? (y/t): ").strip().lower()
kode_promo_valid_3004 = input_promo_3004 in ["y", "ya"]

total_diskon_persen_3004 = 0

# Multi-IF terpisah: setiap kondisi diperiksa secara independen
# Diskon bisa ditumpuk (akumulasi) jika memenuhi beberapa syarat sekaligus

if total_belanja_3004 > 1000000:
    total_diskon_persen_3004 += 10 # Diskon belanja besar

if is_member_3004:
    total_diskon_persen_3004 += 5 # Diskon member

if kode_promo_valid_3004:
    total_diskon_persen_3004 += 15 # Diskon voucher

# menghitung nominal diskon dan total bayar
nominal_diskon_3004 = total_belanja_3004 * (total_diskon_persen_3004 / 100)
total_bayar_3004 = total_belanja_3004 - nominal_diskon_3004

# Output hasil
print("\n--- Rincian Pembayaran ---")
print(f"Total Diskon : {total_diskon_persen_3004}% (Rp {nominal_diskon_3004:,.0f})")
print(f"Total Bayar  : Rp {total_bayar_3004:,.0f}")

print(f"Total diskon yang anda dapatkan: {total_diskon_persen_3004}%")
# Output: Total diskon yang anda dapatkan: 30% jika belanja > 1 juta, member, dan kode promo valid

# Output : total diskon yang anda dapatkan : 30% jika belanja > 1 juta, member, dan kode promo valid