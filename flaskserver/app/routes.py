from flask import request, render_template
from bs4 import BeautifulSoup
import requests
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras import layers
from sklearn.preprocessing import LabelEncoder
from keras.models import load_model
from app import app

def getSiteTitle(site):
	header = requests.utils.default_headers()
	req = requests.get(site, header)
	soup = BeautifulSoup(req.content, 'html.parser')

	soup.prettify()

	siteTitle = ''

	if site.find("title") is not None:
		siteTitle = soup.title.string
	elif site.find("h1") is not None:
		siteTitle = soup.h1.string

	return siteTitle

def getPrediction(title):
	model = load_model('predictor.h5')
    #To predict 
	tokenizer = Tokenizer(num_words=500)
	tokenizer.fit_on_texts(title)
	input = tokenizer.texts_to_sequences(title)
	intput = pad_sequences(input, padding='post', maxlen=50)
	model.predict(input)

@app.route('/')
def my_form():
    return render_template('input.html', clickbait="Enter article link:")

@app.route('/', methods=['POST'])
def my_form_post():
	clickbait = "Enter a article!"
	text = request.form['text']
	clickbait = getSiteTitle(text)
	prediction = getPrediction(clickbait)
	return render_template('input.html', clickbait=prediction)