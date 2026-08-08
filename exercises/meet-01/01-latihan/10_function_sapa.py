# 10_function_sapa.py
# Topik: Fungsi — Definisi & Pemanggilan

# ============================================================
# BAGIAN 1 — Baca dulu contohnya
# ============================================================
# Ini contoh fungsi yang sudah jadi. Jalankan dan amati.

def sapa_formal(nama):
    return "Selamat datang, " + nama + "!"

pesan = sapa_formal("Budi")
print(pesan)
# Output: Selamat datang, Budi!

# Perhatikan:
# - "def" = mendefinisikan fungsi
# - "nama" = parameter (kotak kosong yang diisi saat dipanggil)
# - "return" = nilai yang dikembalikan fungsi


# ============================================================
# BAGIAN 2 — Tugas
# ============================================================
# Buat fungsi bernama "sapa" yang:
# - Menerima satu parameter: nama
# - Mengembalikan string: "Halo, <nama>! Apa kabar?"
#
# Setelah selesai, panggil fungsinya dengan tiga nama berbeda
# dan cetak hasilnya.

# Tulis fungsinya di sini:
def sapa(nama):
    return "Halo, " + nama + "!" + " Apa kabar?"


# Panggil fungsinya di sini (contoh):
# print(sapa("Andi"))
# print(sapa("Sari"))
# print(sapa("Dika"))
pesan = sapa("Pipit") 
print(pesan)

pesan = sapa("Afifah")
print(pesan)

pesan = sapa("Jarwo")
print(pesan)

#output:
# Halo, Pipit! Apa kabar?   
# Halo, Afifah! Apa kabar?
# Halo, Jarwo! Apa kabar? ✅

# ============================================================
# BONUS (opsional)
# ============================================================
# Modifikasi fungsi "sapa" agar bisa menerima dua parameter:
# nama dan kota, lalu hasilkan:
# "Halo, <nama> dari <kota>!"
def sapa(nama,kota):
    return "Halo, " + nama + " dari " + kota + "!"

pesan = sapa("Pipit", "Bandung")
print(pesan)

#output: Halo, Pipit dari Bandung! ✅