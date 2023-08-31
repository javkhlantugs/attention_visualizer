from flask import Flask, render_template, request, session
from mask import *
import os
import uuid

app = Flask(__name__)
app.secret_key = 'habibi'

@app.route('/', methods=['GET', 'POST'])
def index():
    session['new_session_id'] = str(uuid.uuid4())
    if request.method == 'POST':
        sentence = request.form['sentence']
        session['img_path'] = os.path.join("static", "img", session['new_session_id'])
        os.makedirs(session['img_path'])
        generated_sentences = generate(sentence, session['new_session_id'])
        return render_template('index.html', sentence=sentence, generated_sentences=generated_sentences, attention_diagrams=session["img_path"])

    return render_template('index.html', sentence=None, generated_sentences=None, attention_diagrams=None)

# @app.teardown_request
# def delete_session_folder(exception=None):
#     folder_path = session.get('img_path')
#     if folder_path:
#         import shutil
#         shutil.rmtree(folder_path, ignore_errors=True)

if __name__ == '__main__':
    app.run(debug=True)
