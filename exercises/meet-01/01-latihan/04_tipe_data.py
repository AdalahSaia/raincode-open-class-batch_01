# 04_tipe_data.py
# Topik: Tipe Data — int, float, str, bool

# ============================================================
# BAGIAN 1 — Tebak tipe datanya
# ============================================================
# Sebelum dijalankan, tebak tipe data apa yang akan muncul.
# Pilihan: <class 'int'>, <class 'float'>, <class 'str'>, <class 'bool'>

nama      = "Sari"
umur      = 21
tinggi    = 160.5
mahasiswa = True

print(type(nama))        # tebak: ???
print(type(umur))        # tebak: ???
print(type(tinggi))      # tebak: ???
print(type(mahasiswa))   # tebak: ???

# Pertanyaan:
# - Kenapa 160.5 bukan int?
# - Kenapa "21" berbeda dengan 21 di Python?


# ============================================================
# BAGIAN 2 — Jebakan tipe data
# ============================================================
# Tebak tipe data dari variabel-variabel ini.
# Hati-hati, beberapa tidak sesederhana kelihatannya.

a = "100"       # tebak: ???
b = 100         # tebak: ???
c = 100.0       # tebak: ???
d = True        # tebak: ???
e = "True"      # tebak: ???
f = 3 + 2       # tebak: ???
g = 3 + 2.0     # tebak: ???

print(type(a), type(b), type(c))
print(type(d), type(e))
print(type(f), type(g))

# Pertanyaan:
# - Apakah a dan b bisa dijumlahkan langsung? Kenapa?
# - Apa perbedaan d dan e?
# - Kenapa g berbeda dengan f padahal angkanya hampir sama?


# ============================================================
# BAGIAN 3 — Isi yang benar
# ============================================================
# Ganti None dengan nilai yang sesuai tipe datanya.
# Jangan pakai tipe data yang salah!

# Butuh integer (angka tahun):
tahun_lahir = None   # ganti dengan angka tahun lahirmu

# Butuh float (nilai IPK):
ipk = None           # ganti dengan angka desimal, contoh: 3.75

# Butuh string (nama kota):
kota = None          # ganti dengan nama kotamu dalam tanda kutip

# Butuh boolean (apakah sudah makan siang?):
sudah_makan = None   # ganti dengan True atau False

print(tahun_lahir, ipk, kota, sudah_makan)
