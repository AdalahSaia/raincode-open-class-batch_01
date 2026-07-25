# Bug 4 · Function Tidak Cocok

# Tujuan

Melatih kebiasaan membaca pesan error JavaScript di Console untuk
menemukan bug secara tenang, bukan menebak-nebak.

# Yang Dipelajari

- Nama function yang dipanggil di `onclick="..."` harus SAMA PERSIS
  dengan nama function yang dideklarasikan di JavaScript.
- Cara membaca error `ReferenceError` / "is not defined" di Console.

# File yang Harus Diedit

- `script.js`

# Ekspektasi Hasil

Klik tombol "Klik Saya" &rarr; muncul kotak pesan alert bertuliskan
"Hai!".

# Hint

- Buka Console (F12), klik tombolnya, baca pesan error dari bawah.
- Pesan error JavaScript biasanya langsung menyebutkan nama yang
  "tidak ditemukan" — bandingkan ejaannya persis huruf demi huruf
  dengan yang dipanggil di HTML.

# Checklist

- [ ] Nama function di `script.js` sama persis dengan yang dipanggil
      di `onclick="..."`.
- [ ] Klik tombol memunculkan alert "Hai!".
- [ ] Tidak ada error merah lagi di Console.

# Hasil Akhir

Tombol yang benar-benar bereaksi saat diklik, tanpa error di Console.
