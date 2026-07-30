import sqlite3

DB_NAME = "sanx.db"

def get_all_documents():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT document_type,
           name,
           document_number,
           valid_to,
           file_name
    FROM documents
    """)

    documents = cursor.fetchall()

    conn.close()

    return documents

def get_latest_document():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT document_type,
           name,
           document_number,
           dob,
           valid_from,
           valid_to,
           file_name
    FROM documents
    ORDER BY id DESC
    LIMIT 1
    """)

    document = cursor.fetchone()

    conn.close()

    return document


def save_document(data, file_name):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO documents (
        document_type,
        name,
        document_number,
        dob,
        valid_from,
        valid_to,
        file_name
    ) VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        data.get("document_type"),
        data.get("name"),
        data.get("licence_number"),
        data.get("date_of_birth"),
        data.get("valid_from"),
        data.get("valid_to"),
        file_name
    ))

    conn.commit()
    conn.close()