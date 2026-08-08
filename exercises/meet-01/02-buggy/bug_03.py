# bug_03.py
# Bug: Fungsi Tidak Mengembalikan Nilai

# ============================================================
# MISI KAMU
# ============================================================
# Fungsi "hitung_diskon" harusnya mengembalikan harga setelah diskon. harga setelah diskon namanya harga_akhir
# Tapi hasilnya selalu "None". Ada yang kurang — cari dan perbaiki.

def hitung_diskon(harga, persen_diskon):
    diskon = harga * (persen_diskon / 100)
    harga_akhir = harga - diskon #harga bersih yang harus dibayar
    # seharusnya ada sesuatu di sini...
    return  harga_akhir 

harga_sepatu = 200000
harga_bayar = hitung_diskon(harga_sepatu, 20) #harga-(harga*persen diskon/100) = 200000-(200000*20/100) = 200000-40000 = 160000

print("Harga setelah diskon:", harga_bayar)

# Output yang seharusnya:
# Harga setelah diskon: 160000.0

# ---- Petunjuk ----
# Fungsi sudah menghitung harga_akhir dengan benar.
# Tapi nilainya tidak keluar dari fungsi.
# Apa kata kunci yang diperlukan untuk mengembalikan nilai?
