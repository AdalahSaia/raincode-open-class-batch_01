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

print(hasil1)   # pertanyaan 1: cek_kelulusan(70, 80)
print(hasil2)   # pertanyaan 2: cek_kelulusan(55, 90)
print(hasil3)   # pertanyaan 3: cek_kelulusan(80, 60)

# ---- Pertanyaan ----
# 1. Apa yang dicetak untuk hasil1? Kenapa?
#    Jawab: Lulus karena blok if pertama terpenuhi (kehadiran 80 >= 75) sehingga lanjut pengecekan ke blok if kedua, dan nilai 70 >= 60, maka return "Lulus".
#
# 2. Apa yang dicetak untuk hasil2? Kenapa?
#    Jawab: Tidak Lulus - nilai kurang karena walaupun blok if pertama terpenuhi (kehadiran 90>70)tetapi pada nilai 50<60 (tidak memenuhi syarau),maka yang akan jalan adalah operator else yaitu return "Tidak Lulus - nilai kurang".
#
# 3. Apa yang dicetak untuk hasil3? Kenapa?
#    Jawab: Tidak Lulus - kehadiran kurang, karena pada pengecekan if pertama sudah tidak memenuhi syarat kelulusan ( kehadiran < 75), maka yang jalan adalah operator if pertama yaitu return "Tidak Lulus - kehadiran kurang".
#
# 4. Kondisi mana yang dicek lebih dulu — kehadiran atau nilai?
#    Kenapa urutan itu penting?
#    Jawab: yang di cek terlebih dahulu adalah kehadiran, karena jika kehadiran tidak memenuhi syarat maka tidak perlu mengecek nilai.
# urutan itu penting karena supaya program lebih mudah dibaca dan dipahami dan meminimalisir kesalahan logika.
