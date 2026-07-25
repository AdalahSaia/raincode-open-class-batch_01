# Solusi · Challenge Medium

# Tujuan

Referensi pembanding untuk `10-challenge/medium`.

# Yang Dipelajari

Cara memakai dua area flexbox berbeda dalam satu halaman: satu untuk
navigasi (`nav`), satu lagi untuk kumpulan kartu menu.

# File yang Harus Diedit

Tidak ada — folder ini untuk dibaca, bukan diedit.

# Langkah

1. `.menu-nav` diberi `display: flex; justify-content: center; gap: 20px;`
   supaya 3 tautan berjejer mendatar dengan jarak rapi.
2. `.daftar-menu` (pembungkus 3 kartu) diberi `display: flex;
   justify-content: center; gap: 16px; flex-wrap: wrap;` — `flex-wrap`
   ditambahkan supaya kartu tetap rapi kalau layarnya sempit.
3. Setiap `.kartu-menu` diberi lebar tetap (`width: 160px`) supaya
   ukurannya seragam.

# Hint

`display: flex` selalu diletakkan di elemen PEMBUNGKUS. Di sini ada
dua pembungkus berbeda (`.menu-nav` dan `.daftar-menu`) — masing-
masing diatur terpisah, tidak saling memengaruhi.

# Checklist

- [ ] Sudah membandingkan dengan hasil kerjaku sendiri di `10-challenge/medium`.

# Hasil Akhir

Halaman menu kedai kopi dengan navigasi dan kartu menu yang tersusun
rapi berkat dua area flexbox terpisah.
