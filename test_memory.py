from database import create_conversation_table

create_conversation_table()

print("Conversation table created!")

from database import (
    create_conversation_table,
    save_conversation,
    get_recent_conversations
)

create_conversation_table()

save_conversation(
    "Hello",
    "Hello, Sanx. How may I assist you today?"
)

for row in get_recent_conversations():
    print(row)