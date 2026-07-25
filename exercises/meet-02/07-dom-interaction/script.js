// script.js
// Topik: DOM Interaction — Ambil Input, Proses, Tampilkan Hasil

// ============================================================
// INTI FRONTEND INTERAKTIF
// ============================================================
// Ambil input -> proses -> tampilkan hasil.
// Ini "mesin function" yang sama dari Pertemuan 1 — bedanya sekarang
// hidup di halaman web, bukan di terminal.
//
// Alur tombol "Sapa Saya":
//   1. <button onclick="sapa()"> -> saat diklik, jalankan function sapa()
//   2. document.getElementById("nama").value -> ambil teks yang diketik
//   3. document.getElementById("hasil").innerText = "..." -> tulis hasil
// ============================================================


// ============================================================
// BAGIAN 1 — Function sapa()
// ============================================================
// TODO 1: Lengkapi function sapa() di bawah supaya:
//   - Mengambil isi input#nama lewat .value
//   - Menuliskan "Halo, <nama>! Selamat datang di RainCode." ke p#hasil
//     lewat .innerText
//
// Pola:
//   function sapa() {
//       let nama = document.getElementById("nama").value;
//       document.getElementById("hasil").innerText = "Halo, " + nama + "! Selamat datang di RainCode.";
//   }

function sapa() {

}


// ============================================================
// BAGIAN 2 — BONUS: Function cekUmur()
// ============================================================
// TODO 2: Lengkapi function cekUmur() di bawah supaya:
//   - Mengambil isi input#umur lewat .value
//   - Karena .value SELALU berbentuk teks, ubah dulu ke angka
//     pakai Number(...) sebelum dibandingkan
//   - Pakai if/else: kalau umur >= 17, tulis "Sudah bisa buat KTP"
//     ke p#hasilUmur, kalau belum tulis "Belum waktunya buat KTP"
//
// Pola:
//   function cekUmur() {
//       let umur = Number(document.getElementById("umur").value);
//       if (umur >= 17) {
//           document.getElementById("hasilUmur").innerText = "Sudah bisa buat KTP";
//       } else {
//           document.getElementById("hasilUmur").innerText = "Belum waktunya buat KTP";
//       }
//   }

function cekUmur() {

}


// ============================================================
// JEBAKAN UMUM
// ============================================================
// - Nama function di onclick="..." HTML harus SAMA PERSIS dengan
//   nama function di script.js. sapa() vs sapaa() = tombol diam saja.
// - id di HTML (id="nama") harus SAMA PERSIS dengan id yang dicari
//   getElementById("nama") — termasuk huruf besar/kecilnya.
// - .value selalu berbentuk teks/string, walau inputnya angka.
//   Untuk perbandingan angka (>=, <), ubah dulu pakai Number(...).
