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

print("Bayar:", bayar)   # tebak: bayar= 50000 * 0.8 = 40000

# Pertanyaan:
# - Kenapa blok "else" tidak dijalankan?
😶‍🌫️ disini yang jalan blok if karena diketahui di soal memenuhi syarat if yaitu ada_diskon=True
# - Coba ubah ada_diskon = False, kira-kira hasilnya apa?
😶‍🌫️ Setelah di run outputnya:
#Bayar: 50000 , yang jalan adalah blok else karena syarat if tidak terpenuhi


# ============================================================
# BAGIAN 2 — Lengkapi kondisinya
# ============================================================
# Program ini mau ngecek apakah seseorang boleh masuk bioskop.
# Syaratnya: umur minimal 13 tahun.
# Lengkapi bagian yang rumpang.

umur = 15

if umur >=13:                          # tulis kondisi yang benar di sini
    print("Boleh masuk.")
else:
    print("Maaf, belum boleh masuk.")

# Hint (petunjuk): pakai operator perbandingan yang sudah kamu pelajari
#output: Boleh masuk. yang jalan blok if karena syarat di soal sudah terpenuhi yaitu umur=15 >=13

# ============================================================
# BAGIAN 3 — Tulis sendiri
# ============================================================
# Buat program sederhana:
# - Simpan angka berapa saja ke variabel "suhu"
# - Kalau suhu di atas 30, cetak "Panas banget!"
# - Kalau tidak, cetak "Masih oke."

# Tulis kode kamu di sini:
suhu = 29

if suhu > 30:
    print("Panas Banget!!")
else:
    print("Masih Oke.")

#output: Masih Oke.karena suhu =29 < 30 ,yang jalan blok else