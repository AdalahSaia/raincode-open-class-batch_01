# 05 · Flexbox

# Tujuan

Menguasai `display: flex` — bab yang paling sering dipakai di dunia
nyata untuk membuat elemen berjejer dan tertata rapi.

# Yang Dipelajari

- Mengaktifkan flex dengan `display: flex;` pada kotak pembungkus.
- `justify-content` — mengatur posisi mendatar (kiri, tengah, kanan,
  menyebar).
- `align-items` — mengatur posisi tegak.
- `gap` — memberi jarak antar elemen tanpa perlu margin manual.
- `flex-direction` — mengubah arah susunan: `row` (mendatar) atau
  `column` (menurun).

# File yang Harus Diedit

- `style.css` — ikuti komentar `TODO 1` sampai `TODO 4`.
- `index.html` sudah lengkap, tidak perlu diubah.

# Ekspektasi Hasil

1. Menu "Beranda / Tentang / Kontak" berjejer mendatar dengan jarak rapi.
2. Chip "Desain / Fotografi / Ngopi" berjejer mendatar seperti label.
3. Kotak A, B, C berjejer di tengah halaman dengan jarak rapi.

# Hint

- `display: flex` selalu ditulis di elemen PEMBUNGKUS (`.menu`,
  `.chip-container`, `.kartu-container`) — bukan di elemen di
  dalamnya (`a`, `.chip`, `.kartu-kecil`).
- Kalau flex sudah aktif tapi elemen masih menumpuk ke bawah, cek:
  apakah `display: flex;` benar-benar ada di dalam selector yang
  tepat?
- Lupa bedanya `justify-content` dan `align-items`? Ingat:
  **justify** = mendatar (seperti "justify" teks kiri-kanan),
  **align-items** = tegak.

# Checklist

- [ ] `.menu` sudah `display: flex` dengan `gap`.
- [ ] `.chip-container` sudah `display: flex` dengan `gap`.
- [ ] `.kartu-container` sudah `display: flex` dengan `justify-content: center`.
- [ ] Sudah mencoba `flex-direction: column` minimal sekali untuk
      melihat efeknya (boleh dikembalikan lagi ke `row`).

# Hasil Akhir

Tiga contoh tata letak flexbox yang bisa langsung kamu pakai ulang:
menu navigasi, kumpulan chip/label, dan kartu yang berjejer di
tengah. Pola ini akan langsung dipakai lagi di `08-final-project`.
