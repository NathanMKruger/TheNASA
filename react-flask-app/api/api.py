import time
from bs4 import BeautifulSoup
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras import layers
from sklearn.preprocessing import LabelEncoder
from keras.models import load_model
import requests
from flask import request, Flask


app = Flask(__name__)


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
	#TO LOAD MODEL 
	model = load_model('predictor.h5')
	tokenizer = Tokenizer(num_words=500)
	tokenizer.fit_on_texts("surprise")
	input = tokenizer.texts_to_sequences("surprise")
	input = pad_sequences(input, padding='post', maxlen=150)
	prediction = model.predict(input)
	print(prediction)
	return prediction


@app.route('/predict', methods = ['GET', 'POST'])
def get_url():
	if request.method == 'GET':
		url = request.args.get('url', None)
		if url:
			return {'prediction': getPrediction(getSiteTitle(url))}
		return "No url is given!"

@app.route('/time')
def get_current_time():
	return {'time': time.time()}