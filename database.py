import sqlite3
from datetime import datetime

DB_NAME = "sanx.db"

def get_connection() -> sqlite3.Connection:
    """
    Creates and returns a SQLite database connection.
    """
    return sqlite3.connect(DB_NAME)

def db_log(message: str) -> None:
    """
    Prints a timestamped database message.
    """
    now = datetime.now().strftime("%H:%M:%S")
    print(f"[{now}] [DATABASE] {message}")


def init_db():
    create_conversation_table()
    create_preferences_table()
    create_documents_table()
    create_tasks_table()
    

def create_conversation_table():
    try:
        conn = get_connection()
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
        db_log(f"Error: {e}")

    finally:
        conn.close()


def create_preferences_table():
    try:
        conn = get_connection()
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
        db_log(f"Error: {e}")

    finally:
        conn.close()

# ==========================
# TASK MANAGER DATABASE
# ==========================

def create_tasks_table():
    try:
        conn = get_connection()
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

    except Exception as e:
        db_log(f"Error: {e}")
    
    finally:
        conn.close()


def add_task(
    title: str,
    description: str = "",
    due_date: str = "",
    due_time: str = ""
) -> bool:

    try:
        conn = get_connection()
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
        db_log(f"Task added: {title}")
        return True

    except Exception as e:
        db_log(f"Error: {e}")
        return False

    finally:
        conn.close()


def get_tasks():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT * FROM tasks
            ORDER BY id DESC
            """)

        tasks = cursor.fetchall()

    except Exception as e:
        db_log(f"Error: {e}")
        
    finally:
        conn.close()
    return tasks


def complete_task(task_id: int) -> bool:
    """
    Marks a task as completed.
    """
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        UPDATE tasks
        SET status = 'Completed'
        WHERE id = ?
        """, (task_id,))

        conn.commit()
        db_log(f"Task completed: {task_id}")
        return True

    except Exception as e:
        db_log(f"Error completing task: {e}")
        return False

    finally:
        conn.close()


def delete_task(task_id: int) -> bool:
    """
    Deletes a task from the database.
    """
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        DELETE FROM tasks
        WHERE id = ?
        """, (task_id,))

        conn.commit()
        db_log(f"Task deleted: {task_id}")
        return True

    except Exception as e:
        db_log(f"Error deleting task: {e}")
        return False

    finally:
        conn.close()


def create_documents_table():
    try:
        conn = get_connection()
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
        db_log(f"Error: {e}")

    finally:
        conn.close()        


def save_preferences(username: str, voice: str) -> bool:
    """
    Saves or updates the user's preferences.
    """
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT id FROM preferences LIMIT 1")
        existing = cursor.fetchone()

        if existing:
            cursor.execute("""
            UPDATE preferences
            SET username = ?, voice = ?
            WHERE id = ?
            """, (username, voice, existing[0]))
        else:
            cursor.execute("""
            INSERT INTO preferences (username, voice)
            VALUES (?, ?)
            """, (username, voice))

        conn.commit()
        db_log("Preferences saved.")
        return True

    except Exception as e:
        db_log(f"Error saving preferences: {e}")
        return False

    finally:
        conn.close()


def get_preferences():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT username, voice
        FROM preferences
        OERDER BY id DESC
        LIMIT 1
        """)

        result = cursor.fetchall()
        return result

    except Exception as e:
        db_log(f"Error: {e}")
        return []

    finally:
        conn.close()


def save_conversation(
    user_message: str,
    assistant_response: str
) -> bool:
    """
    Saves a conversation between the user and SanX Assistant.
    """
    try:
        conn = get_connection()
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
        db_log("Conversation saved.")
        return True

    except Exception as e:
        db_log(f"Error saving conversation: {e}")
        return False

    finally:
        conn.close()


def get_recent_conversations(limit=10):
    try:
        conn = get_connection()
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
        db_log(f"Error: {e}")
        return []

    finally:
        conn.close()