# 04 · CSS Profile

# Tujuan

Mempercantik halaman profil polos dari `02-html-profile` menjadi
tampilan kartu (card) yang rapi — tanpa mengubah HTML sama sekali,
murni lewat CSS.

# Yang Dipelajari

- HTML dan CSS adalah dua hal terpisah: isi (HTML) tidak berubah,
  yang berubah hanya tampilannya (CSS).
- Membungkus konten jadi "kartu" dengan `background`, `padding`,
  `border-radius`.
- Membuat elemen ke tengah halaman dengan `margin: ... auto;`.
- Mengubah `<img>` persegi jadi bulat dengan `border-radius: 50%`.
- Mengubah tautan `<a>` supaya terlihat seperti tombol.

# File yang Harus Diedit

- `style.css` — ikuti komentar `TODO 1` sampai `TODO 5`.
- `index.html` sudah lengkap. Boleh ganti teksnya dengan datamu
  sendiri, tapi strukturnya tidak perlu diubah.

# Ekspektasi Hasil

Halaman yang tadinya hitam-putih dan menumpuk polos, berubah jadi satu
kartu putih di tengah halaman dengan latar berwarna, foto bulat, judul
berwarna teal, dan tombol "Hubungi Saya" yang terlihat seperti tombol
sungguhan.

# Hint

- Kerjakan TODO secara berurutan — tiap bagian saling menumpuk dan
  lebih mudah dicek kalau satu-satu.
- `margin: 40px auto;` artinya: 40px di atas & bawah, dan "auto" di
  kiri & kanan (yang bikin elemen ke tengah). Ini berlaku hanya kalau
  elemen punya `max-width` atau `width` yang lebih kecil dari layar.
- `border-radius: 50%` hanya membuat lingkaran sempurna kalau lebar
  dan tinggi elemennya sama.
- Tombol tidak berwarna? Cek nama class-nya sama persis antara HTML
  (`class="btn"`) dan CSS (`.btn`) — huruf besar/kecil berpengaruh.

# Checklist

- [ ] Latar halaman (`body`) sudah berwarna, bukan putih polos.
- [ ] Konten terbungkus jadi satu kartu putih di tengah halaman.
- [ ] Foto profil sudah berbentuk bulat.
- [ ] Judul nama (`h1`) sudah berwarna.
- [ ] "Hubungi Saya" terlihat seperti tombol, bukan tautan biru bergaris bawah.

# Hasil Akhir

Satu kartu profil yang enak dilihat: foto bulat, nama berwarna, dan
tombol kontak yang jelas bisa diklik. Selanjutnya kita rapikan tata
letaknya lebih jauh pakai Flexbox di `05-flexbox`.
