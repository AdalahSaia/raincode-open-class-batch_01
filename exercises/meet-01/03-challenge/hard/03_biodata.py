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
#minta input dari user
nama= input("Nama Lengkap: ") #debugging tadi kesalahan harusnya memakai = bukan :
umur= int(input("Umur: "))
kota= input("Kota Asal: ")
hobi= input("Hobi: ")

#print sesuai soal
print("================================")
print("BIODATA")
print("================================")
print(f"Nama   : {nama}")
print(f"Umur   : {umur} tahun")
print(f"Kota   : {kota}")
print(f"Hobi   : {hobi}")
print("================================")

#Cek umur
if umur >= 17:
    print("Status: Sudah bisa buat KTP")
else: #disini langsung saja karena hanya 2 pilihan kalau ga < ya >
    print("Status: Belum waktunya buat KTP")

#cek kota
if kota == "Jakarta":
    print("Catatan: Warga ibukota!")

#cek hobi memakai or untuk variabel yang belakang wajib ditulis ulang
if hobi == "coding" or hobi == "programming":
    print("Catatan: Calon programmer sejati!")
# ============================================================

#INI MASUK KE BONUS
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

#PROGRAMNYA:
#==============BAGIAN 2============
#minta input dari user
nama= input("Nama Lengkap: ") #debugging tadi kesalahan harusnya memakai = bukan :
umur= int(input("Umur: "))
kota= input("Kota Asal: ")
hobi= input("Hobi: ")

#print sesuai soal
print("================================")
print("BIODATA")
print("================================")
print(f"Nama   : {nama}")
print(f"Umur   : {umur} tahun")
print(f"Kota   : {kota}")
print(f"Hobi   : {hobi}")
print("================================")

#TAMBAHAN kondisi:
if umur < 13:
    print("Kategori: Anak-anak")
elif 13 <= umur <= 17:
    print("Kategori: Remaja")
elif 18 <= umur <= 59:
    print("Kategori: Dewasa")
elif umur >= 60:
    print("Kategori: Lansia")

#Cek umur
if umur >= 17:
    print("Status: Sudah bisa buat KTP")
else: #disini langsung saja karena hanya 2 pilihan kalau ga < ya >
    print("Status: Belum waktunya buat KTP")

#cek kota
if kota == "Jakarta":
    print("Catatan: Warga ibukota!")

#cek hobi memakai or untuk variabel yang belakang wajib ditulis ulang
if hobi == "coding" or hobi == "programming":
    print("Catatan: Calon programmer sejati!")