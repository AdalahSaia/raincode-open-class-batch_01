"""
database/db.py - Database Connection & Initialization
======================================================

INI BAGIAN YANG HARUS KAMU BANGUN.

Fungsi file ini SAMA seperti yang sudah kamu buat di
exercises/meet-03/06-create-table: membuka koneksi SQLite dan membuat
tabel `expenses` kalau belum ada. Bedanya, di sini logikanya dipisah
dari app.py supaya jadi satu-satunya tempat yang tahu cara membuka
database.

Kalau bingung mulai dari mana, buka lagi:
- exercises/meet-03/05-sqlite-basic (koneksi & query dasar)
- exercises/meet-03/06-create-table (CREATE TABLE IF NOT EXISTS)
- ../../final/database/db.py — HANYA setelah kamu mencoba sendiri

SKEMA TABEL YANG DIHARAPKAN (dipakai oleh repository & template):
    CREATE TABLE IF NOT EXISTS expenses (
        id          INTEGER PRIMARY KEY AUTOINCREMENT,
        title       TEXT    NOT NULL,
        amount      REAL    NOT NULL,
        category    TEXT    NOT NULL DEFAULT 'Other',
        notes       TEXT             DEFAULT '',
        created_at  TEXT    NOT NULL DEFAULT (datetime('now', 'localtime')),
        updated_at  TEXT    NOT NULL DEFAULT (datetime('now', 'localtime'))
    );
"""

import os
import sqlite3

from config import config
from utils.logger import get_logger

logger = get_logger(__name__)

# TODO 1: Tulis SQL "CREATE TABLE IF NOT EXISTS expenses (...)" di sini,
#         sesuai skema pada docstring di atas.
_CREATE_EXPENSES_TABLE = """
"""


def get_connection() -> sqlite3.Connection:
    """
    Buka dan kembalikan koneksi SQLite baru.

    PENTING: semua bagian aplikasi WAJIB lewat fungsi ini untuk
    mengakses database — jangan panggil sqlite3.connect() di file lain.

    Langkah yang perlu kamu isi:
        1. Pastikan folder tempat file database berada sudah ada
           (config.DATABASE_PATH) — buat kalau belum ada.
        2. Buka koneksi dengan sqlite3.connect(config.DATABASE_PATH).
        3. Set connection.row_factory = sqlite3.Row supaya baris hasil
           query bisa diakses seperti dictionary (row["title"]).
        4. Kembalikan koneksi tersebut.
    """
    # TODO 2: implementasikan sesuai langkah di atas.
    raise NotImplementedError("get_connection() belum diimplementasikan")


def init_db() -> None:
    """
    Jalankan _CREATE_EXPENSES_TABLE lewat get_connection(), lalu commit.

    Dipanggil SEKALI saat aplikasi start (lihat app.py). Karena SQL-nya
    pakai "IF NOT EXISTS", aman dipanggil berkali-kali.
    """
    # TODO 3: buka koneksi, jalankan _CREATE_EXPENSES_TABLE, commit.
    raise NotImplementedError("init_db() belum diimplementasikan")
