from flask import Flask, request, jsonify, redirect, url_for, render_template, session
import os
import uuid
from mask import *

app = Flask(__name__)
app.secret_key = os.urandom(24).hex()  # Set your secret key for session management

# Check and print the FLASK_ENV value
flask_env = os.environ.get('FLASK_ENV')
if flask_env is not None:
    print(f'FLASK_ENV is set to: {flask_env}')

@app.before_request
def before_request():
    if 'new_session_id' not in session:
        session['new_session_id'] = str(uuid.uuid4())

@app.route('/', methods=['GET'])
def index_get():
    return render_template('index.html', sentence=None, generated_sentences=None, attention_diagrams=None)

@app.route('/api', methods=['POST'])
def generate_sentence():
    # Receive the JSON data from the request
    data = request.get_json()

    # Access the updated sentence from the JSON data
    updated_sentence = data.get('updatedSentence')
    session['updated_sentence'] = updated_sentence
    # Process the updated sentence as needed
    # For example, you can save it to a session variable or do any other processing

    # Redirect to the '/result' route without query parameters
    return redirect(url_for('result'))

@app.route('/result')
def result():
    # Process the sentence as needed
    # For example, you can retrieve the sentence from the session variable
    sentence = session['updated_sentence']

    session['img_path'] = os.path.join("static", "img", session['new_session_id'])
    if not os.path.exists(session['img_path']):
        os.makedirs(session['img_path'])
    generated_sentences = generate(sentence, session['new_session_id'])
    return render_template('result.html', sentence=sentence, generated_sentences=generated_sentences, attention_diagrams=session["img_path"])


if __name__ == '__main__':
    app.run(debug=True)
