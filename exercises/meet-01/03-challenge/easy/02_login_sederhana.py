# 02_login_sederhana.py
# Challenge: Sistem Login Sederhana

# ============================================================
# CERITA
# ============================================================
# Kamu bikin sistem login untuk aplikasi internal.
# Username dan password sudah tersimpan di program
# (hardcoded — nanti kalau sudah belajar database baru
# disimpan di tempat yang bener).

# ============================================================
# SPESIFIKASI PROGRAM
# ============================================================
# 1. Simpan username dan password yang valid:
#    USERNAME_VALID = "admin"
#    PASSWORD_VALID = "rahasia123"
#
# 2. Minta input dari user:
#    - username_input = input("Username: ")
#    - password_input = input("Password: ")
#
# 3. Cek apakah keduanya cocok:
#    - Kalau cocok    → cetak "Login berhasil! Selamat datang, admin."
#    - Kalau username salah → cetak "Username tidak ditemukan."
#    - Kalau password salah → cetak "Password salah."
#
# Hint: gunakan if / elif / else dan operator ==

# ============================================================
# TULIS KODE DI SINI
# ============================================================

USERNAME_VALID = "admin"
PASSWORD_VALID = "rahasia123"

# Minta input:
username_input = input("Username: ")
password_input = input("Password: ")

# Cek kondisinya:
if username_input == USERNAME_VALID and password_input == PASSWORD_VALID:
    print(f"Login berhasil! Selamat datang, {USERNAME_VALID}")
elif username_input != USERNAME_VALID:
    print("Username tidak ditemukan.")
else :
    print("Password salah.")

# ============================================================
# BONUS (opsional)
# ============================================================
# Buat program menghitung berapa kali user salah memasukkan
# password. Kalau sudah 3 kali salah, cetak:
# "Akun dikunci. Hubungi administrator."
#
# Hint: kamu butuh variabel counter dan perulangan (while).
#       Kalau belum belajar while, skip dulu boleh.

USERNAME_VALID = "admin"
PASSWORD_VALID = "rahasia123"

# Tambahan variabel counter dan max percobaan perulangan
salah_counter = 0
max_percobaan = 3

# While jika sudah 3x salah cetak
while salah_counter < max_percobaan:
    username_input = input("Username: ")
    password_input = input("Password: ")

    # note: Semua blok di bawah ini letaknya sejajar di dalam loop while
    if username_input == USERNAME_VALID and password_input == PASSWORD_VALID:
        print(f"Login berhasil! Selamat datang, {USERNAME_VALID}")
        break  # Setelah berhasil lalu program berhenti dan keluar dari looping
    elif username_input != USERNAME_VALID:
        print("Username tidak ditemukan.\n")
    else:
        salah_counter += 1
        sisa_percobaan = max_percobaan - salah_counter
        print(f"Password salah. sisa percobaan kamu: {sisa_percobaan}\n")

# Blok if ini akan muncul jika kesempatan 3x tetap gagal
if salah_counter == max_percobaan:
    print("Akun anda dikunci sementara. Silahkan Hubungi administrator.")
