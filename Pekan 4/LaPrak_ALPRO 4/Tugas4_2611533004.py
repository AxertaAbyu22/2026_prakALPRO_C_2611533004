print("=== SISTEM LOKET ALPRO ADVENTURE PARK ===")
nama_3004 = input("Masukkan Nama Pengunjung        : ")
umur_3004 = int(input("Input umur anda                 : "))

# Mengambil huruf pertama dari input SIM untuk validasi yang akurat
sim_input_3004 = input("Apakah Anda Sudah Punya SIM C (y/t): ").strip().lower()
sim_3004 = sim_input_3004[0] if len(sim_input_3004) > 0 else 't'

print("\nPilihan Paket Wahana (1-5):")
print("  1. Safari Rimba         (Rp 50,000)")
print("  2. Arung Jeram          (Rp 75,000)")
print("  3. Motor ATV Ekstrim    (Rp 120,000)")
print("  4. Roller Coaster Kilat (Rp 100,000)")
print("  5. All-Access VIP       (Rp 220,000)")

paket_3004 = int(input("Masukkan nomor paket (1-5)      : "))
jumlah_tiket_3004 = int(input("Masukkan jumlah tiket           : "))
member_3004 = input("Apakah Anda member? (y/t)       : ").strip().lower()
promo_3004 = input("Apakah kode promo valid? (y/t)  : ").strip().lower()

# Variabel flag untuk menghentikan eksekusi tanpa exit() atau nested-if
validasi_3004 = True

# If Tunggal untuk validasi kelogisan tiket
if jumlah_tiket_3004 <= 0:
    print("Peringatan: Kuota tiket tidak valid!")
    validasi_3004 = False

harga_satuan_3004 = 0
nama_wahana_3004 = ""

# Match - Case beserta Case _
match paket_3004:
    case 1:
        nama_wahana_3004 = "Safari Rimba"
        harga_satuan_3004 = 50000
    case 2:
        nama_wahana_3004 = "Arung Jeram"
        harga_satuan_3004 = 75000
    case 3:
        nama_wahana_3004 = "Motor ATV Ekstrim"
        harga_satuan_3004 = 120000
    case 4:
        nama_wahana_3004 = "Roller Coaster Kilat"
        harga_satuan_3004 = 100000
    case 5:
        nama_wahana_3004 = "All-Access VIP"
        harga_satuan_3004 = 220000
    case _:
        print("Paket wahana tidak valid!")
        validasi_3004 = False

# Jika validasi_3004 bernilai False (tiket <= 0 atau paket tidak valid), 
# maka program akan melewati seluruh evaluasi di bawah ini secara otomatis.

if validasi_3004:
    print("\n--- KELAYAKAN PENGENDARA WAHANA ---")

# If - Elif - Else terstruktur tanpa Nested If (if di dalam if)
if validasi_3004 and paket_3004 == 3 and umur_3004 >= 17 and sim_3004 == 'y':
    print("Status Akses: Anda sudah dewasa dan boleh mengendarai ATV sendiri.")
elif validasi_3004 and paket_3004 == 3 and umur_3004 >= 17 and sim_3004 != 'y':
    print("Status Akses: Anda sudah dewasa tetapi tidak boleh membawa motor ATV (wajib didampingi instruktur).")
elif validasi_3004 and paket_3004 == 3 and umur_3004 < 17 and sim_3004 == 'y':
    print("Status Akses: Identitas tidak valid: Belum cukup umur memiliki SIM.")
elif validasi_3004 and paket_3004 == 3:
    print("Status Akses: Anda belum cukup umur dan tidak boleh membawa motor ATV.")
elif validasi_3004 and umur_3004 >= 10:
    print(f"Status Akses: Umur Anda mencukupi untuk wahana {nama_wahana_3004}.")
elif validasi_3004:
    print(f"Status Akses: Anda belum cukup umur untuk wahana {nama_wahana_3004} (wajib didampingi orang tua).")

# Multi-IF terpisah untuk diskon akumulatif
subtotal_3004 = harga_satuan_3004 * jumlah_tiket_3004
total_diskon_persen_3004 = 0

if validasi_3004 and subtotal_3004 >= 200000:
    total_diskon_persen_3004 += 10
if validasi_3004 and member_3004 in ['y', 'ya']:
    total_diskon_persen_3004 += 5
if validasi_3004 and promo_3004 in ['y', 'ya']:
    total_diskon_persen_3004 += 15
if validasi_3004 and jumlah_tiket_3004 >= 5:
    total_diskon_persen_3004 += 5

# Kalkulasi Nominal Diskon dan Evaluasi Akhir
if validasi_3004:
    nominal_diskon_3004 = subtotal_3004 * (total_diskon_persen_3004 / 100)
    total_bayar_3004 = subtotal_3004 - nominal_diskon_3004

    print("\n--- Rincian Pembayaran ---")
    print(f"Subtotal Belanja : Rp {subtotal_3004:,.0f}")
    print(f"Total Diskon     : {total_diskon_persen_3004}% (Rp {nominal_diskon_3004:,.0f})")
    print(f"Total Bayar      : Rp {total_bayar_3004:,.0f}")

# Evaluasi if - else penutup audit
if validasi_3004 and total_bayar_3004 > 300000:
    print("Catatan Layanan  : Selamat! Anda berhak mendapatkan Souvenir Gratis.")
elif validasi_3004:
    print("Catatan Layanan  : Terima kasih telah berkunjung.")