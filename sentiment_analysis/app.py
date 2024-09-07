from flask import Flask, render_template, request
from sentiment_analysis import analysis_sentence
from constants import languages, user_message


app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', languages=languages)

@app.route('/sentiment_analysis', methods=['POST'])
def sentiment():
    language = request.form['languages']

    return render_template('sentiment.html', user_input=user_message[language])


@app.route('/sentiment_analysis', methods=['POST'])
def sentiment_analysis():
    text = request.form['user_text']
    result = analysis_sentence(text)
    return render_template('result.html', text=text, result=result)


if __name__ == "__main__":
    app.run(debug=True)
