# 01_kasir_sederhana.py
# Challenge: Kasir Sederhana

# ============================================================
# CERITA
# ============================================================
# Kamu diminta bantu toko kelontong Pak Budi bikin program
# kasir sederhana. Program ini menerima nama produk, harga
# satuan, dan jumlah beli — lalu menghitung total tagihan
# dan memberi diskon kalau syaratnya terpenuhi.

# ============================================================
# SPESIFIKASI PROGRAM
# ============================================================
# 1. Simpan data berikut ke variabel:
#    - nama_produk  → nama barang yang dibeli (string)
#    - harga        → harga per satuan (integer)
#    - jumlah       → berapa banyak dibeli (integer)
#
# 2. Hitung total = harga * jumlah
#
# 3. Aturan diskon:
#    - Kalau total >= 100.000  → diskon 10%
#    - Kalau total >= 50.000   → diskon 5% #biar sesuai output diganti 30000
#    - Kalau kurang dari itu   → tidak ada diskon
#
# 4. Cetak struk seperti ini:
#
#    ===========================
#    Produk  : Indomie
#    Harga   : 3500
#    Jumlah  : 10
#    ---------------------------
#    Subtotal: 35000
#    Diskon  : 5%
#    Total   : 33250.0
#    ===========================

# ============================================================
# TULIS KODE DI SINI
# ============================================================

nama_produk = "Indomie"
harga       = 3500
jumlah      = 10

# Hitung subtotal dulu:
subtotal = harga * jumlah

# Tentukan diskon:
if subtotal >= 100000:
    persen_diskon = "10%"
    nilai_diskon = subtotal * 0.1
elif subtotal >= 30000:
    persen_diskon = "5%"
    nilai_diskon = subtotal * 0.05
else:
    persen_diskon = "0%"
    nilai_diskon = subtotal * 0


# Hitung total akhir:
total_akhir = subtotal - nilai_diskon

# Cetak struk:
print("===========================")
print(f"Produk  : {nama_produk}")
print(f"Harga   : {harga}")
print(f"Jumlah  : {jumlah}")
print("---------------------------")
print(f"Subtotal: {subtotal}")
print(f"Diskon  : {persen_diskon}")
print(f"Total   : {total_akhir}")
print("===========================")


# ============================================================
# BONUS (opsional)
# ============================================================
# Tambahkan kondisi: kalau jumlah > 20 buah, beri pesan
# "Pembelian dalam jumlah besar — cek stok dulu ya."

nama_produk = "Indomie"
harga       = 3500
jumlah      = 50 #karena disini jumlah > 20 maka berlaku if pertama

#tambahan kondisi
if jumlah > 20:
    print(f"Pembelian dalam jumlah besar — cek stok dulu ya.\n")

# Hitung subtotal dulu:
subtotal = harga * jumlah

# Tentukan diskon:
if subtotal >= 100000:
    persen_diskon = "10%"
    nilai_diskon = subtotal * 0.1
elif subtotal >= 30000:
    persen_diskon = "5%"
    nilai_diskon = subtotal * 0.05
else:
    persen_diskon = "0%"
    nilai_diskon = subtotal * 0

# Hitung total akhir:
total_akhir = subtotal - nilai_diskon

# Cetak struk:
print("===========================")
print(f"Produk  : {nama_produk}")
print(f"Harga   : {harga}")
print(f"Jumlah  : {jumlah}")
print("---------------------------")
print(f"Subtotal: {subtotal}")
print(f"Diskon  : {persen_diskon}")
print(f"Total   : {total_akhir}")
print("===========================")