"""
services/expense_service.py - Business Logic Layer
====================================================

INI BAGIAN YANG HARUS KAMU BANGUN.

Ini "otak" aplikasinya — tempat aturan bisnis hidup, terpisah dari
Route (app.py) dan Repository (SQL). `ExpenseService` yang memutuskan
APAKAH data boleh disimpan (validasi), Repository yang memutuskan
BAGAIMANA cara menyimpannya.

ATURAN MAIN:
    - Service TIDAK PERNAH menulis SQL langsung — selalu lewat
      self.repository.
    - Validasi selalu dilakukan di server (bukan cuma di JavaScript),
      karena JavaScript bisa dilewati siapa pun yang mau curang.
    - Kalau input tidak valid, lempar ValueError dengan pesan yang
      jelas — app.py akan menangkapnya dan menampilkannya ke user.

Kalau bingung mulai dari mana, buka lagi:
- exercises/meet-03/07-create-expense (validasi sebelum simpan)
- exercises/meet-03/11-complete-crud (validasi kategori)
- ../../final/services/expense_service.py — HANYA setelah kamu mencoba sendiri
"""

from typing import Optional

from models.expense_model import EXPENSE_CATEGORIES
from repositories.expense_repository import ExpenseRepository
from utils.logger import get_logger

logger = get_logger(__name__)

# TODO 1: definisikan batas aturan bisnis sebagai konstanta, misalnya:
#   MIN_AMOUNT, MAX_AMOUNT, MAX_TITLE_LENGTH, MAX_NOTES_LENGTH
# Nilai spesifiknya terserah kamu, yang penting konsisten dipakai di
# _validate_and_clean() di bawah.


class ExpenseService:
    """
    Semua business logic untuk expense: validasi input, format output,
    dan orkestrasi pemanggilan ke repository.
    """

    def __init__(self) -> None:
        self.repository = ExpenseRepository()

    # ── Categories ─────────────────────────────────────────────────────────────

    def get_categories(self) -> list[str]:
        """Kembalikan daftar kategori yang valid (dari models/expense_model.py)."""
        return EXPENSE_CATEGORIES

    # ── CREATE ─────────────────────────────────────────────────────────────────

    def create_expense(self, form_data: dict) -> dict:
        """
        Validasi form_data, simpan lewat repository, lalu kembalikan hasil
        yang sudah diformat untuk ditampilkan.

        TODO:
            1. cleaned = self._validate_and_clean(form_data)
            2. expense = self.repository.create_expense(**cleaned)
            3. logger.info(...) untuk mencatat keberhasilan
            4. return self._format_expense(expense)
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
        TODO: ambil raw_expenses dari repository, lalu format tiap
              elemennya lewat self._format_expense() sebelum dikembalikan.
        """
        raise NotImplementedError("get_expenses() belum diimplementasikan")

    def get_expense_by_id(self, expense_id: int) -> Optional[dict]:
        """
        TODO: ambil dari repository, format kalau ketemu, kembalikan
              None kalau tidak ada.
        """
        raise NotImplementedError("get_expense_by_id() belum diimplementasikan")

    def get_recent_expenses(self, limit: int = 5) -> list[dict]:
        """TODO: sama seperti get_expenses(), tapi memanggil get_recent_expenses()."""
        raise NotImplementedError("get_recent_expenses() belum diimplementasikan")

    def get_summary(self) -> dict:
        """
        Hitung total, jumlah transaksi, dan rata-rata pengeluaran.

        TODO:
            1. total = self.repository.get_total_amount()
            2. count = self.repository.get_expense_count()
            3. average = total / count kalau count > 0, selain itu 0.0
            4. Kembalikan dict berisi total_amount, formatted_total,
               expense_count, average_amount (pakai self._format_currency).
        """
        raise NotImplementedError("get_summary() belum diimplementasikan")

    def get_category_totals(self) -> list[dict]:
        """
        Tambahkan persentase pada data kategori dari repository.

        TODO:
            1. Ambil category_data dari repository.
            2. Hitung grand_total = jumlah semua total_amount.
            3. Untuk tiap kategori, hitung percentage = amount / grand_total * 100
               (0.0 kalau grand_total 0), lalu susun dict berisi category,
               total_amount, formatted_amount, expense_count, percentage.
        """
        raise NotImplementedError("get_category_totals() belum diimplementasikan")

    # ── UPDATE ─────────────────────────────────────────────────────────────────

    def update_expense(self, expense_id: int, form_data: dict) -> dict:
        """
        TODO: validasi form_data, panggil repository.update_expense(),
              format hasilnya, log keberhasilan, kembalikan.
        """
        raise NotImplementedError("update_expense() belum diimplementasikan")

    # ── DELETE ─────────────────────────────────────────────────────────────────

    def delete_expense(self, expense_id: int) -> bool:
        """
        TODO: panggil repository.delete_expense(), log hasilnya
              (berhasil/tidak ketemu), kembalikan True/False-nya.
        """
        raise NotImplementedError("delete_expense() belum diimplementasikan")

    # ── Private Helpers ────────────────────────────────────────────────────────

    def _validate_and_clean(self, form_data: dict) -> dict:
        """
        Validasi & bersihkan input form. Lempar ValueError dengan pesan
        yang jelas kalau ada yang tidak valid.

        TODO — validasi minimal yang harus ada:
            - title: wajib diisi, tidak boleh melebihi batas panjang.
            - amount: wajib diisi, harus bisa diubah jadi float, harus
              berada di antara MIN_AMOUNT dan MAX_AMOUNT.
            - category: wajib diisi, harus ada di EXPENSE_CATEGORIES.
            - notes: opsional, tapi tetap ada batas panjang.
        Kembalikan dict berisi title, amount (float, dibulatkan 2
        desimal), category, notes yang sudah bersih (.strip()).
        """
        raise NotImplementedError("_validate_and_clean() belum diimplementasikan")

    def _format_expense(self, expense: dict) -> dict:
        """
        Tambahkan field siap-tampil ke dict expense mentah dari repository.

        TODO: kembalikan salinan `expense` (spread pakai **expense) plus
              field tambahan "formatted_amount" (pakai _format_currency)
              dan "short_notes" (pakai _truncate, max_length=60).
        """
        raise NotImplementedError("_format_expense() belum diimplementasikan")

    def _format_currency(self, amount: float) -> str:
        """
        TODO: format angka jadi string dengan pemisah ribuan, 2 desimal.
              Contoh: 25000 → "25,000.00". Hint: f-string "{amount:,.2f}".
        """
        raise NotImplementedError("_format_currency() belum diimplementasikan")

    def _truncate(self, text: str, max_length: int) -> str:
        """
        TODO: kalau panjang `text` <= max_length, kembalikan apa adanya.
              Kalau lebih panjang, potong sampai max_length karakter dan
              tambahkan "...".
        """
        raise NotImplementedError("_truncate() belum diimplementasikan")
