from flask import request, render_template
from app import app

@app.route('/')
def my_form():
    return render_template('input.html')

@app.route('/', methods=['POST'])
def my_form_post():
	clickbait = "Enter a article!"
	text = request.form['text']
	clickbait = text.upper()
	#return clickbait
	return render_template('input.html', clickbait=clickbait)