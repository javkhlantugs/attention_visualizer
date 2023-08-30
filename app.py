from flask import Flask, render_template, request
from mask import *


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        sentence = request.form['sentence']  # Get user input
        # Process sentence using BERT and generate attention diagrams
        generated_sentences = generate(sentence)
        return render_template('index.html', sentence=sentence, generated_sentences=generated_sentences, attention_diagrams=None)
    return render_template('index.html', sentence=None, generated_sentences=None, attention_diagrams=None)

if __name__ == '__main__':
    app.run(debug=True)
