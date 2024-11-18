from flask import Flask, render_template, request

from sentiment_analysis import SentimentAnalyzer

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/analyze', methods=['POST'])
def analyze():
    # Get the user input from the form
    text = request.form['text']

    # Perform sentiment analysis
    analyzer = SentimentAnalyzer(text)
    analyzer.analyze_sentiment()
    sentiment_label, sentiment_score = analyzer.get_sentiment()

    # Return only the result part of the page
    return render_template(
        'result.html',
        sentiment_label=sentiment_label,
        sentiment_score=sentiment_score,
        original_text=text
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8181, debug=True)
