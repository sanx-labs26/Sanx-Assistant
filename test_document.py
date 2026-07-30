from pdf_reader import read_pdf
from document_processor import process_document

text = read_pdf("sample.pdf")

data = process_document(text)

print(data)