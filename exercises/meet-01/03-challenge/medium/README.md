# Challenge Medium · Kasir Sederhana

# Tujuan

Melatih kalkulasi bertingkat (subtotal &rarr; diskon &rarr; total) dan
mencetak hasilnya dalam format struk yang rapi.

# Yang Dipelajari

Operasi aritmatika, `if/elif/else` untuk menentukan tingkatan diskon,
dan menyusun output multi-baris yang presisi.

# File yang Harus Diedit

- `01_kasir_sederhana.py` — bagian "TULIS KODE DI SINI".

# Langkah

Spesifikasi lengkap ada di komentar `CERITA` & `SPESIFIKASI PROGRAM`
di dalam file. Ringkasnya:

1. Hitung `subtotal = harga * jumlah`.
2. Tentukan diskon berdasarkan aturan tingkatan (`>= 100.000` &rarr;
   10%, `>= 50.000` &rarr; 5%, selain itu &rarr; tidak ada diskon).
3. Hitung `total` setelah diskon diterapkan.
4. Cetak struk sesuai format yang dicontohkan di komentar file.

# Hint

- Untuk data contoh (`harga = 3500`, `jumlah = 10`), coba hitung dulu
  di kepala: berapa `subtotal`-nya, dan tingkatan diskon mana yang
  seharusnya berlaku berdasarkan ATURAN yang tertulis di spesifikasi?
  Bandingkan dengan contoh struk di komentar file — kalau hasilnya
  beda, percayai ATURAN-nya (contoh struk di file ini kebetulan
  memang tidak konsisten dengan aturannya sendiri).
- Cek urutan `elif` diskon: kondisi yang lebih besar harus dicek
  lebih dulu, sama seperti pola grade di `../../01-latihan/07_grade_sederhana.py`.

# Checklist

- [ ] Subtotal dihitung dengan benar (`harga * jumlah`).
- [ ] Tingkatan diskon sesuai aturan (bukan sesuai contoh struk).
- [ ] Total = subtotal dikurangi nilai diskon dalam rupiah.
- [ ] Struk tercetak rapi dengan garis pembatas seperti contoh.
- [ ] Bonus: pesan "cek stok dulu" muncul kalau `jumlah > 20`.

# Hasil Akhir

Program kasir mini yang menghitung tingkatan diskon secara otomatis
dan mencetak struk yang rapi dibaca.
