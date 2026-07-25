# 03_biodata.py
# Solusi Challenge Hard — Form Biodata dengan Kondisi

# Minta input:
nama  = input("Nama lengkap : ")
umur  = int(input("Umur         : "))
kota  = input("Kota asal    : ")
hobi  = input("Hobi         : ")

# Tampilkan biodata:
print("================================")
print("BIODATA")
print("================================")
print(f"Nama   : {nama}")
print(f"Umur   : {umur} tahun")
print(f"Kota   : {kota}")
print(f"Hobi   : {hobi}")
print("================================")

# Tambahkan kondisi-kondisinya:
# Sengaja pakai TIGA blok "if" terpisah, bukan "elif" — ketiga
# kondisi ini independen dan bisa muncul bersamaan.
if umur >= 17:
    print("Status: Sudah bisa buat KTP")
else:
    print("Status: Belum waktunya buat KTP")

if kota == "Jakarta":
    print("Catatan: Warga ibukota!")

if hobi == "coding" or hobi == "programming":
    print("Catatan: Calon programmer sejati!")


# ============================================================
# BONUS — kategori umur
# ============================================================
if umur < 13:
    print("Kategori: Anak-anak")
elif umur < 18:
    print("Kategori: Remaja")
elif umur < 60:
    print("Kategori: Dewasa")
else:
    print("Kategori: Lansia")
