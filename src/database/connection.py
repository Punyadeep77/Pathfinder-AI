import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATABASE_PATH = BASE_DIR / "data" / "database" / "pathfinder.db"

def get_connection():
    
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def close_connection(conn):
    if conn:
        conn.close()

def execute_query(query, parameters=()):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query, parameters)
    conn.commit()
    close_connection(conn)

def fetch_all(query, parameters=()):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query, parameters)
    rows = cursor.fetchall()
    close_connection(conn)
    return rows

def fetch_one(query, parameters=()):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query, parameters)
    row = cursor.fetchone()
    close_connection(conn)
    return row

def test_connection():
    try:
        conn = get_connection()
        print("Database Connected Successfully")
        close_connection(conn)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    test_connection()