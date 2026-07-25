# Solusi · Challenge Hard

# Tujuan

Referensi pembanding untuk `10-challenge/hard`.

# Yang Dipelajari

Cara menggabungkan input form, CSS flexbox untuk menyusun label+input
menurun rapi (`flex-direction: column`), dan JavaScript (`.value`,
`Number(...)`, `if/else`, `.innerText`) menjadi satu interaksi utuh.

# File yang Harus Diedit

Tidak ada — folder ini untuk dibaca, bukan diedit.

# Langkah

1. `index.html` sengaja memakai `<div class="form-daftar">`, BUKAN
   `<form>` — supaya tombol tidak memicu submit/reload halaman.
2. `.form-daftar` diberi `display: flex; flex-direction: column;`
   supaya label dan input tersusun menurun rapi, bukan berjejer
   mendatar berantakan.
3. `script.js` mengambil dua nilai input, mengubah umur ke angka
   dengan `Number(...)`, lalu memakai `if / else if / else` untuk
   menentukan kategori sebelum digabung jadi satu pesan lewat
   `.innerText`.

# Hint

Kalau versimu memakai `<form>` dan tombolnya malah me-reload halaman,
itu memang perilaku bawaan `<form>`. Solusi paling sederhana untuk
level ini: pakai `<div>` biasa seperti di sini.

# Checklist

- [ ] Sudah membandingkan dengan hasil kerjaku sendiri di `10-challenge/hard`.

# Hasil Akhir

Form pendaftaran yang memproses input lewat if/else dan menampilkan
hasilnya secara instan tanpa reload halaman.
