import random

def chatbot_response(user_input):
    user_input = user_input.lower()

    greetings = ["hi", "hello", "hey"]
    jokes = [
        "Why don't programmers like nature? Too many bugs 😂",
        "Why did the computer go to the doctor? Because it caught a virus 🤒",
        "Why was the math book sad? Because it had too many problems 😄"
    ]

    if any(word in user_input for word in greetings):
        return "Hello! 😊 How can I help you today?"

    elif "how are you" in user_input:
        return "I'm doing great! Thanks for asking 😄"

    elif "your name" in user_input:
        return "I'm Kuttu 🤖, your friendly chatbot!"

    elif "joke" in user_input:
        return random.choice(jokes)

    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! 👋 Have a great day!"

    else:
        return "Sorry, I didn't understand that 🤔. Try asking something else!"