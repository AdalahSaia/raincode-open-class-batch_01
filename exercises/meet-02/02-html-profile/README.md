# 02 · HTML Profile

# Tujuan

Membangun kerangka HTML dari project utama kelas ini: **Website Profil
Diri**. Folder ini adalah titik awal — hasilnya akan dipercantik di
`04-css-profile` dan dibuat interaktif di `08-final-project`.

# Yang Dipelajari

- Memakai tag semantik `<header>`, `<main>`, `<section>`, `<footer>`
  untuk menandai area halaman yang bermakna (bukan sekadar `<div>`).
- Menyusun satu halaman utuh dari potongan-potongan kecil.
- Mengorganisir konten per topik memakai `<section>` + `<h2>`.
- Menampilkan foto profil dengan `<img>`.

# File yang Harus Diedit

- `index.html` — ikuti komentar `TODO 1` sampai `TODO 7`.

# Ekspektasi Hasil

Halaman menampilkan (masih polos, belum ada CSS):

1. Foto (atau placeholder), nama, dan peran singkat di bagian atas.
2. Section "Tentang Saya" dengan cerita singkat.
3. Section "Hobi" berisi daftar minimal 3 hobi.
4. Section "Kontak" dengan satu tautan yang bisa diklik.
5. Footer penutup di bagian paling bawah.

# Hint

- Pakai datamu sendiri — bukan contoh "Arin Pratiwi" dari modul.
- Belum punya foto? `https://placehold.co/120x120` bisa dipakai sebagai
  foto sementara.
- `<section>` boleh dipakai berkali-kali dalam satu halaman — setiap
  section berdiri sendiri sebagai satu topik.
- Kalau bingung urutan tag bersarang, ingat "pohon": `body` membungkus
  `header`/`main`/`footer`, dan `main` membungkus beberapa `section`.

# Checklist

- [ ] `<header>` berisi foto, nama (`h1`), dan peran (`p`).
- [ ] `<main>` berisi 3 `<section>`: Tentang Saya, Hobi, Kontak.
- [ ] Section Hobi memakai `<ul><li>` dengan minimal 3 item.
- [ ] Section Kontak memakai `<a href="...">` yang bisa diklik.
- [ ] `<footer>` berisi satu paragraf penutup.
- [ ] Semua tag pembuka punya pasangan tag penutup.

# Hasil Akhir

Halaman profil polos — hitam-putih, menumpuk ke bawah — tapi sudah
punya struktur lengkap: foto, nama, cerita, hobi, dan kontak. Ini
fondasi yang akan kita percantik di `04-css-profile`.
