# Buggy

# Tujuan

Melatih kebiasaan paling penting seorang developer: membaca kode
orang lain, menjalankannya, membandingkan hasil dengan yang
seharusnya, lalu menemukan penyebabnya — bukan menghafal syntax.

# Yang Dipelajari

| File | Bug | Konsep yang diuji |
|---|---|---|
| `bug_01.py` | Tipe data salah | String tidak bisa langsung digabung (`+`) dengan integer |
| `bug_02.py` | Kondisi terbalik | Membaca ulang logika perbandingan pada `if` |
| `bug_03.py` | Function tidak `return` nilai | Function tanpa `return` selalu menghasilkan `None` |
| `bug_04.py` | Logika grade bertingkat salah | Urutan `if/elif` menentukan kondisi mana yang duluan dicek |

# File yang Harus Diedit

Perbaiki langsung di file yang sama (`bug_01.py` sampai `bug_04.py`).
Jangan mengubah tujuan program — hanya perbaiki bagian yang salah.

# Ekspektasi Hasil

Setiap file, setelah dijalankan dengan `python bug_0X.py`, mencetak
output yang sesuai dengan yang dideskripsikan di komentar "MISI KAMU"
pada masing-masing file.

# Hint

- Jalankan dulu SEBELUM menebak — baca pesan error atau outputnya,
  baru cocokkan dengan komentar "Petunjuk" di bagian bawah file.
- `bug_02` dan `bug_04` tidak menghasilkan error sama sekali — kodenya
  jalan lancar, tapi HASILNYA salah. Ini bug logika, bukan bug syntax,
  jadi harus ditelusuri lewat tracing manual (jalankan di kepala).
- `bug_04` khusus: Python mengevaluasi `if/elif` dari atas ke bawah
  dan berhenti begitu satu kondisi bernilai `True`. Urutan
  kondisinya yang perlu disusun ulang.

# Checklist

- [ ] `bug_01.py` — output "Nama: Rafi, Umur: 19 tahun" tanpa error.
- [ ] `bug_02.py` — nilai 75 mencetak "Selamat, kamu lulus!".
- [ ] `bug_03.py` — mencetak "Harga setelah diskon: 160000.0".
- [ ] `bug_04.py` — nilai 85 mencetak "Grade: B".

# Hasil Akhir

Empat kebiasaan debugging dasar yang akan terus kamu pakai di setiap
project — termasuk saat masuk ke JavaScript di Pertemuan 2.
