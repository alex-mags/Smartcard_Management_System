import sqlite3
import os

DB_PATH = "database/cards.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

def initialise_db():
    os.makedirs("database", exist_ok=True)
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cards (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            card_number TEXT UNIQUE NOT NULL,
            holder_name TEXT NOT NULL,
            card_type TEXT NOT NULL,
            balance REAL DEFAULT 0.0,
            status TEXT DEFAULT 'active',
            issue_date TEXT,
            expiry_date TEXT
        )
    """)
    conn.commit()
    conn.close()
    print("Database initialised successfully.")

if __name__ == "__main__":
    initialise_db()