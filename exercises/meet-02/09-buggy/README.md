# 09 · Buggy

# Tujuan

Melatih kebiasaan paling penting seorang developer: membaca kode orang
lain dan menemukan bug-nya — bukan menghafal syntax.

# Yang Dipelajari

- Kode yang "hampir benar" adalah bug yang paling sering ditemui pemula.
- Cara membaca pesan error di Console (DevTools).
- Cara memeriksa HTML/CSS lewat tab Elements di DevTools.
- Lima bug paling umum: tag tidak ditutup, tag lupa ditutup di tengah
  paragraf, CSS lupa titik koma, nama function tidak cocok, dan nama
  class yang beda huruf besar/kecil.

# File yang Harus Diedit

Setiap folder `bug-0X-...` berisi halaman yang BISA dibuka, tapi
tampilan atau interaksinya tidak sesuai harapan. Baca `README.md` di
masing-masing folder untuk tahu apa yang seharusnya terjadi, lalu
perbaiki file yang bersangkutan (`index.html`, `style.css`, atau
`script.js`).

# Ekspektasi Hasil

Setelah diperbaiki, setiap halaman bekerja persis seperti yang
dideskripsikan di README folder masing-masing — tidak lebih, tidak
kurang.

# Hint

- Jangan menebak. Buka DevTools (`F12`), baca dulu.
- Tab **Elements** untuk bug HTML/CSS (lihat struktur & style yang
  benar-benar terpakai browser).
- Tab **Console** untuk bug JavaScript (baca error dari BAWAH — biasanya
  itu yang paling relevan).
- Bandingkan nama (id, class, function) di HTML dengan yang dipakai di
  CSS/JS — bug paling umum adalah dua nama yang HAMPIR sama.

# Checklist

- [ ] `bug-01-tag-tidak-ditutup` — sudah diperbaiki.
- [ ] `bug-02-paragraf-tidak-ditutup` — sudah diperbaiki.
- [ ] `bug-03-css-titik-koma` — sudah diperbaiki.
- [ ] `bug-04-function-tidak-cocok` — sudah diperbaiki.
- [ ] `bug-05-class-besar-kecil` — sudah diperbaiki.

# Hasil Akhir

Lima kebiasaan debugging dasar yang akan terus kamu pakai di setiap
project — bukan cuma di kelas ini.
