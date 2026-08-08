#==============bagian 1==================
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

#=====================bagian 2===========================
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
