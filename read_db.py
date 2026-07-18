from database import get_recent_conversations

rows = get_recent_conversations()

for row in rows:
    print(f"User: {row[0]}")
    print(f"Assistant: {row[1]}")
    print(f"Time: {row[2]}")
    print("-" * 40)