import sqlite3
from datetime import datetime

DB_NAME = "sanx.db"


def create_knowledge_table():
    conn = sqlite3.connect(DB_NAME)
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
    conn.close()


def save_knowledge(topic, content):
    conn = sqlite3.connect(DB_NAME)
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
    conn.close()


def search_knowledge(keyword):
    conn = sqlite3.connect(DB_NAME)
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

    conn.close()

    return rows