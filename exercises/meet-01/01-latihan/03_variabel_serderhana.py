# 03_variabel_sederhana.py
# Topik: Variabel — Menyimpan & Menampilkan Data

# ============================================================
# BAGIAN 1 — Tugas Utama
# ============================================================
# Buatlah tiga variabel untuk menyimpan data dirimu:
#   nama  → nama kamu (string)
#   umur  → umur kamu (integer)
#   kota  → kota asal kamu (string)
#
# Lalu tampilkan dengan format persis seperti ini:
#   Halo, nama saya Budi
#   Umur saya 20 tahun
#   Saya tinggal di Bandung

# Tulis kode kamu di sini:
nama = "Khafifatul"
umur = 20
kota = "Jawa Tengah"

print(f"Halo, nama saya {nama}")
print(f"Umur saya {umur} tahun")
print(f"Saya tinggal di {kota}")
#output:
Halo, nama saya Khafifatul
Umur saya 20 tahun
Saya tinggal di Jawa Tengah

# ============================================================
# BAGIAN 2 — Ubah nilai variabel
# ============================================================
# Setelah Bagian 1 berhasil, coba ini:
# Ganti nilai variabel nama dan kota dengan data orang lain,
# lalu jalankan lagi — apakah outputnya ikut berubah?
#ini setelah mengganti variabel:
nama = "Arya Mohan"
umur = 18
kota = "Asrama Gen Z"

print(f"Halo, nama saya {nama}")
print(f"Umur saya {umur} tahun")
print(f"Saya tinggal di {kota}")
#output:
Halo, nama saya Arya Mohan
Umur saya 18 tahun
Saya tinggal di Asrama Gen Z

# Ini yang bikin variabel berguna: cukup ganti nilainya di satu
# tempat, outputnya otomatis berubah di mana-mana.

# Contoh kalau sudah punya variabel nama dan kota:
# nama = "Sari"
# kota = "Surabaya"
# print("Halo, nama saya", nama)
# print("Saya tinggal di", kota)


# ============================================================
# BONUS (opsional)
# ============================================================
# Tambahkan variabel hobi, lalu cetak juga:
# "Hobi saya <hobi>"
nama = "Arya Mohan"
umur = 18
kota = "Asrama Gen Z"
hobi = "Memandangi gambar harimau di dinding"

print(f"Halo, nama saya {nama}")
print(f"Umur saya {umur} tahun")
print(f"Saya tinggal di {kota}")
print(f"Hobi saya {hobi}")
#output:
Halo, nama saya Arya Mohan
Umur saya 18 tahun
Saya tinggal di Asrama Gen Z
Hobi saya Memandangi gambar harimau di dinding