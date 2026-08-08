# 08_baca_kode_01.py
# Topik: Baca Kode — Telusuri Alurnya

# ============================================================
# CARA MAIN
# ============================================================
# Di bawah ada sepotong kode. Jangan dijalankan dulu.
# Baca dari atas ke bawah, telusuri nilainya di kepala,
# lalu jawab pertanyaan-pertanyaan di komentar.
# Setelah semua pertanyaan dijawab, baru jalankan untuk ngecek.

# ---- Kodenya ----

poin = 10
bonus = 5

poin = poin + bonus
poin = poin * 2

aktif = poin > 25

print(poin)    # pertanyaan 1: berapa ini? 30
#ini melalui 2x operasi poin1= poin + bonus = 10+5 = 15, poin2= poin * 2 = hasill poin 1 * 2 = 15 * 2 = 30✅
print(aktif)   # pertanyaan 2: True atau False? True
# True karena aktif = poin > 25 sedangkan poin diketahui 30 maka aktif = 30 >25 = True✅

# ---- Pertanyaan ----
# 1. Berapa nilai poin setelah baris ketiga (poin = poin + bonus)?
#    Jawab: 10=5 = 15
#
# 2. Berapa nilai poin setelah baris keempat (poin = poin * 2)?
#    Jawab: 15 * 2 = 30
#
# 3. Kenapa aktif bernilai True (atau False)?
#    Jawab: karena aktif = poin > 25 sedangkan poin diketahui 30 maka aktif = 30 >25 = True✅
#
# 4. Kalau poin awalnya 5 (bukan 10), apa yang berubah?
#    Jawab: perubahan nilai poin juga akan mempengaruhi nilai operasi lainnya
# kita ubah disini 
#poin = 5
#bonus = 5

#poin = poin + bonus = 5 + 5 = 10
#poin = poin * 2 = 10 * 2 = 20

#aktif = poin > 25

#print(poin) = 20
#print(aktif) = False karena aktif = 20 > 25 adalah False
