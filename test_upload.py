import pytest
from pathlib import Path

from document_manager import upload_document


def test_upload_document():
    pdf_path = Path("sample.pdf")

    if not pdf_path.exists():
        pytest.skip("sample.pdf is not available")

    data = upload_document(str(pdf_path))

    assert data is not None