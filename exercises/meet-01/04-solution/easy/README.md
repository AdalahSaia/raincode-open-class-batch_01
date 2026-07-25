# Solusi · Challenge Easy

# Tujuan

Referensi pembanding untuk `../../03-challenge/easy`.

# Yang Dipelajari

Cara menyusun tiga kondisi yang saling eksklusif (`if / elif / else`)
supaya masing-masing pesan gagal login menuduh alasan yang tepat.

# File yang Harus Diedit

Tidak ada — folder ini untuk dibaca, bukan diedit.

# Langkah

1. Cek `username_input != USERNAME_VALID` lebih dulu — kalau ini
   True, tidak perlu cek password sama sekali.
2. Baru cek password di cabang `elif` — di titik ini username sudah
   pasti benar.
3. Cabang `else` berarti keduanya benar &rarr; login berhasil.

# Hint

Perhatikan urutannya dibalik dari kondisi "berhasil" — solusi ini
mengecek kegagalan dulu (username salah? password salah?), baru
menyimpulkan berhasil di `else`. Ini pola yang sering dipakai untuk
"guard clause": singkirkan dulu kasus gagal, sisanya pasti kasus
berhasil.

# Checklist

- [ ] Sudah membandingkan dengan hasil kerjaku sendiri di `../../03-challenge/easy`.

# Hasil Akhir

Sistem login dengan tiga jalur pesan yang jelas, ditulis lewat pola
guard clause.
