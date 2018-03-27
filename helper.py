import requests, json, numpy
import matplotlib.pyplot as plt

from datetime import datetime
from paralleldots import similarity, ner, taxonomy, sentiment, keywords, intent, emotion, abuse
from AUTH import news_key, pd_key


def printJSON(JSON):
	''' Prints JSON object in readable format'''
	print(json.dumps(JSON, indent=4))

def convertDatetime(datet):
    return datetime.strptime(datet, '%Y-%m-%dT%H:%M:%SZ')

def similarityscore(title1, title2):
		return similarity(title1,title2)['normalized_score']


newsAPI_sources = 'associated-press, cnn, abc-news, the-hill, the-new-york-times, the-washington-post'


def addEvent(query):

	# Initializing dict
	publishdelay = {}


	url = ('https://newsapi.org/v2/everything?'
	       'q=' + query + '&'
	       'language=en&'
	       'pagesize=20&'
	       'sources=' + newsAPI_sources + '&'
		   'sortBy=relevancy&'
	       'apiKey=' + news_key)

	response = requests.get(url).json()

	text = open('JSON.txt', 'w')
	text.write(response)
	text.close()

	for article in response['articles']:


		# Check if article is deemed relevant enough
		if similarityscore(query, article['title']) >= 3.5:

			id = article['source']['id']

			# If multiple articles from same source found, save earliest one
			if id in publishdelay and convertDatetime(article['publishedAt']) < publishdelay[id][0]:

				publishdelay[id] = [convertDatetime(article['publishedAt']), article['title']]


			elif id not in publishdelay:

				publishdelay[id] = [convertDatetime(article['publishedAt']), article['title']]

	# Get time of earliest published article (time zero)
	time_zero = min([publishdelay[key][0] for key in publishdelay])


	# Calculate delay time of every other article
	for source in publishdelay:
		publishdelay[source].append( (publishdelay[source][0] - time_zero).total_seconds() / 60.0 )

	return publishdelay


delaydict = addEvent('stephen hawking dies')
