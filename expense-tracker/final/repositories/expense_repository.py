"""
repositories/expense_repository.py - Data Access Layer
========================================================

WHY THIS FILE EXISTS:
    This is the ONLY file in the project that writes raw SQL queries.
    Every database operation for expenses is defined here.

WHAT IS THE REPOSITORY PATTERN?
    Think of this as the "librarian" of your data.

    You tell the librarian: "Find me all Food expenses sorted by date."
    The librarian knows exactly which shelf (table) to look at, how to search,
    and brings back exactly what you asked for.
    You don't need to know HOW the library is organized — you just make requests.

    ┌──────────────┐     ┌──────────────────────┐     ┌──────────────┐
    │  app.py      │ →   │  expense_service.py  │ →   │  expense_    │ → SQLite
    │  (routes)    │     │  (business logic)    │     │  repository  │
    └──────────────┘     └──────────────────────┘     └──────────────┘

WHY SEPARATE FROM SERVICE?
    Repository = "HOW to store/retrieve" (database operations only)
    Service    = "WHETHER to store and WHAT rules apply" (business logic)

    Benefit: If you switch from SQLite → PostgreSQL → MongoDB,
    you ONLY update this file. The service and routes stay unchanged.

SQL INJECTION PROTECTION:
    ✅ SAFE:   cursor.execute("SELECT * FROM expenses WHERE id = ?", (expense_id,))
    ❌ UNSAFE: cursor.execute(f"SELECT * FROM expenses WHERE id = {expense_id}")

    The ? placeholder tells SQLite to treat the value as DATA, not SQL code.
    An attacker who enters  1; DROP TABLE expenses; --  as an ID will just get
    "no results found" — the malicious SQL never executes.
"""

import sqlite3
from typing import Optional

from database.db import get_connection
from utils.logger import get_logger

logger = get_logger(__name__)


class ExpenseRepository:
    """
    All database operations for the expenses table.

    Each method performs exactly ONE database operation and returns
    plain Python dictionaries (not custom objects).

    Naming convention:
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
        Insert a new expense row into the database.

        The database automatically sets:
        - id (AUTOINCREMENT)
        - created_at (DEFAULT datetime('now', 'localtime'))
        - updated_at (DEFAULT datetime('now', 'localtime'))

        Args:
            title:    Expense description
            amount:   Cost amount
            category: Expense category
            notes:    Optional notes

        Returns:
            dict: The newly created expense including its auto-generated id

        Raises:
            sqlite3.Error: If the INSERT fails
        """
        sql = """
            INSERT INTO expenses (title, amount, category, notes)
            VALUES (?, ?, ?, ?)
        """
        try:
            with get_connection() as conn:
                cursor = conn.execute(sql, (title, amount, category, notes))
                conn.commit()

                # lastrowid gives us the auto-generated id from AUTOINCREMENT
                new_id = cursor.lastrowid

            # Fetch and return the complete record (including timestamps)
            return self.get_expense_by_id(new_id)

        except sqlite3.Error as e:
            logger.error(f"DB error creating expense | title={title} | {e}")
            raise

    # ── READ ───────────────────────────────────────────────────────────────────

    def get_expenses(
        self,
        search: str = "",
        category: str = "",
        sort_by: str = "created_at",
        order: str = "desc",
    ) -> list[dict]:
        """
        Retrieve expenses with optional search, filter, and sorting.

        Dynamic WHERE clause:
            - If search is provided: filters title OR notes with LIKE
            - If category is provided: exact match on category column
            - Both can be combined

        Args:
            search:   Text to search in title and notes (partial match)
            category: Exact category name to filter by
            sort_by:  Column to sort by
            order:    'asc' or 'desc'

        Returns:
            list[dict]: List of matching expenses as dictionaries
        """
        # ── Whitelist sort column to prevent SQL injection ──────────────────────
        # We CANNOT use ? placeholders for column names, only for values.
        # So we validate manually against a known-safe set of column names.
        allowed_columns = {"id", "title", "amount", "category", "created_at", "updated_at"}
        if sort_by not in allowed_columns:
            sort_by = "created_at"

        # Normalize order direction
        order_sql = "DESC" if order.strip().lower() == "desc" else "ASC"

        # ── Build WHERE clause dynamically ─────────────────────────────────────
        # We build conditions as a list, then join them with AND
        # Parameters are collected separately to keep them OUT of the SQL string
        conditions: list[str] = []
        params: list = []

        if search:
            # LIKE with % wildcards → "coffee" matches "Morning Coffee", "Coffee Shop"
            conditions.append("(title LIKE ? OR notes LIKE ?)")
            params.extend([f"%{search}%", f"%{search}%"])

        if category:
            conditions.append("category = ?")
            params.append(category)

        where_clause = ("WHERE " + " AND ".join(conditions)) if conditions else ""

        sql = f"""
            SELECT id, title, amount, category, notes, created_at, updated_at
            FROM   expenses
            {where_clause}
            ORDER  BY {sort_by} {order_sql}
        """

        try:
            with get_connection() as conn:
                cursor = conn.execute(sql, params)
                rows = cursor.fetchall()
                # Convert sqlite3.Row objects to plain dicts
                return [dict(row) for row in rows]

        except sqlite3.Error as e:
            logger.error(f"DB error fetching expenses | search={search} | {e}")
            raise

    def get_expense_by_id(self, expense_id: int) -> Optional[dict]:
        """
        Retrieve a single expense by its primary key.

        Args:
            expense_id: The unique ID of the expense

        Returns:
            dict: Expense data if found
            None: If no expense with that ID exists
        """
        sql = """
            SELECT id, title, amount, category, notes, created_at, updated_at
            FROM   expenses
            WHERE  id = ?
        """
        try:
            with get_connection() as conn:
                cursor = conn.execute(sql, (expense_id,))
                row = cursor.fetchone()
                return dict(row) if row else None

        except sqlite3.Error as e:
            logger.error(f"DB error fetching expense | id={expense_id} | {e}")
            raise

    def get_recent_expenses(self, limit: int = 5) -> list[dict]:
        """
        Retrieve the N most recently created expenses.

        Used on the dashboard to show latest activity.

        Args:
            limit: Maximum number of expenses to return

        Returns:
            list[dict]: Most recent expenses, newest first
        """
        sql = """
            SELECT id, title, amount, category, notes, created_at, updated_at
            FROM   expenses
            ORDER  BY created_at DESC
            LIMIT  ?
        """
        try:
            with get_connection() as conn:
                cursor = conn.execute(sql, (limit,))
                rows = cursor.fetchall()
                return [dict(row) for row in rows]

        except sqlite3.Error as e:
            logger.error(f"DB error fetching recent expenses: {e}")
            raise

    def get_category_totals(self) -> list[dict]:
        """
        Calculate total spending and count per category using SQL aggregation.

        SQL Lesson — Aggregation functions:
            SUM(amount)  → adds up all amounts in the group
            COUNT(*)     → counts how many rows are in the group
            GROUP BY     → creates one result row per unique category value
            ORDER BY ... DESC → highest spending categories first

        Returns:
            list[dict]: Each dict has 'category', 'total_amount', 'expense_count'
        """
        sql = """
            SELECT
                category,
                SUM(amount)  AS total_amount,
                COUNT(*)     AS expense_count
            FROM   expenses
            GROUP  BY category
            ORDER  BY total_amount DESC
        """
        try:
            with get_connection() as conn:
                cursor = conn.execute(sql)
                rows = cursor.fetchall()
                return [dict(row) for row in rows]

        except sqlite3.Error as e:
            logger.error(f"DB error fetching category totals: {e}")
            raise

    def get_total_amount(self) -> float:
        """
        Calculate the grand total of all expenses.

        COALESCE(SUM(amount), 0):
            SUM of an empty table returns NULL in SQL.
            COALESCE returns the first non-NULL value.
            So if there are no expenses, we get 0 instead of NULL.

        Returns:
            float: Total amount of all expenses (0.0 if none exist)
        """
        sql = "SELECT COALESCE(SUM(amount), 0) AS total FROM expenses"
        try:
            with get_connection() as conn:
                cursor = conn.execute(sql)
                row = cursor.fetchone()
                return float(row["total"])

        except sqlite3.Error as e:
            logger.error(f"DB error calculating total: {e}")
            raise

    def get_expense_count(self) -> int:
        """
        Count the total number of expense records.

        Returns:
            int: Total number of expenses in the database
        """
        sql = "SELECT COUNT(*) AS count FROM expenses"
        try:
            with get_connection() as conn:
                cursor = conn.execute(sql)
                row = cursor.fetchone()
                return int(row["count"])

        except sqlite3.Error as e:
            logger.error(f"DB error counting expenses: {e}")
            raise

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
        Update all fields of an existing expense.

        Also sets updated_at to the current timestamp.
        The WHERE id = ? ensures we only update the intended row.

        Args:
            expense_id: ID of the expense to update
            title:      New title
            amount:     New amount
            category:   New category
            notes:      New notes

        Returns:
            dict: The updated expense with fresh timestamps
        """
        sql = """
            UPDATE expenses
            SET
                title      = ?,
                amount     = ?,
                category   = ?,
                notes      = ?,
                updated_at = datetime('now', 'localtime')
            WHERE id = ?
        """
        try:
            with get_connection() as conn:
                conn.execute(sql, (title, amount, category, notes, expense_id))
                conn.commit()

            return self.get_expense_by_id(expense_id)

        except sqlite3.Error as e:
            logger.error(f"DB error updating expense | id={expense_id} | {e}")
            raise

    # ── DELETE ─────────────────────────────────────────────────────────────────

    def delete_expense(self, expense_id: int) -> bool:
        """
        Permanently delete an expense by its ID.

        Args:
            expense_id: The ID of the expense to delete

        Returns:
            True:  If the expense was found and deleted
            False: If no expense with that ID was found

        Note:
            cursor.rowcount tells us how many rows were affected.
            If rowcount == 0, the expense didn't exist.
        """
        sql = "DELETE FROM expenses WHERE id = ?"
        try:
            with get_connection() as conn:
                cursor = conn.execute(sql, (expense_id,))
                conn.commit()
                return cursor.rowcount > 0

        except sqlite3.Error as e:
            logger.error(f"DB error deleting expense | id={expense_id} | {e}")
            raise
