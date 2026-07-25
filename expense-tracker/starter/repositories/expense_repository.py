"""
repositories/expense_repository.py - Data Access Layer
========================================================

INI BAGIAN YANG HARUS KAMU BANGUN.

Ini satu-satunya file yang boleh berisi SQL mentah — persis prinsip
yang sudah kamu pakai di seluruh exercises/meet-03 (07 sampai 11).
`ExpenseService` (lapisan di atasnya) memanggil method-method di
class ini tanpa tahu SQL-nya seperti apa — dia cuma tahu "minta data,
dapat dictionary balik".

ATURAN MAIN:
    - Setiap method di sini melakukan TEPAT SATU operasi database.
    - Selalu pakai placeholder `?` untuk value, JANGAN f-string
      langsung ke dalam SQL (itu celah SQL Injection).
    - Method mengembalikan dict atau list[dict] biasa — bukan objek
      kustom — supaya lapisan Service & Route mudah memakainya.

Kalau bingung mulai dari mana, buka lagi:
- exercises/meet-03/07-create-expense s.d. 10-delete-expense (CRUD dasar)
- exercises/meet-03/11-complete-crud (CRUD lengkap + kategori)
- ../../final/repositories/expense_repository.py — HANYA setelah kamu mencoba sendiri
"""

import sqlite3
from typing import Optional

from database.db import get_connection
from utils.logger import get_logger

logger = get_logger(__name__)


class ExpenseRepository:
    """
    Semua operasi database untuk tabel `expenses`.

    Naming convention (ikuti ini supaya konsisten dengan Service):
        create_*   → INSERT
        get_*      → SELECT
        update_*   → UPDATE
        delete_*   → DELETE
    """

    # ── CREATE ─────────────────────────────────────────────────────────────────

    def create_expense(
        self,
        title: str,
        amount: float,
        category: str,
        notes: str,
    ) -> dict:
        """
        INSERT satu baris baru ke tabel expenses, lalu kembalikan baris
        lengkapnya (termasuk id dan timestamp yang dibuat otomatis oleh DB).

        TODO:
            1. Tulis SQL INSERT dengan placeholder `?` untuk keempat kolom.
            2. Jalankan lewat get_connection(), lalu conn.commit().
            3. Ambil id baris baru dari cursor.lastrowid.
            4. Panggil self.get_expense_by_id(new_id) dan kembalikan hasilnya.
        """
        raise NotImplementedError("create_expense() belum diimplementasikan")

    # ── READ ───────────────────────────────────────────────────────────────────

    def get_expenses(
        self,
        search: str = "",
        category: str = "",
        sort_by: str = "created_at",
        order: str = "desc",
    ) -> list[dict]:
        """
        Ambil daftar expenses, dengan pencarian, filter, dan sorting opsional.

        TODO:
            1. Whitelist `sort_by` terhadap kolom yang diizinkan
               ({"id", "title", "amount", "category", "created_at", "updated_at"})
               — kolom TIDAK BISA memakai placeholder `?`, jadi validasi manual.
            2. Kalau `search` diisi: tambahkan kondisi
               "(title LIKE ? OR notes LIKE ?)" dengan value f"%{search}%".
            3. Kalau `category` diisi: tambahkan kondisi "category = ?".
            4. Gabungkan kondisi dengan AND, susun jadi klausa WHERE (kalau ada).
            5. Jalankan SELECT ... ORDER BY {sort_by} {ASC/DESC}.
            6. Ubah setiap sqlite3.Row jadi dict sebelum dikembalikan.
        """
        raise NotImplementedError("get_expenses() belum diimplementasikan")

    def get_expense_by_id(self, expense_id: int) -> Optional[dict]:
        """
        Ambil satu expense berdasarkan id.

        TODO: SELECT ... WHERE id = ?. Kembalikan dict kalau ketemu,
              None kalau tidak ada baris yang cocok.
        """
        raise NotImplementedError("get_expense_by_id() belum diimplementasikan")

    def get_recent_expenses(self, limit: int = 5) -> list[dict]:
        """
        Ambil N expense terbaru (untuk dashboard).

        TODO: SELECT ... ORDER BY created_at DESC LIMIT ?.
        """
        raise NotImplementedError("get_recent_expenses() belum diimplementasikan")

    def get_category_totals(self) -> list[dict]:
        """
        Hitung total & jumlah expense per kategori pakai SQL aggregation.

        TODO: SELECT category, SUM(amount) AS total_amount,
              COUNT(*) AS expense_count FROM expenses GROUP BY category
              ORDER BY total_amount DESC.
        """
        raise NotImplementedError("get_category_totals() belum diimplementasikan")

    def get_total_amount(self) -> float:
        """
        Hitung total keseluruhan semua expense.

        TODO: SELECT COALESCE(SUM(amount), 0) AS total FROM expenses —
              COALESCE penting supaya tabel kosong menghasilkan 0, bukan NULL.
        """
        raise NotImplementedError("get_total_amount() belum diimplementasikan")

    def get_expense_count(self) -> int:
        """
        Hitung jumlah baris expense.

        TODO: SELECT COUNT(*) AS count FROM expenses.
        """
        raise NotImplementedError("get_expense_count() belum diimplementasikan")

    # ── UPDATE ─────────────────────────────────────────────────────────────────

    def update_expense(
        self,
        expense_id: int,
        title: str,
        amount: float,
        category: str,
        notes: str,
    ) -> Optional[dict]:
        """
        Update semua kolom milik satu expense, dan set updated_at ke waktu
        sekarang.

        TODO:
            1. UPDATE expenses SET title=?, amount=?, category=?, notes=?,
               updated_at=datetime('now','localtime') WHERE id=?.
            2. commit().
            3. Kembalikan self.get_expense_by_id(expense_id).
        """
        raise NotImplementedError("update_expense() belum diimplementasikan")

    # ── DELETE ─────────────────────────────────────────────────────────────────

    def delete_expense(self, expense_id: int) -> bool:
        """
        Hapus satu expense berdasarkan id.

        TODO: DELETE FROM expenses WHERE id = ?, commit(), lalu kembalikan
              True kalau ada baris yang terhapus (cursor.rowcount > 0),
              False kalau tidak ada.
        """
        raise NotImplementedError("delete_expense() belum diimplementasikan")
