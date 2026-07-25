"""
database/db.py - Database Connection & Initialization
======================================================

WHY THIS FILE EXISTS:
    Every part of the app that needs the database must go through here.
    This is the ONLY place in the project that knows how to open a
    SQLite connection and where the database file lives.

WHAT IS SQLite?
    SQLite is a file-based database. The entire database lives in ONE file
    (database/expense_tracker.db). No server needed, no installation needed.

    Perfect for:   Learning, small apps, desktop apps, prototypes
    Not ideal for: High-traffic production apps with many concurrent users
    Upgrade path:  When you're ready, swap to PostgreSQL — only this file changes!

SQL INJECTION — THE #1 WEB SECURITY RISK:
    SQL Injection is when an attacker puts malicious SQL into a form field.

    VULNERABLE (NEVER DO THIS):
        user_input = "1; DROP TABLE expenses; --"
        sql = f"SELECT * FROM expenses WHERE id = {user_input}"
        # ↑ This would DELETE your entire expenses table!

    SAFE (ALWAYS DO THIS):
        sql = "SELECT * FROM expenses WHERE id = ?"
        cursor.execute(sql, (user_input,))
        # ↑ SQLite handles escaping. The ? is a placeholder for the actual value.
        # Even if user_input contains SQL code, it's treated as plain text data.

    PARAMETERIZED QUERIES (using ?) are the standard protection against SQL Injection.
    We use them throughout expense_repository.py.

WHAT IS row_factory?
    By default, SQLite returns rows as tuples: (1, "Coffee", 25000, "Food", ...)
    With row_factory = sqlite3.Row, rows behave like dictionaries:
    row["id"], row["title"], row["amount"] — much more readable!

THE DATABASE SCHEMA (Table Structure):
    CREATE TABLE expenses (
        id          INTEGER PRIMARY KEY AUTOINCREMENT,  ← auto-incrementing unique ID
        title       TEXT NOT NULL,                       ← required field
        amount      REAL NOT NULL,                       ← decimal number
        category    TEXT NOT NULL DEFAULT 'Other',       ← with fallback
        notes       TEXT DEFAULT '',                     ← optional
        created_at  TEXT DEFAULT (datetime('now',...)),  ← set automatically by DB
        updated_at  TEXT DEFAULT (datetime('now',...))   ← updated on each change
    );
"""

import os
import sqlite3

from config import config
from utils.logger import get_logger

logger = get_logger(__name__)

# ── SQL Schema ─────────────────────────────────────────────────────────────────
# "IF NOT EXISTS" makes this safe to run multiple times — it only creates
# the table on the very first run, then does nothing on subsequent runs.
_CREATE_EXPENSES_TABLE = """
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


def get_connection() -> sqlite3.Connection:
    """
    Open and return a new SQLite database connection.

    IMPORTANT: Always use this function to get a connection.
    Never create a sqlite3.connect() call anywhere else in the project.

    WHY?
    - Single place to change database settings (path, timeouts, etc.)
    - Consistent row_factory setup on every connection
    - Easy to add connection pooling later

    HOW TO USE (with context manager):
        with get_connection() as conn:
            cursor = conn.execute("SELECT * FROM expenses")
            rows = cursor.fetchall()
        # Connection is automatically closed after the 'with' block

    Returns:
        sqlite3.Connection: An open, configured database connection

    Raises:
        sqlite3.Error: If the database file cannot be opened
    """
    # Make sure the database directory exists
    # (handles first-time setup when database/ folder is empty)
    db_dir = os.path.dirname(config.DATABASE_PATH)
    if db_dir and not os.path.exists(db_dir):
        os.makedirs(db_dir, exist_ok=True)
        logger.info(f"Created database directory: {db_dir}")

    connection = sqlite3.connect(config.DATABASE_PATH)

    # ── Dictionary-style rows ──────────────────────────────────────────────────
    # Without this: row = (1, "Coffee", 25000.0, "Food", ...)  → row[2] for amount
    # With this:    row = {"id": 1, "title": "Coffee", ...}    → row["amount"]
    connection.row_factory = sqlite3.Row

    # Enable foreign key enforcement (good habit even without foreign keys yet)
    connection.execute("PRAGMA foreign_keys = ON")

    return connection


def init_db() -> None:
    """
    Initialize the database by creating all tables.

    This is called ONCE when the application starts (in app.py).
    The CREATE TABLE IF NOT EXISTS statement means:
    - First time running: creates the expenses table
    - Every time after:  skips silently (no error, no duplicate table)

    So you can restart the app as many times as you like without issues.

    Raises:
        sqlite3.Error: If the database cannot be created (disk full, permissions)
    """
    try:
        with get_connection() as conn:
            conn.execute(_CREATE_EXPENSES_TABLE)
            conn.commit()
        logger.info(f"Database initialized | path={config.DATABASE_PATH}")
    except sqlite3.Error as e:
        # Use critical level — if the DB can't be created, nothing works
        logger.critical(f"Database initialization failed: {e}")
        raise
