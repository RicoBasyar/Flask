from flask import Flask, render_template, request
from test import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    chat = request.form['name']
    while True:
        response = respond(chat)
        return render_template('index.html', name=response)
    

if __name__ == '__main__':
    app.run(debug=True)