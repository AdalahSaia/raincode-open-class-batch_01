"""
app.py - Flask Application & Route Definitions
================================================

INI BAGIAN YANG HARUS KAMU BANGUN.

Setup aplikasi (Flask app, secret key, init_db, error handler, entry
point) sudah disiapkan di bawah — itu bagian yang sama di semua
project Flask, bukan inti latihannya. Yang perlu kamu isi adalah ENAM
route: index, expenses, create, edit, delete, summary.

Pola tiap route SAMA seperti yang sudah kamu bangun folder demi folder
di exercises/meet-03 (07 sampai 11):
    1. Terima request (form data / query parameter / URL parameter).
    2. Panggil expense_service (jangan pernah menulis SQL di sini).
    3. Tangani ValueError (kesalahan input user) secara berbeda dari
       Exception lain (kesalahan sistem).
    4. render_template(...) atau redirect(url_for(...)).

Nama route/endpoint di bawah ini JANGAN diubah — template di
templates/*.html memanggilnya lewat url_for("nama_fungsi").

Kalau bingung mulai dari mana, buka lagi:
- exercises/meet-03/04-form-request (request.form)
- exercises/meet-03/07-create-expense s.d. 10-delete-expense
- ../../final/app.py — HANYA setelah kamu mencoba sendiri
"""

from flask import Flask, flash, redirect, render_template, request, url_for

from config import config
from database.db import init_db
from services.expense_service import ExpenseService
from utils.logger import get_logger

# ── Logger ──────────────────────────────────────────────────────────────────────
logger = get_logger(__name__)

# ── Flask App Instance ──────────────────────────────────────────────────────────
app = Flask(__name__)
app.secret_key = config.SECRET_KEY

# ── Database Setup ────────────────────────────────────────────────────────────
init_db()

# ── Service Instance ────────────────────────────────────────────────────────────
expense_service = ExpenseService()

logger.info(f"Application started | name={config.APP_NAME} | env={config.APP_ENV}")


# ══════════════════════════════════════════════════════════════════════════════
# ROUTES
# ══════════════════════════════════════════════════════════════════════════════


@app.route("/")
def index():
    """
    Dashboard — GET /, render templates/index.html.

    TODO: ambil summary (expense_service.get_summary()), recent
          expenses (get_recent_expenses), dan category_totals
          (get_category_totals), lalu render_template("index.html", ...)
          dengan ketiganya. Bungkus dengan try/except supaya kalau
          gagal, dashboard tetap tampil dengan data kosong + flash error.
    """
    raise NotImplementedError("index() belum diimplementasikan")


@app.route("/expenses")
def expenses():
    """
    Daftar expenses dengan search/filter/sort — GET /expenses.

    Query parameter yang didukung: ?search=, ?category=, ?sort=, ?order=

    TODO: baca query parameter lewat request.args.get(...), panggil
          expense_service.get_expenses(...) dan get_categories(), lalu
          render_template("expenses.html", ...).
    """
    raise NotImplementedError("expenses() belum diimplementasikan")


@app.route("/create", methods=["GET", "POST"])
def create():
    """
    Form tambah expense — GET tampilkan form kosong, POST simpan data.

    TODO:
        - GET: render_template("create.html", categories=..., form_data={})
        - POST: ambil data lewat request.form, panggil
          expense_service.create_expense(form_data). Kalau sukses,
          flash pesan berhasil lalu redirect(url_for("expenses")).
          Kalau ValueError (input tidak valid), flash pesannya dan
          render ulang form dengan form_data supaya user tidak perlu
          mengetik ulang.
    """
    raise NotImplementedError("create() belum diimplementasikan")


@app.route("/edit/<int:expense_id>", methods=["GET", "POST"])
def edit(expense_id: int):
    """
    Form edit expense — GET tampilkan form terisi, POST simpan perubahan.

    TODO:
        - Cari expense lewat expense_service.get_expense_by_id(expense_id).
          Kalau tidak ketemu, flash error dan redirect ke expenses.
        - GET: render_template("edit.html", expense=..., form_data=expense).
        - POST: sama seperti create(), tapi panggil
          expense_service.update_expense(expense_id, form_data).
    """
    raise NotImplementedError("edit() belum diimplementasikan")


@app.route("/delete/<int:expense_id>", methods=["POST"])
def delete(expense_id: int):
    """
    Hapus expense — POST /delete/<expense_id>. SENGAJA hanya POST,
    bukan GET, supaya tidak bisa ke-trigger tidak sengaja (lihat catatan
    keamanan di final/app.py kalau penasaran kenapa).

    TODO: cari expense dulu (untuk pesan flash), panggil
          expense_service.delete_expense(expense_id), flash hasilnya,
          lalu redirect(url_for("expenses")).
    """
    raise NotImplementedError("delete() belum diimplementasikan")


@app.route("/summary")
def summary():
    """
    Ringkasan pengeluaran per kategori — GET /summary.

    TODO: ambil category_totals dan summary dari expense_service,
          lalu render_template("summary.html", ...).
    """
    raise NotImplementedError("summary() belum diimplementasikan")


# ══════════════════════════════════════════════════════════════════════════════
# ERROR HANDLERS
# ══════════════════════════════════════════════════════════════════════════════

@app.errorhandler(404)
def page_not_found(error):
    logger.warning(f"404 | {request.method} {request.url}")
    return render_template("errors/404.html", page_title="Page Not Found"), 404


@app.errorhandler(500)
def internal_server_error(error):
    logger.error(f"500 | {error}")
    return render_template("errors/500.html", page_title="Server Error"), 500


# ══════════════════════════════════════════════════════════════════════════════
# ENTRY POINT
# ══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    app.run(debug=config.DEBUG, host="0.0.0.0", port=5000)
