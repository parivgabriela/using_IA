import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from constants import green_circle, blue_circle, yellow_circle 
nltk.download('vader_lexicon')

sia = SentimentIntensityAnalyzer()

def analyze_sentiment(sentence):
    sentiment = sia.polarity_scores(sentence)
    return sentiment

def analysis_sentence(sentence):
    result = analyze_sentiment(sentence)
    print(result)
    if result['neg'] > 0.5:
        return f"Negative {blue_circle}"
    elif result['neu'] >= 0.5:
        return f"Neutral {yellow_circle}"
    elif result['pos'] > 0.5:
        return f"Positive {green_circle}"

