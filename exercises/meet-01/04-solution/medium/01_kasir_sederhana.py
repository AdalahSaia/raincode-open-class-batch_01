# 01_kasir_sederhana.py
# Solusi Challenge Medium — Kasir Sederhana

nama_produk = "Indomie"
harga       = 3500
jumlah      = 10

# Hitung subtotal dulu:
subtotal = harga * jumlah

# Tentukan diskon (ikuti ATURAN di spesifikasi, bukan contoh struk
# di komentar file soal — untuk data di atas, subtotal = 35.000,
# yang belum menyentuh ambang diskon manapun):
if subtotal >= 100000:
    persen_diskon = 10
elif subtotal >= 50000:
    persen_diskon = 5
else:
    persen_diskon = 0

diskon_rupiah = subtotal * (persen_diskon / 100)

# Hitung total akhir:
total = subtotal - diskon_rupiah

# Cetak struk:
print("===========================")
print(f"Produk  : {nama_produk}")
print(f"Harga   : {harga}")
print(f"Jumlah  : {jumlah}")
print("---------------------------")
print(f"Subtotal: {subtotal}")
print(f"Diskon  : {persen_diskon}%")
print(f"Total   : {total}")
print("===========================")


# ============================================================
# BONUS — peringatan pembelian besar
# ============================================================
if jumlah > 20:
    print("Pembelian dalam jumlah besar — cek stok dulu ya.")
