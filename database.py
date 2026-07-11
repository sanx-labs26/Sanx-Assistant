import sqlite3

DB_NAME = "sanx.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS preferences (
        id INTEGER PRIMARY KEY,
        username TEXT,
        voice TEXT
    )
    """)

    conn.commit()
    conn.close()

def save_preferences(username, voice):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT OR REPLACE INTO preferences
    (id, username, voice)
    VALUES (1, ?, ?)
    """, (username, voice))

    conn.commit()
    conn.close()

def get_preferences():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT username, voice FROM preferences WHERE id = 1"
    )

    result = cursor.fetchone()

    conn.close()

    return result

def create_conversation_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS conversations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_message TEXT,
        assistant_response TEXT
    )
    """)

    conn.commit()
    conn.close()

    import sqlite3
from datetime import datetime

DB_NAME = "sanx.db"

def create_conversation_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS conversations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_message TEXT,
        assistant_response TEXT,
        created_at TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_conversation(user_message, assistant_response):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO conversations
    (user_message, assistant_response, created_at)
    VALUES (?, ?, ?)
    """, (
        user_message,
        assistant_response,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    conn.commit()
    conn.close()


def get_recent_conversations(limit=10):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT user_message,
           assistant_response,
           created_at
    FROM conversations
    ORDER BY id DESC
    LIMIT ?
    """, (limit,))

    data = cursor.fetchall()

    conn.close()

    return data

def get_preferences():
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute("""
        SELECT username, voice
        FROM preferences
        WHERE id = 1
        """)

        result = cursor.fetchone()
        return result

    except Exception as e:
        print(f"Database Error: {e}")
        return None

    finally:
        conn.close()

def save_preferences(username, voice):
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute("""
        INSERT OR REPLACE INTO preferences
        (id, username, voice)
        VALUES (1, ?, ?)
        """, (username, voice))

        conn.commit()

    except Exception as e:
        print(f"Database Error: {e}")

    finally:
        conn.close()

def save_conversation(user_message, assistant_response):
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO conversations
        (user_message, assistant_response, created_at)
        VALUES (?, ?, ?)
        """, (
            user_message,
            assistant_response,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ))

        conn.commit()

    except Exception as e:
        print(f"Database Error: {e}")

    finally:
        conn.close()

def get_recent_conversations(limit=10):
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute("""
        SELECT user_message,
               assistant_response,
               created_at
        FROM conversations
        ORDER BY id DESC
        LIMIT ?
        """, (limit,))

        return cursor.fetchall()

    except Exception as e:
        print("Database Error: e")
        return []

    finally:
        conn.close()
