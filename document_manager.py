from pdf_reader import read_pdf
from document_processor import process_document
from document_db import save_document

def upload_document(pdf_path):
    text = read_pdf(pdf_path)
    data = process_document(text)
    save_document(data, pdf_path)
    return data