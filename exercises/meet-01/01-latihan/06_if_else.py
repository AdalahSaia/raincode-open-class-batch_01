# 06_if_else.py
# Topik: Percabangan (if / else)

# ============================================================
# BAGIAN 1 — Baca dan tebak output
# ============================================================
# Jangan langsung dijalankan. Baca dulu pelan-pelan,
# telusuri alurnya, baru tulis jawabanmu.

tiket = 50000
ada_diskon = True

if ada_diskon:
    bayar = tiket * 0.8
else:
    bayar = tiket

print("Bayar:", bayar)   # tebak: ???

# Pertanyaan:
# - Kenapa blok "else" tidak dijalankan?
# - Coba ubah ada_diskon = False, kira-kira hasilnya apa?


# ============================================================
# BAGIAN 2 — Lengkapi kondisinya
# ============================================================
# Program ini mau ngecek apakah seseorang boleh masuk bioskop.
# Syaratnya: umur minimal 13 tahun.
# Lengkapi bagian yang rumpang.

umur = 15

if ???:                          # tulis kondisi yang benar di sini
    print("Boleh masuk.")
else:
    print("Maaf, belum boleh masuk.")

# Hint: pakai operator perbandingan yang sudah kamu pelajari


# ============================================================
# BAGIAN 3 — Tulis sendiri
# ============================================================
# Buat program sederhana:
# - Simpan angka berapa saja ke variabel "suhu"
# - Kalau suhu di atas 30, cetak "Panas banget!"
# - Kalau tidak, cetak "Masih oke."

# Tulis kode kamu di sini:
