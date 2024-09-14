import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from transformers import pipeline

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



classifier = pipeline('sentiment-analysis', 
                      model="nlptown/bert-base-multilingual-uncased-sentiment")

def analyze_spanish(sentence):
    result = classifier(sentence)[0]
    return f"polaridad: {result['label']}, score: {round(result['score'], 4)}"