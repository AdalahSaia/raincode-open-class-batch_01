# 03_biodata.py
# Challenge: Form Biodata dengan Kondisi

# ============================================================
# CERITA
# ============================================================
# Buat program yang meminta biodata seseorang,
# lalu menampilkan rangkumannya dengan beberapa kondisi
# yang disesuaikan dengan data yang dimasukkan.

# ============================================================
# SPESIFIKASI PROGRAM
# ============================================================
# 1. Minta input berikut dari user:
#    - Nama lengkap
#    - Umur (dalam angka)
#    - Kota asal
#    - Hobi
#
# 2. Tampilkan biodata dalam format rapi:
#    ================================
#    BIODATA
#    ================================
#    Nama   : <nama>
#    Umur   : <umur> tahun
#    Kota   : <kota>
#    Hobi   : <hobi>
#    ================================
#
# 3. Tambahkan kondisi-kondisi ini setelah biodata:
#    - Kalau umur >= 17       → "Status: Sudah bisa buat KTP"
#    - Kalau umur < 17        → "Status: Belum waktunya buat KTP"
#    - Kalau kota == "Jakarta" → "Catatan: Warga ibukota!"
#    - Kalau hobi == "coding" atau hobi == "programming"
#                             → "Catatan: Calon programmer sejati!"

# ============================================================
# TULIS KODE DI SINI
# ============================================================

# Minta input:
nama  = input("Nama lengkap : ")
umur  = int(input("Umur         : "))
kota  = input("Kota asal    : ")
hobi  = input("Hobi         : ")

# Tampilkan biodata:


# Tambahkan kondisi-kondisinya:


# ============================================================
# BONUS (opsional)
# ============================================================
# Tambahkan satu kondisi lagi berdasarkan umur:
#   < 13 tahun     → "Kategori: Anak-anak"
#   13 - 17 tahun  → "Kategori: Remaja"
#   18 - 59 tahun  → "Kategori: Dewasa"
#   >= 60 tahun    → "Kategori: Lansia"
