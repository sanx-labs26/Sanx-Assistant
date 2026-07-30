from database import init_db
from pdf_reader import read_pdf
from document_processor import process_document
from document_db import save_document

# Initialize database
init_db()

# Read PDF
text = read_pdf("sample.pdf")

# Extract fields
data = process_document(text)

# Save to database
save_document(data, "sample.pdf")

print("Document saved successfully!")