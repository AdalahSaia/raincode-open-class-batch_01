# 01 · HTML Basic

# Tujuan

Memahami kerangka dasar dokumen HTML dan mengenal tag-tag yang paling
sering dipakai: `h1`-`h6`, `p`, `ul`/`li`, `a`, dan `img`.

# Yang Dipelajari

- Struktur wajib: `<!DOCTYPE html>`, `<html>`, `<head>`, `<body>`.
- Beda `<head>` (tak terlihat pengunjung) dan `<body>` (terlihat pengunjung).
- Tag berpasangan: pembuka `<p>` selalu butuh penutup `</p>`.
- Tag judul `<h1>` sampai `<h6>`, dari terbesar ke terkecil.
- Membuat daftar berpoin dengan `<ul>` dan `<li>`.
- Membuat tautan yang bisa diklik dengan `<a href="...">`.
- Menampilkan gambar dengan `<img src="..." alt="...">`.

# File yang Harus Diedit

- `index.html` — ikuti setiap komentar `TODO` dari atas ke bawah.

# Ekspektasi Hasil

Saat dibuka di Live Server, halaman menampilkan (masih polos, belum ada
CSS — itu normal):

1. Judul halaman di tab browser (dari `<title>`).
2. Satu `<h1>` sebagai judul utama.
3. Dua paragraf perkenalan diri.
4. Judul "Hal yang Ingin Aku Pelajari" + daftar berpoin minimal 3 item.
5. Judul "Tautan Favoritku" + satu tautan yang bisa diklik.
6. Judul "Foto" + satu gambar.

# Hint

- Lupa tag apa isinya? Buka `.README` di folder ini lagi, atau cek
  Cheat Sheet bagian "Tag HTML paling sering dipakai".
- Kalau halaman terlihat kosong padahal sudah menulis kode, cek: apakah
  kode kamu ada di dalam `<body>`, bukan di dalam `<head>`?
- Tag pembuka dan penutup harus punya nama yang SAMA persis.
  `<h1>...</h2>` itu salah — perhatikan angkanya.

# Checklist

- [ ] `<title>` sudah diisi dan muncul di tab browser.
- [ ] Ada tepat satu `<h1>` di halaman.
- [ ] Dua paragraf perkenalan sudah ditulis dan tertutup rapi.
- [ ] Daftar `<ul><li>` berisi minimal 3 item.
- [ ] Tautan `<a href="...">` bisa diklik dan membuka halaman baru.
- [ ] Gambar tampil (atau muncul teks `alt` kalau gambar gagal dimuat).

# Hasil Akhir

Satu halaman HTML polos — hitam putih, menumpuk ke bawah — tapi sudah
punya struktur, judul, daftar, tautan, dan gambar. Belum cantik, tapi
ini sudah "website beneran".
