import openai

# Set up OpenAI API credentials
openai.api_key = "YOUR_API_KEY"

# Define a function to generate chatbot responses
def generate_response(user_input):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_input,
        max_tokens=50,
        temperature=0.7,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

# Start the conversation
print("Hello, I'm Chatbot! How can I assist you today?")

while True:
    user_input = input("> ")

    if user_input.lower() == "quit":
        break

    # Generate chatbot response
    chatbot_response = generate_response(user_input)
    print(chatbot_response)
