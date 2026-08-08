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
