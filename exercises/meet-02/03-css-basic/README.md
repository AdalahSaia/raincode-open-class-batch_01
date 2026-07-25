# 03 · CSS Basic

# Tujuan

Memahami pola dasar CSS (`selector { properti: nilai; }`) dan properti
yang paling sering dipakai, terutama **box model**: beda `padding`
(jarak dalam) dan `margin` (jarak luar).

# Yang Dipelajari

- Pola inti CSS: pilih elemen → beri aturan.
- Properti warna & teks: `color`, `font-size`.
- Properti box model: `padding`, `margin`, `border`, `border-radius`.
- Cara CSS menempel ke HTML lewat `<link rel="stylesheet">` dan `class`.

# File yang Harus Diedit

- `style.css` — ikuti komentar `TODO 1` sampai `TODO 5`.
- `index.html` sudah lengkap, tidak perlu diubah.

# Ekspektasi Hasil

1. Paragraf "Beri aku warna hijau..." berubah jadi hijau.
2. Paragraf "Beri aku ukuran huruf..." tampak lebih besar dari teks lain.
3. "Kotak Padding" punya jarak lega antara tulisan dan tepi kotaknya.
4. Dua "Kotak Margin" punya jarak renggang satu sama lain.
5. Blok "Kartu Sederhana" tampak seperti kartu: putih, sudut membulat,
   ada jarak dari tepi layar.

# Hint

- Setiap aturan CSS **wajib** diakhiri titik koma `;` — kalau tidak,
  aturan setelahnya bisa ikut gagal terbaca.
- Satuan ukuran jangan lupa ditulis: `font-size: 24;` salah, harus
  `font-size: 24px;`.
- Bingung bedanya padding vs margin? Coba ubah nilainya jadi angka
  besar (`padding: 60px;`) lalu lihat langsung bagian mana yang
  melebar — isi kotak, atau jarak ke tetangganya?

# Checklist

- [ ] `.teks-hijau` berwarna hijau.
- [ ] `.teks-besar` ukuran hurufnya lebih besar dari paragraf biasa.
- [ ] `.kotak-padding` punya jarak dalam yang terlihat jelas.
- [ ] `.kotak-margin` punya jarak antar-kotak yang terlihat jelas.
- [ ] `.kartu` tampak seperti kartu: putih, sudut membulat, ada lebar tetap.
- [ ] Tidak ada aturan CSS yang lupa titik koma.

# Hasil Akhir

Halaman yang tadinya polos sekarang mulai punya warna, jarak, dan
bentuk. Kamu sudah paham 80% kebingungan orang soal CSS: padding vs
margin. Selanjutnya kita pakai ilmu ini untuk mempercantik profilmu di
`04-css-profile`.
