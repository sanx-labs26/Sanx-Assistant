import sqlite3


def test_database_tables():
    conn = sqlite3.connect("sanx.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT name FROM sqlite_master WHERE type='table';"
    )

    tables = cursor.fetchall()

    conn.close()

    assert tables is not None