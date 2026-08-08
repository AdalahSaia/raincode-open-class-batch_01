# bug_02.py
# Bug: Kondisi Terbalik

# ============================================================
# MISI KAMU
# ============================================================
# Program ini harusnya:
# - Cetak "Selamat, kamu lulus!" kalau nilai >= 60
# - Cetak "Coba lagi ya." kalau nilai < 60
#
# Tapi outputnya selalu salah. Cari dan perbaiki bugnya.

nilai = 75

if nilai < 60:
    print("Selamat, kamu lulus!")
else:
    print("Coba lagi ya.")
#output: Coba lagi ya.

# ---- Petunjuk ----
# Jalankan dulu, perhatikan outputnya. #output: Coba lagi ya.
# Apakah kondisi di "if" sudah benar? Kondisi If pertama salah karena nilai < 60 bukan nilai >= 60❌
# Coba tracing manual: nilai = 75, kondisi nilai < 60 itu True atau False? False jelas, karena 75 > 60 bukan 75<60 ❌


#Perbaikan kode:
nilai = 75

if nilai >= 60:
    print("Selamat, kamu lulus!")
else:
    print("Coba lagi ya.")

#outout: Selamat, kamu lulus!