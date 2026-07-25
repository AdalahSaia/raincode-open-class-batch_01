# 06 · JavaScript Basic

# Tujuan

Menyambungkan logika pemrograman yang sudah kamu kuasai di Pertemuan 1
(Python) ke sintaks JavaScript — variabel, if-else, dan function.

# Yang Dipelajari

- JavaScript adalah satu-satunya dari tiga lapisan website yang
  benar-benar bahasa pemrograman: bisa memutuskan, menghitung,
  bereaksi.
- Deklarasi variabel dengan `let` (bisa berubah) dan `const` (tetap).
- Menggabungkan teks & variabel dengan template string: `` `Halo ${nama}` ``.
- Struktur `if / else if / else` versi JavaScript.
- Membuat dan memanggil `function`.
- `console.log()` untuk melihat hasil di Console (DevTools).

# File yang Harus Diedit

- `script.js` — ikuti komentar `TODO 1` sampai `TODO 6`.
- `index.html` sudah lengkap, tidak perlu diubah.

# Ekspektasi Hasil

Halaman di browser tetap terlihat sama (hanya 2 paragraf) — semua
hasil latihan ini muncul di tab **Console**, bukan di halaman.
Setelah selesai, Console menampilkan:
1. Nama, umur, kota yang sudah kamu isi.
2. Satu kalimat perkenalan dari template string.
3. Grade hasil if/else berdasarkan `nilai`.
4. Kalimat sapaan dari function `sapa()`.

# Hint

- Lupa cara buka Console? Klik kanan halaman &rarr; **Inspect** &rarr;
  tab **Console** (atau tekan `F12`).
- Kalau Console kosong, cek dulu: apakah ada tanda merah (error)?
  Baca pesannya dari bawah — biasanya menyebutkan baris yang bermasalah.
- JS itu case-sensitive: `console.log` benar, `Console.log` salah.
- Kondisi di `if` JS dibungkus tanda kurung `( )`, dan blok kodenya
  dibungkus kurung kurawal `{ }` — beda dari Python yang pakai titik
  dua `:` dan indentasi.

# Checklist

- [ ] Tiga variabel (nama, umur, kota) sudah dibuat dan dicetak.
- [ ] Satu kalimat perkenalan pakai template string sudah tercetak.
- [ ] Logika if/else if/else grade sudah menghasilkan huruf yang benar.
- [ ] Function `sapa()` sudah dibuat, dipanggil, dan hasilnya tercetak.
- [ ] Tidak ada tulisan error berwarna merah di Console.

# Hasil Akhir

Kamu sudah menerjemahkan cara berpikir Python ke JavaScript — bekal
utama sebelum lanjut ke `07-dom-interaction`, tempat logika ini mulai
mengubah tampilan HALAMAN, bukan cuma Console.
