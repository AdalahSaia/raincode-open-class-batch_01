# 02_login_sederhana.py
# Solusi Challenge Easy — Sistem Login Sederhana

USERNAME_VALID = "admin"
PASSWORD_VALID = "rahasia123"

username_input = input("Username: ")
password_input = input("Password: ")

# Cek username dulu, baru password — urutan ini penting supaya
# pesan errornya menuduh alasan yang tepat.
if username_input != USERNAME_VALID:
    print("Username tidak ditemukan.")
elif password_input != PASSWORD_VALID:
    print("Password salah.")
else:
    print("Login berhasil! Selamat datang, admin.")


# ============================================================
# BONUS — hitung berapa kali password salah
# ============================================================
# Versi ini memakai while supaya user bisa mencoba ulang sampai
# 3 kali sebelum akunnya "dikunci". Boleh dilewati kalau belum
# belajar while — bagian WAJIB di atas sudah cukup untuk lulus
# challenge ini.

# percobaan = 0
# while percobaan < 3:
#     password_coba = input("Password: ")
#     if password_coba == PASSWORD_VALID:
#         print("Login berhasil!")
#         break
#     percobaan += 1
#     print(f"Password salah. Sisa percobaan: {3 - percobaan}")
# else:
#     print("Akun dikunci. Hubungi administrator.")
