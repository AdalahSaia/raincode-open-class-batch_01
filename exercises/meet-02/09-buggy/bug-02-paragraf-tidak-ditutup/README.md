# Bug 2 · Paragraf Tidak Ditutup

# Tujuan

Melatih mata menghitung pasangan tag pembuka & penutup dalam blok
yang lebih panjang.

# Yang Dipelajari

- Tag yang lupa ditutup bisa "menelan" konten setelahnya.
- Pentingnya menghitung jumlah tag pembuka vs penutup saat sesuatu
  tampil tidak sesuai harapan.

# File yang Harus Diedit

- `index.html`

# Ekspektasi Hasil

Dua paragraf terpisah, masing-masing di barisnya sendiri:
"Nama saya Arin" dan "Saya suka desain".

# Hint

- Ada dua tag pembuka `<p>` — ada berapa tag penutup `</p>`?
- Tag yang tidak ditutup akan menggabungkan dirinya dengan konten
  berikutnya sampai ketemu penutup pertama yang tersedia.

# Checklist

- [ ] Setiap `<p>` punya `</p>` pasangannya sendiri.
- [ ] Dua kalimat tampil di baris terpisah, bukan menyatu.

# Hasil Akhir

Dua paragraf yang berdiri sendiri-sendiri, sesuai isi aslinya.
