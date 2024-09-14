# Sentiment analysis

This app can analize the sentiment of a sentence and then give the results.

It works with spanish and english. 
The user can choose the language in the index.
I use the library 'SentimentIntensityAnalyzer' from NLTK and pipeline from transformers

The results in 'SentimentIntensityAnalyzer' return a dict with the following values:
'neg': 0.0, 'neu': 0.192, 'pos': 0.808, 'compound': 0.6369

Pipeline give these result 
polaridad: 4 stars, score: 0.4546 

5 stars is the highest value, means it's positive
