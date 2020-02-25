from flask import request, render_template
from app import app

@app.route('/')
def my_form():
    return render_template('input.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    return processed_text