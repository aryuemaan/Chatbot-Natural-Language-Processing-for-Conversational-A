import nltk
from nltk.chat.util import Chat, reflections
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree
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
chatbot = Chat(pairs, reflections)

sid = SentimentIntensityAnalyzer()
def extract_entities(text):
    entities = []
    for sent in nltk.sent_tokenize(text):
        for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
            if isinstance(chunk, Tree):
                entities.append(" ".join([token for token, pos in chunk.leaves()]))
    return entities
print("Hello, I'm Chatbot! How can I assist you today?")
while True:
    user_input = input("> ")
    if user_input.lower() == "quit":
        break
    sentiment_score = sid.polarity_scores(user_input)["compound"]
    sentiment = "positive" if sentiment_score >= 0 else "negative"
    entities = extract_entities(user_input)

    response = chatbot.respond(user_input)
    if "%NE%" in response:
        response = response.replace("%NE%", ", ".join(entities))
    if "%SENTIMENT%" in response:
        response = response.replace("%SENTIMENT%", sentiment)
    
    print(response)
