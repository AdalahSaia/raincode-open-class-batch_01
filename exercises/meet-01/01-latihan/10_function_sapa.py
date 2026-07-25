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


# Panggil fungsinya di sini (contoh):
# print(sapa("Andi"))
# print(sapa("Sari"))
# print(sapa("Dika"))


# ============================================================
# BONUS (opsional)
# ============================================================
# Modifikasi fungsi "sapa" agar bisa menerima dua parameter:
# nama dan kota, lalu hasilkan:
# "Halo, <nama> dari <kota>!"
