from database import get_recent_conversations

history = get_recent_conversations()

for user, assistant, time in history:
    print(f"User: {user}")
    print(f"Sanx: {assistant}")
    print(f"Time: {time}")
    print("-" * 30)