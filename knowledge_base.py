import sqlite3
from datetime import datetime

DB_NAME = "sanx.db"

def get_connection() -> sqlite3.Connection:
    """
    Returns a SQLite database connection.
    """
    return sqlite3.connect(DB_NAME)


def knowledge_log(message: str) -> None:
    """
    Prints knowledge base logs.
    """
    now = datetime.now().strftime("%H:%M:%S")
    print(f"[{now}] [KNOWLEDGE] {message}")


def create_knowledge_table() -> None:
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS knowledge (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic TEXT,
            content TEXT,
            created_at TEXT
        )
        """)

        conn.commit()
        knowledge_log("Knowledge table ready.")

    except Exception as e:
        knowledge_log(f"Error: {e}")

    finally:
        conn.close()


def save_knowledge(topic: str, content: str) -> bool:
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO knowledge (topic, content, created_at)
        VALUES (?, ?, ?)
        """, (
            topic,
            content,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ))

        conn.commit()
        knowledge_log(f"Saved topic: {topic}")
        return True

    except Exception as e:
        knowledge_log(f"Error: {e}")
        return False

    finally:
        conn.close()


def search_knowledge(keyword: str) -> list:
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT topic, content
        FROM knowledge
        WHERE topic LIKE ? OR content LIKE ?
        """, (
            f"%{keyword}%",
            f"%{keyword}%"
        ))

        rows = cursor.fetchall()
        knowledge_log(f"Search: {keyword} ({len(rows)} result(s))")
        return rows

    except Exception as e:
        knowledge_log(f"Error: {e}")
        return []

    finally:
        conn.close()

    return rows