# Challenge Medium · Menu Kedai Kopi

# Tujuan

Melatih penggunaan Flexbox untuk membuat tata letak yang lebih
kompleks dari satu kartu tunggal: navigasi mendatar dan beberapa
kartu berjejer rapi.

# Yang Dipelajari

Materi yang dipakai: seluruh materi `easy`, ditambah `display: flex`,
`justify-content`, `align-items`, `gap`, dan `flex-direction`. Belum
ada JavaScript di level ini.

# File yang Harus Diedit

- `index.html`
- `style.css`

# Langkah (Spesifikasi)

Bangun satu halaman "Menu Kedai Kopi" berisi:

1. Bagian atas (`header`) berisi nama kedai (`h1`) dan sebuah menu
   navigasi (`nav`) dengan 3 tautan (`a`): "Menu", "Lokasi", "Kontak"
   — berjejer MENDATAR (pakai flexbox) dengan jarak rapi antar tautan.
2. Judul (`h2`) "Menu Andalan Kami".
3. Tiga "kartu menu" berjejer MENDATAR (pakai flexbox), masing-masing
   berisi:
   - Satu `img` (boleh placeholder).
   - Nama minuman (`h3` atau `p` tebal), misalnya "Kopi Susu",
     "Americano", "Cappuccino".
   - Harga (`p`), misalnya "Rp 18.000".
   Ketiga kartu ini harus punya jarak rapi antar satu sama lain dan
   berada di tengah halaman.
4. Setiap kartu diberi `background`, `padding`, dan `border-radius`
   supaya terlihat rapi (pakai pola card seperti di `04-css-profile`).

# Hint

- Pisahkan dua area flex yang berbeda: satu untuk `nav`
  (`justify-content`/`gap` saja sudah cukup), satu lagi untuk
  pembungkus tiga kartu menu.
- Kalau kartu-kartunya malah menumpuk ke bawah, cek: apakah
  `display: flex;` sudah ada di ELEMEN PEMBUNGKUS-nya (bukan di
  kartu itu sendiri)?
- Boleh contek ulang pola dari `05-flexbox` — spesifikasi ini memang
  sengaja mirip supaya kamu terbiasa memakainya ulang.

# Checklist

- [ ] `nav` berisi 3 tautan yang berjejer mendatar dengan jarak rapi.
- [ ] Tiga kartu menu berjejer mendatar, bukan menumpuk ke bawah.
- [ ] Tiap kartu punya gambar, nama minuman, dan harga.
- [ ] Tiap kartu punya `background`, `padding`, `border-radius`.

# Hasil Akhir

Satu halaman menu kedai kopi dengan navigasi dan kartu menu yang
tersusun rapi berkat Flexbox.
