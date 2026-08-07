import sqlite3
from datetime import datetime

DB_NAME = "sanx.db"

def get_connection() -> sqlite3.Connection:
    """
    Returns a SQLite database connection.
    """
    return sqlite3.connect(DB_NAME)


def progress_log(message: str) -> None:
    """
    Prints progress database logs.
    """
    now = datetime.now().strftime("%H:%M:%S")
    print(f"[{now}] [PROGRESS] {message}")


def create_progress_table() -> None:
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS study_progress (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic TEXT,
            status TEXT,
            score INTEGER,
            created_at TEXT
        )
        """)

        conn.commit()
        progress_log("Study progress table ready.")

    except Exception as e:
        progress_log(f"Error: {e}")

    finally:
        conn.close()


def save_progress(
    topic: str,
    status: str,
    score: int
) -> bool:
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO study_progress
        (topic, status, score, created_at)
        VALUES (?, ?, ?, ?)
        """, (
            topic,
            status,
            score,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ))

        conn.commit()
        progress_log(f"Saved progress: {topic}")
        return True

    except Exception as e:
        progress_log(f"Error: {e}")
        return False

    finally:
        conn.close()


def get_progress() -> list:
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT topic, status, score, created_at
        FROM study_progress
        ORDER BY id DESC
        """)

        rows = cursor.fetchall()
        progress_log(f"Loaded {len(rows)} progress record(s).")
        return rows

    except Exception as e:
        progress_log(f"Error: {e}")
        return []

    finally:
        conn.close()

    return rows