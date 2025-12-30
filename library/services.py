from .db import get_conn

def add_author(name):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("INSERT INTO authors(name) VALUES (?)", (name,))
    conn.commit()
    conn.close()

def add_book(title, author_id):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO books(title, author_id, available) VALUES (?, ?, 1)",
        (title, author_id)
    )
    conn.commit()
    conn.close()

def list_books():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        SELECT b.id, b.title, a.name, b.available
        FROM books b JOIN authors a ON b.author_id = a.id
    """)
    rows = cur.fetchall()
    conn.close()
    return rows

def borrow(book_id):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("UPDATE books SET available=0 WHERE id=?", (book_id,))
    conn.commit()
    conn.close()
