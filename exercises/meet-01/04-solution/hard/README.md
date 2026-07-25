# Solusi · Challenge Hard

# Tujuan

Referensi pembanding untuk `../../03-challenge/hard`.

# Yang Dipelajari

Cara membedakan kondisi INDEPENDEN (pakai `if` terpisah-pisah) dari
kondisi bertingkat/eksklusif (pakai `if/elif/else`) dalam satu
program yang sama.

# File yang Harus Diedit

Tidak ada — folder ini untuk dibaca, bukan diedit.

# Langkah

1. Biodata dicetak dulu dengan format garis pembatas.
2. Status KTP, catatan kota, dan catatan hobi ditulis sebagai TIGA
   blok `if` yang BERDIRI SENDIRI — bukan `elif` — karena ketiganya
   bisa sama-sama benar untuk satu orang yang sama (misalnya: umur
   20 tahun, dari Jakarta, hobi coding &rarr; ketiga catatan muncul
   sekaligus).
3. Kategori umur di bagian bonus BEDA polanya — di sini dipakai
   `if/elif/else` karena empat kategori itu SALING MENIADAKAN (satu
   umur cuma bisa masuk satu kategori).

# Hint

Ini bagian paling sering salah di level hard: kalau status KTP, kota,
dan hobi ditulis pakai `elif` yang saling menyambung, cuma SATU
catatan yang akan tercetak walau harusnya bisa lebih dari satu.
Bandingkan lagi kode `if` vs `elif` di solusi ini kalau hasil
punyamu beda.

# Checklist

- [ ] Sudah membandingkan dengan hasil kerjaku sendiri di `../../03-challenge/hard`.

# Hasil Akhir

Program biodata yang bisa menampilkan beberapa catatan independen
sekaligus, plus satu kategori umur yang saling eksklusif.
