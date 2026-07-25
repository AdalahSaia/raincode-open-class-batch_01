// script.js
// Topik: JavaScript Dasar — Variabel, If-Else, Function

// ============================================================
// LOGIKA P1 HIDUP LAGI — beda kulit saja
// ============================================================
// Ingat variabel, if-else, function dari Pertemuan 1 (Python)?
// Semua itu hidup lagi di sini, cuma "kulitnya" beda:
//
//   Python (minggu lalu)          JavaScript (hari ini)
//   umur = 20                     let umur = 20;
//   if umur >= 18:                if (umur >= 18) {
//       print("Boleh daftar")         console.log("Boleh daftar");
//   else:                         } else {
//       print("Belum cukup")          console.log("Belum cukup");
//                                 }
//
// Cara berpikirnya SAMA PERSIS. Yang beda: JS pakai ( ) untuk
// kondisi, { } untuk blok kode, dan titik koma ; di akhir baris.
// ============================================================


// ============================================================
// BAGIAN 1 — Variabel
// ============================================================
// let   -> variabel yang isinya BOLEH berubah
// const -> variabel yang isinya TETAP, tidak boleh diubah lagi

// TODO 1: Buat 3 variabel tentang dirimu:
//   const nama = "..."
//   let umur = ...
//   const kota = "..."


// TODO 2: Cetak ketiganya ke Console pakai console.log()
//   Pola: console.log("Nama:", nama);
//   Boleh gabung dalam satu baris:
//   console.log("Nama:", nama, "| Umur:", umur, "| Kota:", kota);


// ============================================================
// BAGIAN 2 — Template string (gabung teks & variabel)
// ============================================================
// JS punya cara gabung teks yang mirip f-string di Python, tapi
// pakai backtick (`) dan ${...}:
//   console.log(`Nama saya ${nama}, umur ${umur} tahun`);

// TODO 3: Cetak satu kalimat perkenalan pakai template string di atas.


// ============================================================
// BAGIAN 3 — If / Else
// ============================================================
// TODO 4: Buat variabel nilai = 82 (angka bebas),
//   lalu tulis if/elif/else versi JS untuk menentukan grade:
//     >= 90        -> "A"
//     >= 80        -> "B"
//     >= 70        -> "C"
//     >= 60        -> "D"
//     di bawah 60  -> "E"
//   Cetak hasilnya: console.log("Grade:", grade);
//
//   Pola if/else if/else di JS:
//     if (nilai >= 90) {
//         ...
//     } else if (nilai >= 80) {
//         ...
//     } else {
//         ...
//     }


// ============================================================
// BAGIAN 4 — Function
// ============================================================
// TODO 5: Buat function sapa(nama) yang RETURN kalimat sapaan.
//   Pola:
//     function sapa(nama) {
//         return "Halo, " + nama + "!";
//     }

// TODO 6: Panggil function sapa() dengan namamu, simpan hasilnya
//   ke variabel, lalu cetak ke Console.
//   Pola:
//     let pesan = sapa("Budi");
//     console.log(pesan);


// ============================================================
// BONUS (opsional)
// ============================================================
// Buat function kuadrat(angka) yang me-return angka pangkat 2,
// lalu cetak hasil kuadrat(4) ke Console. (JS pakai angka ** 2
// sama seperti Python.)
