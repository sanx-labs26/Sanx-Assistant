import fitz
import pytesseract
from PIL import Image
import io

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def read_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""

    for page in doc:
        page_text = page.get_text()

        # If text exists, use it
        if page_text.strip():
            text += page_text
        else:
            # OCR for scanned page
            pix = page.get_pixmap(dpi=300)
            img = Image.open(io.BytesIO(pix.tobytes("png")))
            text += pytesseract.image_to_string(img)

    return text