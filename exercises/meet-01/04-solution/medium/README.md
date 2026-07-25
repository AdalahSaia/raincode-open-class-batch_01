# Solusi · Challenge Medium

# Tujuan

Referensi pembanding untuk `../../03-challenge/medium`.

# Yang Dipelajari

Cara menyusun kalkulasi bertingkat (subtotal &rarr; persentase diskon
&rarr; nilai diskon dalam rupiah &rarr; total) dan mencetaknya rapi
lewat f-string.

# File yang Harus Diedit

Tidak ada — folder ini untuk dibaca, bukan diedit.

# Langkah

1. `subtotal = harga * jumlah` dihitung lebih dulu, karena semua
   aturan diskon bergantung pada nilai ini.
2. Tingkatan diskon dicek dari yang PALING BESAR dulu (`>= 100000`),
   baru turun ke `>= 50000` — sama seperti pola grade di
   `../../01-latihan/07_grade_sederhana.py`.
3. `diskon_rupiah` dihitung terpisah dari `persen_diskon` supaya
   perhitungan totalnya jelas: `total = subtotal - diskon_rupiah`.

# Hint

**Catatan penting:** untuk data contoh di file (`harga = 3500`,
`jumlah = 10`), `subtotal`-nya adalah 35.000 — angka ini TIDAK
menyentuh ambang diskon manapun (baik 50.000 maupun 100.000), jadi
solusinya mencetak `Diskon: 0%` dan `Total: 35000.0`. Ini BEDA dengan
contoh struk yang tertulis di komentar file soal (`Diskon: 5%, Total:
33250.0`) — contoh struk itu memang tidak konsisten dengan aturan
diskon yang dituliskan tepat di atasnya. Solusi ini mengikuti ATURAN,
karena aturan adalah spesifikasi yang bisa diprogram; contoh struk
hanyalah ilustrasi format.

# Checklist

- [ ] Sudah membandingkan dengan hasil kerjaku sendiri di `../../03-challenge/medium`.

# Hasil Akhir

Program kasir yang menghitung tingkatan diskon secara konsisten
mengikuti aturan yang didefinisikan, dengan struk tercetak rapi.
