import datetime

print("ChatBot Started (type 'exit' to quit)")

while True:
    user = input("You: ").lower()

    if user == "exit":
        print("Bot: Goodbye!")
        break

    elif "hello" in user or "hi" in user:
        print("Bot: Hello! How can I help?")

    elif "name" in user:
        print("Bot: I am a Python chatbot.")

    elif "time" in user:
        now = datetime.datetime.now()
        print("Bot:", now)

    else:
        print("Bot: I didn't understand that.")