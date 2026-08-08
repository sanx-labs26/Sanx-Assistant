import pytest
from pathlib import Path

from database import init_db
from pdf_reader import read_pdf
from document_processor import process_document
from document_db import save_document


def test_save_document():
    pdf_path = Path("sample.pdf")

    if not pdf_path.exists():
        pytest.skip("sample.pdf is not available")

    # Initialize database
    init_db()

    # Read PDF
    text = read_pdf(str(pdf_path))

    # Process document
    data = process_document(text)

    # Save document
    result = save_document(data, str(pdf_path))

    # Verify the operation completed
    assert result is not False