"""
config.py - Application Configuration
======================================

WHY THIS FILE EXISTS:
    Every application has settings: database path, debug mode, log level, etc.
    Instead of scattering these values throughout the code, we centralize
    them here and read them from a .env file.

INDUSTRY PRACTICE:
    Real companies NEVER hardcode configuration values in source code because:
    1. Security: Secrets (passwords, API keys) should never be in git
    2. Flexibility: Dev uses SQLite, Production uses PostgreSQL
    3. Portability: Different developers, different machines, same code

HOW IT WORKS:
    1. You create a .env file with your settings (never commit this!)
    2. python-dotenv reads the .env file
    3. os.getenv() fetches each value with a sensible default
    4. The Config class holds everything in one place

EXAMPLE .env:
    APP_NAME=RainCode Expense Tracker
    APP_ENV=development
    APP_DEBUG=True
    DATABASE_PATH=database/expense_tracker.db
    LOG_LEVEL=INFO
"""

import os
from dotenv import load_dotenv

# Load .env file BEFORE accessing any os.getenv() calls
# This must happen at the top of the file
load_dotenv()


class Config:
    """
    Central configuration for the application.

    All settings are read from environment variables (.env file).
    Default values are provided as fallbacks for development.

    Usage:
        from config import config
        print(config.APP_NAME)
        print(config.DATABASE_PATH)
    """

    # ── Application ────────────────────────────────────────────────────────────
    APP_NAME: str = os.getenv("APP_NAME", "RainCode Expense Tracker")
    APP_ENV: str = os.getenv("APP_ENV", "development")

    # "True" string from .env → convert to actual Python bool
    DEBUG: bool = os.getenv("APP_DEBUG", "True").lower() == "true"

    # Secret key for Flask sessions and flash messages
    # In production: use a long random string, never share it
    SECRET_KEY: str = os.getenv(
        "SECRET_KEY", "raincode-dev-secret-change-this-in-production-123!"
    )

    # ── Database ───────────────────────────────────────────────────────────────
    # Path to the SQLite database file
    # SQLite stores the entire database in a single file — great for learning!
    DATABASE_PATH: str = os.getenv("DATABASE_PATH", "database/expense_tracker.db")

    # ── Logging ────────────────────────────────────────────────────────────────
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    LOG_FILE: str = os.getenv("LOG_FILE", "logs/app.log")

    # ── Pagination ─────────────────────────────────────────────────────────────
    # How many expenses to show per page (future feature)
    EXPENSES_PER_PAGE: int = int(os.getenv("EXPENSES_PER_PAGE", "10"))

    # ── Dashboard ──────────────────────────────────────────────────────────────
    # How many recent transactions to show on dashboard
    RECENT_EXPENSES_LIMIT: int = int(os.getenv("RECENT_EXPENSES_LIMIT", "5"))


# ── Single instance ────────────────────────────────────────────────────────────
# Create ONE instance to import everywhere.
# This way all modules share the same configuration object.
#
# Usage across the project:
#   from config import config
#   path = config.DATABASE_PATH
config = Config()
