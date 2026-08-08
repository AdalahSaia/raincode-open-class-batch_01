# bug_01.py
# Bug: Tipe Data Salah

# ============================================================
# MISI KAMU
# ============================================================
# Kode di bawah ini harusnya mencetak:
# "Nama: Rafi, Umur: 19 tahun"
#
# Tapi kalau dijalankan, ada error.
# Cari tahu errornya apa, lalu perbaiki.

nama = "Rafi"
umur = 19

print("Nama: " + nama + ", Umur: " + umur + " tahun") , error dibagian tipe data umur berbeda dengan nama

# ---- Petunjuk ----
# Baca pesan error-nya dengan teliti.
# Error apa yang muncul? Di baris berapa? di baris 3
# Cek tipe data masing-masing variabel — apakah bisa digabung langsung?

#Perbaikan kode:
nama = "Rafi"
umur = 19

print("Nama: " + nama + ", Umur: " + str(umur) + " tahun") #disamakan dulu tipe datanya
#output: Nama: Rafi, Umur: 19 tahun
atau 
print(f"Nama: {nama}, Umur: {umur} tahun") #f-string, bisa langsung gabungin tipe data berbeda
#output: Nama: Rafi, Umur: 19 tahun