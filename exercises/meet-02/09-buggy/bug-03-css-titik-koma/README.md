# Bug 3 · CSS Lupa Titik Koma

# Tujuan

Melatih mata menemukan tanda baca CSS yang hilang — salah satu bug
paling sering dilakukan pemula.

# Yang Dipelajari

- Setiap aturan CSS wajib diakhiri titik koma `;`.
- Titik koma yang hilang bisa membuat DUA aturan sekaligus gagal
  diterapkan, bukan cuma satu.

# File yang Harus Diedit

- `style.css`

# Ekspektasi Hasil

Tombol "Kirim" tampil berlatar warna teal dengan tulisan putih, sudut
membulat, dan tanpa border.

# Hint

- Buka tab **Elements** di DevTools, klik elemen `<button>`, lihat
  panel Styles di sebelahnya — CSS yang gagal diterapkan biasanya
  tercoret.
- Baca aturan `.btn` baris demi baris. Ada dua baris pertama yang
  seharusnya terpisah tapi menyatu jadi satu.

# Checklist

- [ ] Setiap baris di dalam `.btn { }` diakhiri titik koma.
- [ ] Tombol tampil berwarna teal dengan tulisan putih.

# Hasil Akhir

Tombol yang tampil sesuai desain: berwarna, sudut membulat, siap
diklik.
