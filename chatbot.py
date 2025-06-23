# chatbot.py

def get_response(user_input):
    user_input = user_input.lower()

    if user_input == "hello":
        return "Hi there!"
    elif user_input == "hi":
        return "Hello!"
    elif user_input == "how are you":
        return "I'm fine, thank you!"
    elif user_input == "what is your name":
        return "I'm a simple chatbot created by Ekata."
    elif user_input == "bye":
        return "Goodbye! Have a nice day!"
    else:
        return "Sorry, I don't understand that."

# START of program
print("🤖 Chatbot is ready! (type 'bye' to exit)")

while True:
    user = input("You: ")
    response = get_response(user)
    print("Bot:", response)

    if user.lower() == "bye":
        break

