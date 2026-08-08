// 1. Fitur Tombol Salam Interaksi🫰 + Alert masih pake tampilan web belum dikasih .css nya hehe
const btnSalam = document.getElementById('btnSalam');

btnSalam.addEventListener('click', function() {
    alert('Hallo WNI! Terima kasih sudah berkunjung ke web perkenalan Khafifatul Isaroh!\nSemoga harimu senin terus!');
});


// 2. Fitur Ganti Mode☀️ (Toggle Dark / Light Mode)
const btnGantiWarna = document.getElementById('btnGantiWarna');

btnGantiWarna.addEventListener('click', function() {
    // untuk nambah/hapus class 'dark-theme' pada tag body
    document.body.classList.toggle('dark-theme');
});


// 3. Fitur Counter Like❤️ 1x klik nambah,double klik gagal nambah
const btnLike = document.getElementById('btnLike');
const likeCount = document.getElementById('likeCount');

let totalLike = 59175;    // Set angka awal jadi 59175 biar banyak yang like kaliatannya
let isLiked = false;  // Status user saat ini belum like

// Tampilkan angka 5 di layar saat pertama kali web dimuat
if (likeCount) {
    likeCount.textContent = totalLike;
}

if (btnLike && likeCount) {
    btnLike.addEventListener('click', function() {
        if (!isLiked) {
            // KLIK PERTAMA: Angka 59175 jadi 59176
            totalLike++;
            isLiked = true;
            btnLike.classList.add('liked');
        } else {
            // KLIK KEDUA: Angka 59176 balik lagi jadi 59175
            totalLike--;
            isLiked = false;
            btnLike.classList.remove('liked');
        }
        
        // Update angka di layar
        likeCount.textContent = totalLike;
    });
}