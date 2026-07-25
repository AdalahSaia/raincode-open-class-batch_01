// script.js
// Solusi Challenge Hard — Form Pendaftaran Interaktif

function daftar() {
    let nama = document.getElementById("nama").value;
    let umur = Number(document.getElementById("umur").value);

    let kategori = "";
    if (umur < 13) {
        kategori = "Anak-anak";
    } else if (umur <= 17) {
        kategori = "Remaja";
    } else if (umur <= 59) {
        kategori = "Dewasa";
    } else {
        kategori = "Lansia";
    }

    document.getElementById("hasil").innerText =
        "Halo " + nama + "! Pendaftaranmu berhasil. Kategori: " + kategori;
}
