# 02_tebak_output_02.py
# Topik: Operator Aritmatika

# ============================================================
# BAGIAN 1 — Tebak dulu, baru jalankan
# ============================================================
# Perhatikan operator yang dipakai di setiap baris.
# Tuliskan hasil tebakanmu sebelum menjalankan kode.

a = 10
b = 3

print(a + b)    # tebak: 13   → penjumlahan
print(a - b)    # tebak: 7   → pengurangan
print(a * b)    # tebak: 30   → perkalian
print(a / b)    # tebak: 3.333...   → pembagian biasa
print(a // b)   # tebak: 3   → pembagian bulat (buang koma)
print(a % b)    # tebak: 1   → sisa bagi (modulo)
print(a ** b)   # tebak: 1000   → pangkat

# Pertanyaan setelah jalankan:
# - Kenapa a / b hasilnya beda dengan a // b?
😶‍🌫️ print (a/b) ini pembagian biasa yang hasilnya terdapat koma/sisanya tetap diitung dan termasuk kedalam tipe data float.
😶‍🌫️ print (a//b) ini pembagian bulat yang hasilnya dibulatkan kebawah menuju biangan bulat yang terdekat,tipe datanya bisa int atau float tergantung tipe data awalnya.
# - Apa kegunaan operator % di kehidupan nyata?
😶‍🌫️ % atau operator modulo ini untuk menghitung sisa dari bagi, nah dikehidupan nyata misalnya:
a = 10 (buah apel)
b = 3 (dibagi untuk 3 orang)
maka a % b = 10%3 = 1 (sisanya 1 buah apel dan bisa untuk disimpan untuk nanti)
#   (Hint: cek apakah angka genap atau ganjil)
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

# ============================================================
# BAGIAN 2 — Prediksi tanpa jalankan
# ============================================================
# Tanpa menjalankan, tulis jawaban kamu di komentar.

x = 7
y = 2

# Berapa hasilnya?
# x + y * 3        → 7+(2*3)=7+6=13   (ingat urutan operasi!)
# (x + y) * 3      → (7+2)*3=9*3=27)
# x % y            → 7%2 = 3 (sisa 1) jawabannya adalah 1
# x ** 2 + y       → 7**2+2= (** pangkat) = 49+2=51
