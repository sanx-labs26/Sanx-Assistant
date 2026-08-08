from database import (
    create_conversation_table,
    save_conversation,
    get_recent_conversations,
)


def test_conversation_memory():
    create_conversation_table()

    save_conversation(
        "Hello",
        "Hello, Sanx. How may I assist you today?"
    )

    conversations = get_recent_conversations()

    assert conversations is not None