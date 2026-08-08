import pytest
from pathlib import Path

from pdf_reader import read_pdf
from document_processor import process_document


def test_document_processing():
    pdf_path = Path("sample.pdf")

    if not pdf_path.exists():
        pytest.skip("sample.pdf is not available")

    text = read_pdf(str(pdf_path))
    data = process_document(text)

    assert data is not None