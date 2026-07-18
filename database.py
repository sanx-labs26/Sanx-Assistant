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


def create_preferences_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS preferences (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        voice TEXT
    )
    """)

    conn.commit()
    conn.close()

def init_db():
    create_conversation_table()
    create_preferences_table()

def save_preferences(username, voice):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO preferences (username, voice)
    VALUES (?, ?)
    """, (username, voice))

    conn.commit()
    conn.close()


def get_preferences():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT username, voice
    FROM preferences
    """)

    result = cursor.fetchall()

    conn.close()
    return result


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