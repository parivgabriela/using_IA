import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from constants import green_circle, blue_circle, yellow_circle 
nltk.download('vader_lexicon')

sia = SentimentIntensityAnalyzer()

def analyze_sentiment(sentence):
    sentiment = sia.polarity_scores(sentence)
    return sentiment

# Example sentence
# "I love this product! It works great and is very affordable."
sentence = input("Enter a sentence: ")
result = analyze_sentiment(sentence)

print(f"Sentiment analysis for the sentence: '{sentence}'")
print(result)

if result['neg'] > 0.5:
    print(f"Negative {blue_circle}")
elif result['neu'] >= 0.5:
    print(f"Neutral {yellow_circle}")
elif result['pos'] > 0.5:
    print(f"Positive {green_circle}")

