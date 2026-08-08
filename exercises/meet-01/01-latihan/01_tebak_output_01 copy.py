# 01_tebak_output_01.py
# Topik: Variabel & print()

# ============================================================
# BAGIAN 1 — Tebak dulu, baru jalankan
# ============================================================
# Tulis tebakan kamu di bagian "???" sebelum menjalankan.
# Setelah kamu tulis, baru jalankan dan bandingkan.

nama = "Andi"
umur = 20

print(nama)          # tebak: Andi
print(umur)          # tebak: 20
print(type(nama))    # tebak: <class 'str'>
print(type(umur))    # tebak: <class 'int'>

# Pertanyaan:
# - Kenapa print(nama) tidak mencetak huruf n-a-m-a, tapi isinya?
😶‍🌫️Karena nama di print(nama) merupakan bentuk variabel dengan string Andi,maka output yang akan dicetak adalah isi dari variabel nama yaitu Andi (atau nama lain disini).
# - Apa perbedaan output print("Andi") vs print(nama)?
😶‍🌫️Outpit print("Andi") menghasilkan Andi dalam bentuk string biasa,jika diubah nilainya akan tetap menghasilkan Andi
😶‍🌫️Output print(nama) akan menghasilkan Andi dalam bentuk nilai yang tersimban di variabel nama,jika nilainya diubah maka akan ikut berubah

misalnya gini:
nama = "susi"
umur = 20

print("Andi") #output Andi
print(nama) #output susi


# ============================================================
# BAGIAN 2 — Modifikasi kecil
# ============================================================
# Ubah nilai variabel di bawah ini sesuai data kamu sendiri,
# lalu jalankan lagi dan lihat hasilnya.

nama = "???"   # ganti dengan namamu
umur = 0       # ganti dengan umurmu

print("Nama saya:", nama)
print("Umur saya:", umur, "tahun")
#output:
#Nama saya: ???
#Umur saya: 0 tahun

#===============================================================
nama = "Khafifatul"   # ganti dengan namamu
umur = 20       # ganti dengan umurmu

print("Nama saya:", nama)
print("Umur saya:", umur, "tahun")
#output:
#Nama saya: Khafifatul
#Umur saya: 20 tahun