# Challenge Easy · Sistem Login Sederhana

# Tujuan

Melatih `if / elif / else` untuk membedakan beberapa kondisi gagal
yang berbeda alasannya, bukan cuma benar/salah.

# Yang Dipelajari

Perbandingan string dengan `==`, `input()`, dan percabangan
bertingkat.

# File yang Harus Diedit

- `02_login_sederhana.py` — bagian "TULIS KODE DI SINI".

# Langkah

Spesifikasi lengkap ada di komentar `CERITA` & `SPESIFIKASI PROGRAM`
di dalam file. Ringkasnya:

1. Minta `username_input` dan `password_input` lewat `input()`.
2. Bandingkan dengan `USERNAME_VALID` dan `PASSWORD_VALID` yang sudah
   disediakan.
3. Tiga kemungkinan pesan: login berhasil, username tidak ditemukan,
   atau password salah — masing-masing punya pesan yang berbeda.

# Hint

- Urutan pengecekan penting: cek username dulu, baru password. Kalau
  urutannya terbalik, pesan errornya bisa salah menuduh.
- Bonus (opsional, boleh dilewati kalau belum belajar `while`):
  hitung berapa kali password salah berturut-turut.

# Checklist

- [ ] Username & password benar &rarr; "Login berhasil! Selamat
      datang, admin."
- [ ] Username salah &rarr; "Username tidak ditemukan."
- [ ] Username benar, password salah &rarr; "Password salah."

# Hasil Akhir

Sistem login sederhana dengan tiga jalur pesan yang jelas dan tepat
sasaran.
