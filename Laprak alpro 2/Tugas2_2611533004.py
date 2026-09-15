from typing import Final
# Konstanta batas kelulusan
BATAS_LULUS: Final = 75.0

print("=== SISTEM REGISTRASI PRAKTIKAN ALPRO 2026 ===")
nama_3004 = input("Masukkan Nama Mahasiswa\t\t: ")
jenis_kelamin_3004 = input("Masukkan Jenis Kelamin (L/P)\t: ")
umur_3004 = int(input("Masukkan Umur\t\t\t: "))
skor_tes_3004 = float(input("Masukkan Skor Tes Awal\t\t: "))

# Deklarasi alamat secara multiline
alamat_3004 = """Jalan Belibis Blok A no 5,
    Kecamatan Padang Utara, Kelurahaan Air Tawar Barat,
    Kota Padang"""

# Token identifikasi menggunakan bilangan kompleks
token_3004 = 100+3j

# Evaluasi status kelulusan
status_lulus_3004 = skor_tes_3004 >= BATAS_LULUS

print("\n=== DATA PRAKTIKAN & HASIL PEMERIKSAAN ===")
print("Nama Mahasiswa\t:", nama_3004, "| Tipe:", type(nama_3004))
print("Jenis Kelamin\t:", jenis_kelamin_3004, "| Tipe:", type(jenis_kelamin_3004))
print("Alamat Domisili\t:\n" + alamat_3004, "\n| Tipe:", type(alamat_3004))
print("Umur\t\t:", umur_3004, "tahun | Tipe:", type(umur_3004))
print("Skor Tes Awal\t:", skor_tes_3004, "| Tipe:", type(skor_tes_3004))
print("ID Token Sinyal\t:", token_3004, "| Tipe:", type(token_3004))

print("\n=== STATUS KELULUSAN PRAKTIKUM ===")
print("Batas Minimum Nilai:", BATAS_LULUS)
print("Apakah Dinyatakan Lulus?:", status_lulus_3004, "| Tipe:", type(status_lulus_3004))