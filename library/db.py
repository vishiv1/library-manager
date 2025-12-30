import sqlite3
from pathlib import Path

try:
    import settings
except ImportError:
    import settings_example as settings

def get_conn():
    Path("data").mkdir(exist_ok=True)
    return sqlite3.connect(settings.DB_PATH)

def init_db():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS authors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author_id INTEGER,
        available INTEGER
    )
    """)

    conn.commit()
    conn.close()
