from sentiment_analysis import analysis_sentence

def main():
    sentence = input("Enter a sentence: ")

    print(f"Sentiment analysis for the sentence: '{sentence}'")
    result = analysis_sentence(sentence)
    print(result)

if __name__ == '__main__':
    main()

