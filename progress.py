import sqlite3
from datetime import datetime

DB_NAME = "sanx.db"


def create_progress_table():
    conn = sqlite3.connect(DB_NAME)
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
    conn.close()


def save_progress(topic, status, score):
    conn = sqlite3.connect(DB_NAME)
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
    conn.close()


def get_progress():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT topic, status, score, created_at
    FROM study_progress
    ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows