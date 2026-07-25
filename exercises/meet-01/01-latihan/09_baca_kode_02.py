# 09_baca_kode_02.py
# Topik: Baca Kode — Ada Fungsi & Kondisi

# ============================================================
# CARA MAIN
# ============================================================
# Kali ini ada fungsi. Telusuri dari bawah (dari pemanggilan)
# ke atas (ke definisi fungsinya), bukan sebaliknya.
# Jawab semua pertanyaan sebelum menjalankan kode.

# ---- Kodenya ----

def cek_kelulusan(nilai, kehadiran):
    if kehadiran < 75:
        return "Tidak Lulus — kehadiran kurang"
    if nilai >= 60:
        return "Lulus"
    else:
        return "Tidak Lulus — nilai kurang"


hasil1 = cek_kelulusan(70, 80)
hasil2 = cek_kelulusan(55, 90)
hasil3 = cek_kelulusan(80, 60)

print(hasil1)   # pertanyaan 1: ???
print(hasil2)   # pertanyaan 2: ???
print(hasil3)   # pertanyaan 3: ???

# ---- Pertanyaan ----
# 1. Apa yang dicetak untuk hasil1? Kenapa?
#    Jawab: ???
#
# 2. Apa yang dicetak untuk hasil2? Kenapa?
#    Jawab: ???
#
# 3. Apa yang dicetak untuk hasil3? Kenapa?
#    Jawab: ???
#
# 4. Kondisi mana yang dicek lebih dulu — kehadiran atau nilai?
#    Kenapa urutan itu penting?
#    Jawab: ???
