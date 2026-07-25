# 00_panduan_syntax.py
# Panduan Sintaks Python — Pertemuan 1
#
# File ini BUKAN latihan.
# Ini referensi — buka kalau lupa cara nulis sesuatu.
# Semua kode di sini bisa langsung dijalankan.
# ============================================================


# ============================================================
# 1. VARIABEL
# ============================================================

nama    = "Budi"        # string  → pakai tanda kutip
umur    = 20            # integer → angka bulat
tinggi  = 170.5         # float   → angka desimal
aktif   = True          # boolean → True atau False


# ============================================================
# 2. PRINT — berbagai cara
# ============================================================

# Cara 1 — langsung
print("Halo dunia")

# Cara 2 — cetak variabel
print(nama)
print(umur)

# Cara 3 — gabung string dengan +
#           (variabelnya harus string dulu!)
print("Nama: " + nama)
print("Umur: " + str(umur) + " tahun")   # int harus diubah ke str

# Cara 4 — pakai koma (otomatis ada spasi)
print("Nama:", nama, "| Umur:", umur)

# Cara 5 — f-string (paling bersih, direkomendasikan)
print(f"Nama: {nama}, umur: {umur} tahun")
print(f"Tinggi: {tinggi} cm")


# ============================================================
# 3. KARAKTER KHUSUS DI STRING
# ============================================================

# \n → pindah baris
print("Baris pertama\nBaris kedua\nBaris ketiga")

# \t → tab (indentasi)
print("Nama:\tBudi")
print("Kota:\tBandung")

# Kombinasi
print("Menu:\n\t1. Makan\n\t2. Minum\n\t3. Tidur")

# String dikali angka → diulang
print("-" * 30)
print("halo " * 3)
print("=" * 30)


# ============================================================
# 4. INPUT DARI USER
# ============================================================

# input() selalu menghasilkan string
# nama_user = input("Masukkan nama: ")
# print("Halo,", nama_user)

# Kalau butuh angka, konversi dulu
# umur_user  = int(input("Umur: "))       # ke integer
# berat_user = float(input("Berat: "))    # ke float

# Contoh lengkap (uncomment untuk coba):
# nama_user = input("Nama kamu: ")
# umur_user = int(input("Umur kamu: "))
# print(f"Halo {nama_user}, umur {umur_user} tahun.")


# ============================================================
# 5. TIPE DATA & KONVERSI
# ============================================================

# Cek tipe data
print(type("teks"))     # <class 'str'>
print(type(10))         # <class 'int'>
print(type(3.14))       # <class 'float'>
print(type(True))       # <class 'bool'>

# Konversi antar tipe
angka_str = "42"
angka_int = int(angka_str)      # str → int
angka_flt = float(angka_str)    # str → float
balik_str = str(angka_int)      # int → str

print(type(angka_int), angka_int)
print(type(angka_flt), angka_flt)


# ============================================================
# 6. OPERATOR
# ============================================================

a = 10
b = 3

# Aritmatika
print(a + b)    # 13   → penjumlahan
print(a - b)    # 7    → pengurangan
print(a * b)    # 30   → perkalian
print(a / b)    # 3.33 → pembagian (hasil float)
print(a // b)   # 3    → pembagian bulat
print(a % b)    # 1    → sisa bagi
print(a ** b)   # 1000 → pangkat

# Perbandingan (hasilnya boolean)
print(a > b)    # True
print(a == b)   # False
print(a != b)   # True
print(a >= 10)  # True

# Logika
print(True and False)   # False
print(True or False)    # True
print(not True)         # False


# ============================================================
# 7. IF / ELIF / ELSE
# ============================================================

nilai = 75

if nilai >= 90:
    print("Grade A")
elif nilai >= 80:
    print("Grade B")
elif nilai >= 70:
    print("Grade C")
elif nilai >= 60:
    print("Grade D")
else:
    print("Grade E")

# Satu baris kondisi sederhana
x = 5
print("Genap") if x % 2 == 0 else print("Ganjil")


# ============================================================
# 8. FUNGSI
# ============================================================

# Definisi fungsi
def sapa(nama):
    return "Halo, " + nama + "!"

# Fungsi dengan beberapa parameter
def hitung_luas(panjang, lebar):
    luas = panjang * lebar
    return luas

# Fungsi yang return string
def info_umur(umur):
    if umur >= 18:
        return "Dewasa"
    else:
        return "Belum dewasa"

# Fungsi yang return variabel
def kuadrat(angka):
    hasil = angka ** 2
    return hasil

# Memanggil fungsi
pesan   = sapa("Sari")
luas    = hitung_luas(5, 3)
status  = info_umur(17)
kali    = kuadrat(4)

print(pesan)                        # Halo, Sari!
print(f"Luas: {luas}")              # Luas: 15
print(f"Status: {status}")          # Status: Belum dewasa
print(f"4 kuadrat = {kali}")        # 4 kuadrat = 16


# ============================================================
# 9. JEBAKAN UMUM
# ============================================================

# = adalah ASSIGNMENT (simpan nilai)
# == adalah COMPARISON (bandingkan nilai)
x = 10          # simpan 10 ke x
print(x == 10)  # cek apakah x sama dengan 10 → True

# String "5" bukan angka 5
print("5" + "3")    # "53"  → disambung sebagai string
print(5 + 3)        # 8     → dijumlahkan sebagai angka

# Indentasi wajib konsisten (4 spasi atau 1 tab)
# Jangan campur keduanya!
