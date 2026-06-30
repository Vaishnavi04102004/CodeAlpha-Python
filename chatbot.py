from datetime import datetime

print("=" * 45)
print("        BASIC CHATBOT")
print("=" * 45)
print("Type 'bye' to exit.\n")

while True:
    message = input("You: ").strip().lower()

    if message == "hello" or message == "hi":
        print("Bot: Hello! How can I help you?")

    elif message == "how are you":
        print("Bot: I am doing well. Thanks for asking!")

    elif message == "what is your name":
        print("Bot: I am a Python Chatbot.")

    elif message == "who created you":
        print("Bot: I was created using Python.")

    elif message == "help":
        print("Bot: You can ask me about my name, date, time or say hello.")

    elif message == "date":
        print("Bot:", datetime.now().strftime("%d-%m-%Y"))

    elif message == "time":
        print("Bot:", datetime.now().strftime("%I:%M:%S %p"))

    elif message == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand that.")