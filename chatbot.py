import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    (r"hi|hello|hey", ["Hello!", "Hi there!"]),
    (r"what's up|sup|how are you", [
     "Not much, how about you?", "I'm good, thanks for asking!"]),
    (r"how do you do|nice to meet you", ["Nice to meet you too!"]),

    # Pattern-response pairs for talking about the weather
    (r"what's the weather like today", [
     "I'm sorry, I don't know. Where are you located?"]),
    (r"i'm in (.*)",
     ["Ah, I see. I'm still learning about different locations. Is it usually sunny or rainy there?"]),
    (r"it's usually (sunny|rainy)", ["Interesting! I'll remember that."]),

    (r"tell about python", [
     "Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation via the off-side rule."]),

    # Pattern-response pairs for saying goodbye
    (r"goodbye|bye", ["Goodbye!", "See you later!"]),
]

chatbot = Chat(pairs, reflections)
chatbot.converse()
