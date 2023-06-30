import nltk
from nltk.chat.util import Chat, reflections

# Define the chatbot's responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there"]
    ],
    [
        r"what is your name?",
        ["You can call me Chatbot.",]
    ],
    [
        r"how are you ?",
        ["I'm doing good. How about you?",]
    ],
    [
        r"sorry (.*)",
        ["No problem", "Apologies accepted"]
    ],
    [
        r"quit",
        ["Bye-bye. Take care!"]
    ],
]

# Create a Chatbot instance
chatbot = Chat(pairs, reflections)

# Start the conversation loop
print("Hello, I'm Chatbot! How can I assist you today?")
while True:
    user_input = input("> ")
    if user_input.lower() == "quit":
        break
    print(chatbot.respond(user_input))
