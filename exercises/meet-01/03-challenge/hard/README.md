# Challenge Hard · Form Biodata dengan Kondisi

# Tujuan

Menggabungkan banyak input dan banyak kondisi INDEPENDEN (bukan
if/elif berantai) dalam satu program — level tersulit karena kamu
harus menentukan sendiri kondisi mana yang berdiri sendiri dan mana
yang saling terkait.

# Yang Dipelajari

Banyak `input()` sekaligus, format cetak biodata yang rapi, kondisi
independen (`if` terpisah-pisah, bukan `elif` berantai), dan kondisi
bertingkat untuk kategori umur.

# File yang Harus Diedit

- `03_biodata.py` — bagian "TULIS KODE DI SINI".

# Langkah

Spesifikasi lengkap ada di komentar `CERITA` & `SPESIFIKASI PROGRAM`
di dalam file. Ringkasnya:

1. Tampilkan biodata (nama, umur, kota, hobi) dalam format rapi
   dengan garis pembatas `====`.
2. Setelah itu, cetak SETIAP kondisi yang terpenuhi (boleh lebih dari
   satu sekaligus, makanya pakai `if` terpisah, bukan `elif`):
   - Umur &rarr; status boleh/tidaknya buat KTP.
   - Kota == "Jakarta" &rarr; catatan warga ibukota.
   - Hobi coding/programming &rarr; catatan calon programmer.
3. Bonus: tambahkan kategori umur (Anak-anak/Remaja/Dewasa/Lansia).

# Hint

- Perhatikan: kondisi umur, kota, dan hobi TIDAK saling menggantikan
  — ketiganya bisa muncul bersamaan. Kalau kamu memakai `elif` untuk
  menghubungkan ketiganya, hanya satu yang akan tercetak. Pakai tiga
  blok `if` terpisah.
- Kondisi kota dan hobi bersifat opsional — kalau tidak terpenuhi,
  TIDAK usah cetak apa-apa untuk kondisi itu (bukan pesan "tidak
  cocok").
- Untuk kategori umur di bagian bonus, urutan `elif`-nya penting —
  sama seperti prinsip di `../../02-buggy/bug_04.py`.

# Checklist

- [ ] Biodata tercetak rapi dengan format garis pembatas.
- [ ] Status KTP muncul sesuai umur.
- [ ] Catatan warga ibukota HANYA muncul kalau kota Jakarta.
- [ ] Catatan calon programmer HANYA muncul kalau hobi coding/programming.
- [ ] Bonus: kategori umur muncul sesuai rentangnya.

# Hasil Akhir

Program biodata yang bisa menampilkan beberapa catatan sekaligus
sesuai data yang dimasukkan — bukan cuma satu jalur pesan seperti di
level easy.
