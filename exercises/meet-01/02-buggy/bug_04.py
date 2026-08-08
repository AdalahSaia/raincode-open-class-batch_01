# bug_04.py
# Bug: Logika Grade Bertingkat Salah

# ============================================================
# MISI KAMU
# ============================================================
# Program penentu grade di bawah ini punya bug logika.
# Untuk nilai = 85, harusnya muncul "B".
# Tapi coba jalankan — apakah hasilnya benar?
#
# Kalau tidak, cari di mana logikanya salah.

nilai = 85

if nilai >= 60: #Kondisi pengecekan 1 berhenti disini 
    grade = "D"
elif nilai >= 70: #kondisi pengecekan 2 berhenti disini
    grade = "C"
elif nilai >= 80:
    grade = "B"
elif nilai >= 90:
    grade = "A"
else:
    grade = "E"

print("Grade:", grade) #output Grade: D

# ---- Petunjuk ----
# Python mengevaluasi kondisi if/elif dari atas ke bawah.
# Begitu satu kondisi True, yang lain dilewati.
# Coba tanya diri sendiri: nilai 85 >= 60 itu True atau False? True
# Terus apa yang terjadi setelah kondisi pertama True? pengecekan berhenti di blok pertama karena kondisi pertama true.

#Perbaikan kode:
nilai = 85

if nilai <= 60: #diganti ke nilai <=60
    grade = "D"
elif nilai <= 70: #diganti ke nilai <=70
    grade = "C"
elif nilai >= 80:
    grade = "B"
elif nilai >= 90:
    grade = "A"
else:
    grade = "E"

print("Grade:", grade) #Output: Grade: B