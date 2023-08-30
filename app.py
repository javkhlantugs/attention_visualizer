from flask import Flask, render_template, request
from mask import *
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        sentence = request.form['sentence']  # Get user input
        # Process sentence using BERT and generate attention diagrams
        generated_sentences = generate(sentence)
        predicted_words = generated_sentences[0]
        return render_template('index.html', sentence=sentence, predicted_word=predicted_words, attention_diagrams=None)
    return render_template('index.html', sentence=None, predicted_word=None, attention_diagrams=None)

if __name__ == '__main__':
    app.run(debug=True)
