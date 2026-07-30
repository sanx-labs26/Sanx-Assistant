from chat_engine import chat

while True:
    user = input("You: ")

    if user.lower() == "exit":
        break

    reply = chat(user)
    print("SanX:",reply)
    