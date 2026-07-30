import sqlite3
from datetime import datetime

DB_NAME = "sanx.db"

def init_db():
    create_conversation_table()
    create_preferences_table()
    create_documents_table()
    create_tasks_table()
    

def create_conversation_table():
    try:
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

    except Exception as e:
        print(f"Database Error: {e}")

    finally:
        conn.close()


def create_preferences_table():
    try:
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

    except Exception as e:
        print(f"Database Error: {e}")

    finally:
        conn.close()

# ==========================
# TASK MANAGER DATABASE
# ==========================

def create_tasks_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        due_date TEXT,
        due_time TEXT,
        status TEXT DEFAULT 'Pending',
        created_at TEXT
    )
    """)

    conn.commit()
    conn.close()


def add_task(title, description="", due_date="", due_time=""):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO tasks
    (title, description, due_date, due_time, created_at)
    VALUES (?, ?, ?, ?, ?)
    """, (
        title,
        description,
        due_date,
        due_time,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    conn.commit()
    conn.close()


def get_tasks():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM tasks
    ORDER BY id DESC
    """)

    tasks = cursor.fetchall()

    conn.close()
    return tasks


def complete_task(task_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE tasks
    SET status = 'Completed'
    WHERE id = ?
    """, (task_id,))

    conn.commit()
    conn.close()


def delete_task(task_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    DELETE FROM tasks
    WHERE id = ?
    """, (task_id,))

    conn.commit()
    conn.close()

def create_documents_table():
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS documents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            document_type TEXT,
            name TEXT,
            document_number TEXT,
            dob TEXT,
            valid_from TEXT,
            valid_to TEXT,
            file_name TEXT
        )
        """)

        conn.commit()

    except Exception as e:
        print(f"Database Error: {e}")

    finally:
        conn.close()        


def save_preferences(username, voice):
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO preferences (username, voice)
        VALUES (?, ?)
        """, (username, voice))

        conn.commit()

    except Exception as e:
        print(f"Database Error: {e}")

    finally:
        conn.close()


def get_preferences():
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute("""
        SELECT username, voice
        FROM preferences
        """)

        result = cursor.fetchall()
        return result

    except Exception as e:
        print(f"Database Error: {e}")
        return []

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

        data = cursor.fetchall()
        return data

    except Exception as e:
        print(f"Database Error: {e}")
        return []

    finally:
        conn.close()