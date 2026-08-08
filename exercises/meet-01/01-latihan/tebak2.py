#BAGIAN 1
a = 10
b = 3

print(a + b) #output 13 
print(a - b) #output 7
print(a * b) #output 30
print(a / b) #output 3.333...
print(a // b) #output 3
print(a % b) #output 1
print(a ** b) #output 1000

#=====================================
#Hint untuk cek ganjil atau genap

a = 10
b = 3

# 1. Penjumlahan
hasil_tambah = a + b
print(f"Hasil {a} + {b} = {hasil_tambah}")
if hasil_tambah % 2 == 0:
    print("-> Hasilnya Genap")
else:
    print("-> Hasilnya Ganjil")

# 2. Pengurangan
hasil_kurang = a - b
print(f"Hasil {a} - {b} = {hasil_kurang}")
if hasil_kurang % 2 == 0:
    print("-> Hasilnya Genap")
else:
    print("-> Hasilnya Ganjil")

# 3. Perkalian
hasil_kali = a * b
print(f"Hasil {a} * {b} = {hasil_kali}")
if hasil_kali % 2 == 0:
    print("-> Hasilnya Genap")
else:
    print("-> Hasilnya Ganjil")

# 4. Pembagian Bulat (Floor Division)
hasil_bagi_bulat = a // b
print(f"Hasil {a} // {b} = {hasil_bagi_bulat}")
if hasil_bagi_bulat % 2 == 0:
    print("-> Hasilnya Genap")
else:
    print("-> Hasilnya Ganjil")

# 5. Sisa Bagi (Modulo)
hasil_modulo = a % b
print(f"Hasil {a} % {b} = {hasil_modulo}")
if hasil_modulo % 2 == 0:
    print("-> Hasilnya Genap")
else:
    print("-> Hasilnya Ganjil")

# 6. Perpangkatan
hasil_pangkat = a ** b
print(f"Hasil {a} ** {b} = {hasil_pangkat}")
if hasil_pangkat % 2 == 0:
    print("-> Hasilnya Genap")
else:
    print("-> Hasilnya Ganjil")

#outputnya:
Hasil 10 + 3 = 13
-> Hasilnya Ganjil
Hasil 10 - 3 = 7
-> Hasilnya Ganjil
Hasil 10 * 3 = 30
-> Hasilnya Genap
Hasil 10 // 3 = 3
-> Hasilnya Ganjil
Hasil 10 % 3 = 1
-> Hasilnya Ganjil
Hasil 10 ** 3 = 1000
-> Hasilnya Genap

#================================================
#BAGIAN 2 di soal langsung

