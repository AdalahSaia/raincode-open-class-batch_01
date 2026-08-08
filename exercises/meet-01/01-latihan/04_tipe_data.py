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

print(type(nama))        # tebak: String
print(type(umur))        # tebak: integer (int)
print(type(tinggi))      # tebak: float
print(type(mahasiswa))   # tebak: boolean (bool)

# Pertanyaan:
# - Kenapa 160.5 bukan int?
😶‍🌫️ 160.5 ini merupakan angka desimal yang masuknya ke tipe data float,jika int ini untuk bilangan bulat
# - Kenapa "21" berbeda dengan 21 di Python?
😶‍🌫️ "21" ini merupakan tipe data string (terdapat petik dua) sedangkan untuk 21 ini adalah tipe data integer

# ============================================================
# BAGIAN 2 — Jebakan tipe data
# ============================================================
# Tebak tipe data dari variabel-variabel ini.
# Hati-hati, beberapa tidak sesederhana kelihatannya.

a = "100"       # tebak: String
b = 100         # tebak: int
c = 100.0       # tebak: float
d = True        # tebak: bool
e = "True"      # tebak: String
f = 3 + 2       # tebak: int (karena hasilnya adalah 5)
g = 3 + 2.0     # tebak: float (karena hasilnya adalah 5.0)

print(type(a), type(b), type(c))
print(type(d), type(e))
print(type(f), type(g))

# Pertanyaan:
# - Apakah a dan b bisa dijumlahkan langsung? Kenapa?
😶‍🌫️ diketahui a merupakan tipe data String sedangkan b merupakan tipe data integer,maka keduanya tidak bisa dijunlahkan langsung harus dikonversi dahulu
yang  bagian a (String ) menjadi integer atau bagian b (integer) menjadi String
misalkan gini:
a="100"
b=100
c=int(a)+b  = 200
atau 
c= a + str(b) = "100100"
# - Apa perbedaan d dan e?
😶‍🌫️ d= True, merupakan tipe data boolean yaitu kebenaran murni dari (True atau False). Sedangkan e="True" merupakan jenis tipe data String yang akan terbaca sebagai text biasa.
# - Kenapa g berbeda dengan f padahal angkanya hampir sama?
😶‍🌫️ f= 3 + 2 yang hasilnya adalah 5 yaitu bilangan bulat. sedangkan g= 3 + 2.0 yang hasilnya adalah 5.0 yaitu bilangan desimal.


# ============================================================
# BAGIAN 3 — Isi yang benar
# ============================================================
# Ganti None dengan nilai yang sesuai tipe datanya.
# Jangan pakai tipe data yang salah!

# Butuh integer (angka tahun):
tahun_lahir = 2004   # ganti dengan angka tahun lahirmu

# Butuh float (nilai IPK):
ipk = 3.63           # ganti dengan angka desimal, contoh: 3.75

# Butuh string (nama kota):
kota = "Bogor"         # ganti dengan nama kotamu dalam tanda kutip

# Butuh boolean (apakah sudah makan siang?):
sudah_makan = False   # ganti dengan True atau False

print(tahun_lahir, ipk, kota, sudah_makan)
# output:
# 2004 3.63 Bogor False