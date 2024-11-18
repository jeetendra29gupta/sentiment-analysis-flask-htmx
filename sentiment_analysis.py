from textblob import TextBlob


class SentimentAnalyzer:
    def __init__(self, text):
        """Initialize with text to analyze"""
        self.text = text.strip().lower()
        self.sentiment_score = None
        self.sentiment_label = None

    def analyze_sentiment(self):
        """Analyze the sentiment of the provided text"""
        blob = TextBlob(self.text)
        self.sentiment_score = blob.sentiment.polarity
        if self.sentiment_score > 0.6:
            self.sentiment_label = "Very Positive"
        elif self.sentiment_score > 0.2:
            self.sentiment_label = "Positive"
        elif self.sentiment_score == 0:
            self.sentiment_label = "Neutral"
        elif self.sentiment_score > -0.2:
            self.sentiment_label = "Negative"
        else:
            self.sentiment_label = "Very Negative"

    def get_sentiment(self):
        """Return the sentiment label and score"""
        return self.sentiment_label, self.sentiment_score


def main():
    test_texts = [
        "I absolutely love this product! It's amazing.",
        "This is the worst experience I've ever had.",
        "I'm so excited for the weekend!",
        "I can't believe how terrible the service was today.",
        "Everything about this app is perfect!",
        "I don't like how this movie ended.",
        "This restaurant was fantastic! The food was great.",
        "Such a disappointment. I expected much more.",
        "I feel so lucky to have found this.",
        "The weather today is absolutely terrible.",
        "I'm feeling really good today, everything is going well.",
        "I regret buying this. It's a waste of money.",
        "This is a beautiful place, I love it!",
        "I can't stand this show anymore. It's so boring.",
        "I'm so proud of my team for their hard work.",
        "Not happy with the results. Could have been better.",
        "I don't think I can handle this anymore.",
        "The concert was amazing! I had a blast.",
        "It's a very average product, nothing special.",
        "I'm so tired of these issues popping up all the time."
    ]
    for test_text in test_texts:
        analyzer = SentimentAnalyzer(test_text)
        analyzer.analyze_sentiment()
        sentiment_label, sentiment_score = analyzer.get_sentiment()

        print(f"Text: {test_text}")
        print(f"Sentiment: {sentiment_label}")
        print(f"Sentiment Score: {sentiment_score:.2f}")

        print(40 * '#')


if __name__ == '__main__':
    main()
