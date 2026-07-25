# Challenge Hard · Form Pendaftaran Interaktif

# Tujuan

Menggabungkan HTML Forms, CSS, dan JavaScript (DOM) sekaligus — level
tersulit yang menuntut kamu memakai semua materi Pertemuan 2 dari
spesifikasi kosong.

# Yang Dipelajari

Materi yang dipakai: elemen form (`label`, `input`, `button`), CSS
card + flexbox, dan JavaScript (`getElementById`, `.value`,
`.innerText`, `onclick`, `if/else`). Tidak ada konsep baru di luar
Bagian 1-7.

# File yang Harus Diedit

- `index.html`
- `style.css`
- `script.js`

# Langkah (Spesifikasi)

Bangun satu halaman "Form Pendaftaran Webinar RainCode" berisi:

1. Judul (`h1`) "Pendaftaran Webinar RainCode".
2. Form berisi:
   - `label` + `input type="text"` untuk Nama Lengkap.
   - `label` + `input type="number"` untuk Umur.
   - `button` bertuliskan "Daftar Sekarang".
3. Satu elemen kosong (misalnya `<p id="hasil"></p>`) di bawah form,
   tempat pesan sambutan akan muncul.
4. Bungkus form dalam kartu (`background`, `padding`, `border-radius`)
   seperti pola di `04-css-profile`, dan buat label+input tersusun
   rapi (boleh pakai flexbox `flex-direction: column` supaya
   label & input-nya menumpuk teratur, bukan berantakan).
5. Saat tombol "Daftar Sekarang" diklik, JavaScript harus:
   - Mengambil isi Nama dan Umur dari input.
   - Menampilkan pesan di `#hasil` dengan format:
     `"Halo <nama>! Pendaftaranmu berhasil."`
   - DITAMBAH satu baris kategori umur berdasarkan if/else:
     - `< 13` &rarr; "Kategori: Anak-anak"
     - `13` - `17` &rarr; "Kategori: Remaja"
     - `18` - `59` &rarr; "Kategori: Dewasa"
     - `>= 60` &rarr; "Kategori: Lansia"

# Hint

- Bangun HTML dan CSS dulu sampai form terlihat rapi dan bisa diisi,
  BARU kerjakan JavaScript-nya.
- `.value` dari `<input type="number">` tetap berupa teks — ubah dulu
  ke angka dengan `Number(...)` sebelum dibandingkan dengan `if`.
- Pecah jadi dua bagian di dalam function-mu: bagian yang menyusun
  pesan sambutan, dan bagian if/else untuk kategori umur. Boleh
  digabung jadi satu string besar sebelum ditulis ke `#hasil`.
- Kalau bingung strukturnya, lihat lagi pola `sapa()` di
  `07-dom-interaction` dan pola if/else di `06-javascript-basic`.
- Boleh bungkus label & input dalam `<div>` biasa (seperti pola di
  `07-dom-interaction`), tidak wajib pakai tag `<form>`. Kalau kamu
  tetap ingin pakai `<form>`, ingat: tombol di dalamnya akan otomatis
  mencoba "submit" dan me-reload halaman — hal yang belum kita
  pelajari cara menanganinya.

# Checklist

- [ ] Form berisi input Nama, input Umur, dan tombol.
- [ ] Form terbungkus rapi dalam kartu.
- [ ] Klik tombol menampilkan pesan sambutan berisi nama.
- [ ] Pesan juga menampilkan kategori umur yang benar sesuai rentangnya.
- [ ] Tidak ada error di Console.

# Hasil Akhir

Form pendaftaran yang benar-benar interaktif — mengambil input,
memprosesnya dengan logika if/else, lalu menampilkan hasilnya
langsung di halaman tanpa reload.
