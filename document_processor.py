import re

def process_document(text):
    data = {}

    # Document Type
    if "LEARNER'S LICENCE" in text.upper():
        data["document_type"] = "Learner's Licence"

    # Name
    name = re.search(r"Name\s+([A-Z ]+)", text)
    if name:
        data["name"] = name.group(1).strip()

    # Licence Number
    licence = re.search(r"Licence No\.\s*([A-Z0-9/ ]+)", text)
    if licence:
        data["licence_number"] = licence.group(1).strip()

    # Date of Birth
    dob = re.search(r"Date of Birth\s*([0-9\-]+)", text)
    if dob:
        data["date_of_birth"] = dob.group(1)

    # Blood Group
    blood = re.search(r"Factor\s*([A-Z0-9+]+)", text)
    if blood:
        data["blood_group"] = blood.group(1)

    # Validity
    validity = re.search(
        r"valid from date\s*([0-9/]+)\s*To\s*([0-9/]+)",
        text,
        re.IGNORECASE,
    )
    if validity:
        data["valid_from"] = validity.group(1)
        data["valid_to"] = validity.group(2)

    return data