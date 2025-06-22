 
from nltk.chat.util import Chat , reflections
pairs=[
    [  r"my name is (.*)",
        ["Hello %1, how can i help you today?"]
    ],
    [
        r"hi|hey|hello",
        ["Hello!", "Hey there!", "Hi! How can I help?"]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created by you! You can call me Chatbot."]
    ],
    [
        r"how are you ?",
        ["I'm doing good, thanks! How about you?"]
    ],
    [
        r"sorry (.*)",
        ["It's okay, no worries."]
    ],
    [
        r"quit",
        ["Bye-bye! Take care."]
    ],
    [
        r"(.*)",
        ["I'm sorry, I don't understand that yet."]
    ]

]

def chatbot():
    print("Hello!, Im your chatbot . Type 'quit' to exit")
    chat= Chat(pairs,reflections)
    chat.converse()

if __name__ =="__main__":
    chatbot()