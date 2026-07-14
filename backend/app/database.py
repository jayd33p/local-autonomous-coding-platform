"""Database initialization (SQLite) using SQLAlchemy or simple sqlite3.
This is a lightweight placeholder for future models and persistence.
"""
import os
from pathlib import Path
import sqlite3

DB_PATH = Path(__file__).resolve().parents[1] / "data" / "app.db"

def ensure_db():
    DB_PATH.parent.mkdir(exist_ok=True)
    if not DB_PATH.exists():
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        # basic tables
        c.execute('''CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, description TEXT, status TEXT)''')
        conn.commit()
        conn.close()

if __name__ == '__main__':
    ensure_db()
