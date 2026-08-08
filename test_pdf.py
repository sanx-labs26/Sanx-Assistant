import pytest
from pathlib import Path

from pdf_reader import read_pdf


def test_read_pdf():
    pdf_path = Path("sample.pdf")

    if not pdf_path.exists():
        pytest.skip("sample.pdf is not available")

    text = read_pdf(str(pdf_path))

    assert text is not None
    assert isinstance(text, str)