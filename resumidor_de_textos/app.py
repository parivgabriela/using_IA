from flask import Flask, render_template, request
from resumidor import resumir_texto

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/resumidor', methods=['POST'])
def resumidor():
    texto = request.form['inputText']
    nuevo_texto = resumir_texto(texto)
    return render_template('index.html', nuevo_texto = nuevo_texto )


if __name__ == '__main__':  
   app.run()
