from textblob import TextBlob

name = input("\nName: ")

while True:
    s = input("Sentence (or 'exit'): ")
    if s.lower() == 'exit':
    print("Bye!", name)
    break
    p = TextBlob(s).sentiment.polarity
    if p > 0:
    print("\U0001F642",p)
    elif p < 0:
    print("\U0001F641",p)
    else:
    print("\U0001F610",p)