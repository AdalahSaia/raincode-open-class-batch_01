# Bug 5 · Class Beda Huruf Besar/Kecil

# Tujuan

Melatih ketelitian membandingkan nama class antara HTML dan CSS —
bug yang sering luput karena terlihat "hampir sama".

# Yang Dipelajari

- CSS bersifat case-sensitive: `Card` dan `card` dianggap dua nama
  yang berbeda.
- Class di HTML (`class="..."`) dan selector di CSS (`.namaClass`)
  harus dieja SAMA PERSIS, termasuk huruf besar/kecilnya.

# File yang Harus Diedit

- Perbaiki salah satu: `index.html` ATAU `style.css`, supaya
  keduanya memakai ejaan yang sama.

# Ekspektasi Hasil

Kartu tampil berlatar putih, sudut membulat, dan berada di tengah
halaman.

# Hint

- Buka tab **Elements** di DevTools, klik elemen kartunya, lihat
  panel Styles — apakah aturan `.card` muncul di sana atau tidak?
- Kalau aturan `.card` tidak muncul sama sekali di panel Styles,
  itu tandanya selector-nya tidak "menemukan" elemen manapun.

# Checklist

- [ ] Nama class di HTML dan selector di CSS sudah sama persis.
- [ ] Kartu tampil berwarna putih dengan sudut membulat.

# Hasil Akhir

Kartu yang tampil sesuai gaya CSS-nya — bukti bahwa CSS itu
case-sensitive dan ketelitian penamaan itu penting.
