# 05_boolean.py
# Topik: Boolean & Operator Perbandingan

# ============================================================
# BAGIAN 1 — Tebak dulu, baru jalankan
# ============================================================
# Aturannya: tulis tebakan kamu di bagian "???"
# baru setelah itu jalankan untuk ngecek.
#
# Ingat: hasil boolean cuma dua pilihan — True atau False

umur = 17

print(umur >= 18)        # tebak: False
print(umur == 17)        # tebak: True
print(umur != 20)        # tebak: True
print(not (umur >= 18))  # tebak: True

# Coba jawab dulu sebelum jalankan:
# - Kenapa baris pertama hasilnya False?
😶‍🌫️ Baris pertama print(umur >=18) yang artinya umur lebih besar dari 18 yang disini diketahui umur=17 , berarti pernyataan ini salah atau False
# - Apa perbedaan == dengan >=?
😶‍🌫️ == untuk mengecek nilai kesamaan (sama dengan) nilainya sedangkan >= untuk lebih besar atau sama dengan
# - Apa yang dilakukan "not" terhadap hasil boolean?
😶‍🌫️ not disini untuk mengembalikan atau kebalikan dari nilai yang dihasilkan sebelumnya.semacam negasi


# ============================================================
# BAGIAN 2 — Lengkapi kodenya
# ============================================================
# Ganti setiap None dengan ekspresi boolean yang benar.
# Kalau output-nya masih None, berarti belum kamu ganti.

nilai = 75

# Apakah nilai lebih besar atau sama dengan 60?
lulus = nilai >=60           # ganti ini

# Apakah nilai kurang dari 75?
butuh_remedial = nilai <75  # ganti ini

print("Lulus:", lulus)
print("Perlu remedial:", butuh_remedial)

# Output yang seharusnya muncul:
# Lulus: True
# Perlu remedial: False

#output:bener ✅
Lulus: True
Perlu remedial: False