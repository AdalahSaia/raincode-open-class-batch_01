# RainCode Expense Tracker — Starter

Ini bukan latihan folder-per-folder seperti `exercises/meet-03`.
Ini kerangka **satu project utuh** — arsitektur, template, dan
tampilan sudah disiapkan, tugasmu adalah menghidupkan bagian
"otak"-nya: koneksi database, query SQL, validasi, dan route.

Anggap ini ujian akhir informal: kalau kamu bisa menyelesaikan ini
sendiri (boleh sambil buka kembali `exercises/meet-03`), itu tanda
kamu benar-benar paham alurnya, bukan cuma pernah mengikuti
langkah-langkahnya.

## Apa yang Sudah Disiapkan

| Bagian | Status |
|---|---|
| `templates/*.html` | Sudah lengkap — tampilan, form, tabel |
| `static/css`, `static/js` | Sudah lengkap — styling & interaksi UI |
| `config.py`, `utils/logger.py` | Sudah lengkap — konfigurasi & logging |
| `models/expense_model.py` | Sudah lengkap — daftar kategori |
| `database/db.py` | **Kosong, isi sendiri** — koneksi & buat tabel |
| `repositories/expense_repository.py` | **Kosong, isi sendiri** — semua query SQL |
| `services/expense_service.py` | **Kosong, isi sendiri** — validasi & business logic |
| `app.py` | **Kosong, isi sendiri** — enam route |

Kenapa frontend & infrastruktur sudah jadi? Karena fokus latihan ini
adalah alur **Route → Service → Repository → Database** — pola yang
sama yang kamu pelajari di `exercises/meet-03` dan `exercises/meet-04`.

## Urutan Mengerjakan

Ikuti urutan ini — tiap lapisan butuh lapisan di bawahnya sudah jalan:

1. **`database/db.py`** — buat koneksi jalan dan tabel `expenses` ada.
2. **`repositories/expense_repository.py`** — satu per satu method,
   test tiap method dengan memanggilnya lewat Python shell sebelum
   lanjut ke method berikutnya.
3. **`services/expense_service.py`** — validasi & format data.
4. **`app.py`** — sambungkan semuanya lewat route, baru terlihat di
   browser.

Tiap file punya komentar `TODO` yang menjelaskan apa yang perlu
diisi — baca docstring-nya dulu sebelum menulis kode.

## Cara Menjalankan

```bash
cd projects/expense-tracker/starter
pip install -r requirements.txt
cp .env.example .env
python app.py
```

Buka `http://localhost:5000` — akan error sampai kamu mengisi
lapisan-lapisan di atas. Itu wajar, error-nya adalah petunjukmu.

## Kalau Benar-Benar Mentok

Jangan langsung buka [../final](../final). Coba dulu:

1. Baca lagi folder `exercises/meet-03` yang relevan dengan lapisan
   yang sedang kamu kerjakan.
2. Jalankan aplikasi dan baca pesan error-nya baris demi baris.
3. Pakai prompt dari [ai-prompts/meet-03.md](../../../ai-prompts/meet-03.md)
   untuk minta AI menuntunmu lewat pertanyaan, bukan jawaban langsung.

Kalau sudah benar-benar mencoba dan masih stuck di satu bagian, baru
buka bagian yang sepadan di `../final` — baca satu function itu saja,
pahami, tutup lagi, lalu tulis ulang dengan pemahamanmu sendiri.
Jangan copy-paste.

## Checklist

- [ ] `database/db.py` — aplikasi bisa start tanpa error, file `.db` muncul otomatis.
- [ ] `repositories/expense_repository.py` — semua method sudah diisi.
- [ ] `services/expense_service.py` — validasi menolak input yang tidak valid dengan pesan jelas.
- [ ] `app.py` — keenam route jalan: dashboard, list, create, edit, delete, summary.
- [ ] Sudah dites lewat browser: tambah, cari, edit, hapus expense — semuanya tersimpan.

## Hasil Akhir

Expense Tracker versi kamu sendiri, dengan arsitektur rasa-industri
(Route → Service → Repository), dibangun dari kerangka kosong tanpa
panduan langkah-per-langkah — bukti kamu siap membangun project di
luar kelas.

RainCode Open Class · Understand before memorizing.
