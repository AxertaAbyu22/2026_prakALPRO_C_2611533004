#program menghitung diskon belanja

# input dari user
total_belanja_3004 = float(input("Masukan Total Belanja (Rp) :"))

# input status member (mengecek apakah user mengetik 'y' atau 'ya')
input_member_3004 = input(" Apakah Anda Member? (y/t): ").strip().lower()
is_member_3004 = input_member_3004 in ["y" ,"ya"]

# input status member (mengecek apakah user mengetik 'y' atau 'ya')
input_promo_3004 = input(" Apakah Kode promo Valid? (y/t): ").strip().lower()
kode_promo_valid_3004 = input_promo_3004 in ["y" ,"ya"]

total_diskon_persen_3004 = 0

if total_belanja_3004 > 1000000:
    total_diskon_persen_3004 += 10 # diskon belanja besar

if is_member_3004:
    total_diskon_persen_3004 += 5 # diskon belanja member

if kode_promo_valid_3004 :
    total_diskon_persen_3004 += 15 # diskon belanja vocher

# mengihutung nominal diskon dan total bayar
nominal_diskon_3004 = total_belanja_3004 * (total_diskon_persen_3004 / 100)
total_bayar_3004 = total_belanja_3004 * nominal_diskon_3004

# output hasil
print("\n --- Rincian Pembayaran")
print(f"Total Diskon    : (total_diskon_persen_3004)% (Rp {nominal_diskon_3004:,.0f})")
print(f"Total Bayar     : Rp {total_bayar_3004:,.0f}")

print(f"Total diskon yang Anda dapatkan : {total_diskon_persen_3004}%")
# Output : total diskon yang anda dapatkan : 30% jika belanja > 1 juta, member, dan kode promo valid