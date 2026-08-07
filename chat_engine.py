from document_manager import upload_document
from document_db import get_all_documents,get_latest_document
from database import save_conversation,get_recent_conversations


def chat(user_input):
    original_input = user_input
    user_input = user_input.lower().strip()

    # Greetings
    if user_input in ["hi", "hello", "hey"]:
        response = "Hello! I am SanX. How can I help you?"
        save_conversation(original_input, response)
        return response

    # Document upload
    if user_input.startswith("upload "):
        pdf_path = original_input.replace("upload ", "").strip()

        try:
            data = upload_document(pdf_path)
            response = f"Document uploaded successfully!\n\n{data}"
        except Exception as e:
            response = f"Error uploading document: {e}"

        save_conversation(original_input, response)
        return response

    # Show documents
    if "show documents" in user_input:
        docs = get_all_documents()

        if not docs:
            response = "No documents found."
            save_conversation(original_input, response)
            return response

        result = "Your Documents:\n\n"

        for doc in docs:
            result += (
                f"Type: {doc[0]}\n"
                f"Name: {doc[1]}\n"
                f"Number: {doc[2]}\n"
                f"Valid Until: {doc[3]}\n"
                f"File: {doc[4]}\n"
                "-------------------------\n"
            )

        save_conversation(original_input, result)
        return result

    doc = get_latest_document()

    if "licence number" in user_input or "license number" in user_input:
        if doc:
            response = f"Your licence number is {doc[2]}"
        else:
            response = "No licence found."

        save_conversation(original_input, response)
        return response

    if "date of birth" in user_input or "dob" in user_input:
        if doc:
            response = f"Your date of birth is {doc[3]}"
        else:
            response = "No document found."

        save_conversation(original_input, response)
        return response

    if "expire" in user_input or "valid until" in user_input:
        if doc:
            response = f"Your learner's licence is valid until {doc[5]}"
        else:
            response = "No document found."

        save_conversation(original_input, response)
        return response

    if "my name" in user_input:
        if doc:
            response = f"Your name is {doc[1]}"
        else:
            response = "No document found."

        save_conversation(original_input, response)
        return response

    # Show conversation history
    if "show conversation" in user_input or "conversation history" in user_input:
        conversations = get_recent_conversations()

        if not conversations:
            response = "No conversation history found."
            save_conversation(original_input, response)
            return response

        response = "Recent Conversations:\n\n"

        for convo in conversations:
            response += (
                f"You: {convo[0]}\n"
                f"SanX: {convo[1]}\n"
                f"Time: {convo[2]}\n"
                "-------------------------\n"
            )

        save_conversation(original_input, response)
        return response
    

    # Help
    if "help" in user_input:
        response = (
            "Available commands:\n"
            "- Hello\n"
            "- Upload sample.pdf\n"
            "- Show documents\n"
            "- Show conversation\n"
            "- Help"
        )

        save_conversation(original_input, response)
        return response
    

    response = "Sorry, I didn't understand that."
    save_conversation(original_input, response)
    return response