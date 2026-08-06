import sqlite3

from config.logging_config import get_logger
from config.settings import DATABASE_PATH

from src.exceptions.database_exceptions import (
    DatabaseConnectionError,
)

logger = get_logger(__name__)

def get_connection():
    """
    Returns a SQLite database connection.
    """
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        conn.row_factory = sqlite3.Row

        logger.info("Database connection established.")

        return conn

    except sqlite3.Error as e:
        logger.exception("Failed to connect to the database.")
        raise DatabaseConnectionError(str(e)) from e

def close_connection(conn):
    """
    Safely closes the database connection.
    """
    if conn:
        conn.close()
        logger.info("Database connection closed.")


def execute_query(query, parameters=()):
    conn = get_connection()

    try:
        cursor = conn.cursor()
        cursor.execute(query, parameters)
        conn.commit()

    except sqlite3.Error as e:
        logger.exception("Failed to execute database query.")
        raise DatabaseConnectionError(str(e)) from e

    finally:
        close_connection(conn)


def fetch_all(query, parameters=()):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(query, parameters)
        rows = cursor.fetchall()
        return rows

    except sqlite3.Error as e:
        logger.exception("Failed to fetch records.")
        raise DatabaseConnectionError(str(e)) from e

    finally:
        close_connection(conn)

def fetch_one(query, parameters=()):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(query, parameters)
        row = cursor.fetchone()
        return row

    except sqlite3.Error as e:
        logger.exception("Failed to fetch record.")
        raise DatabaseConnectionError(str(e)) from e

    finally:
        close_connection(conn)

def test_connection():
    conn = get_connection()
    logger.info("Database connected successfully.")
    close_connection(conn)

if __name__ == "__main__":
    test_connection()