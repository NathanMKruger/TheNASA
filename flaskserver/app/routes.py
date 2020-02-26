from flask import request, render_template
from bs4 import BeautifulSoup
import requests
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

@app.route('/')
def my_form():
    return render_template('input.html', clickbait="Enter article link:")

@app.route('/', methods=['POST'])
def my_form_post():
	clickbait = "Enter a article!"
	text = request.form['text']
	clickbait = getSiteTitle(text)
	return render_template('input.html', clickbait=clickbait)