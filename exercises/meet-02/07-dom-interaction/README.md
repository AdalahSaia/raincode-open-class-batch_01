# 07 · DOM Interaction

# Tujuan

Membuat interaksi sungguhan pertamamu: pengunjung mengetik, menekan
tombol, lalu halaman bereaksi — pola inti dari semua website
interaktif.

# Yang Dipelajari

- `document.getElementById("id")` — mengambil satu elemen HTML lewat id-nya.
- `.value` — membaca isi yang diketik user di `<input>`.
- `.innerText` — menuliskan teks ke dalam elemen.
- `onclick="namaFunction()"` — menjalankan function saat tombol diklik.
- Mengubah teks input (selalu string) menjadi angka dengan `Number(...)`
  sebelum dipakai dalam perbandingan.

# File yang Harus Diedit

- `script.js` — lengkapi function `sapa()` dan `cekUmur()`.
- `index.html` dan `style.css` sudah lengkap, tidak perlu diubah.

# Ekspektasi Hasil

1. Ketik nama di kotak pertama, klik "Sapa Saya" &rarr; muncul kalimat
   sapaan berisi namamu.
2. Ketik angka umur di kotak kedua, klik "Cek Status" &rarr; muncul
   "Sudah bisa buat KTP" atau "Belum waktunya buat KTP" sesuai umurnya.

# Hint

- Ikuti alur 3 langkah yang sudah dijelaskan di komentar: ambil isi
  input &rarr; proses &rarr; tampilkan hasil. Jangan lompat langkah.
- Tombol tidak bereaksi sama sekali? Buka Console (F12) — biasanya ada
  pesan error yang menyebutkan nama function yang salah ketik.
- `.value` dari `<input type="number">` tetap berupa **teks**, bukan
  angka asli — kalau langsung dibandingkan dengan `>=` hasilnya bisa
  aneh. Selalu bungkus dengan `Number(...)` dulu.

# Checklist

- [ ] `sapa()` mengambil isi `input#nama` dengan `.value`.
- [ ] `sapa()` menuliskan sapaan ke `p#hasil` dengan `.innerText`.
- [ ] `cekUmur()` mengubah `.value` jadi angka dengan `Number(...)`.
- [ ] `cekUmur()` memakai if/else untuk menentukan status KTP.
- [ ] Tidak ada error merah di Console saat tombol diklik.

# Hasil Akhir

Dua tombol yang benar-benar bereaksi terhadap isian pengunjung. Ini
adalah "jantung" dari halaman web interaktif — pola yang sama akan
kamu pakai lagi untuk tombol sapaan di `08-final-project`.
