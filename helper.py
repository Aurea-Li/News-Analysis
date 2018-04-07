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

def getQuery(query):

	url = ('https://newsapi.org/v2/everything?'
	       'q=' + query + '&'
	       'language=en&'
	       'pagesize=20&'
	       'sources=' + newsAPI_sources + '&'
		   'sortBy=relevancy&'
	       'apiKey=' + news_key)

	return requests.get(url).json()


newsAPI_sources = 'associated-press, cnn, abc-news, the-hill, the-new-york-times, the-washington-post'


def addEvent(query):

	publishdelay = {}

	response = getQuery(query)

	text = open('JSON.txt', 'w')
	text.write(json.dumps(response, indent=4))
	text.close()

	for article in response['articles']:

		title = article['title']

		# Check if article is deemed relevant enough
		if similarityscore(query, title) >= 3.5:

			id = article['source']['id']

			# If multiple articles from same source found, save earliest one
			if id in publishdelay and convertDatetime(article['publishedAt']) < publishdelay[id]['datetime']:

				publishdelay[id] = {'datetime': convertDatetime(article['publishedAt']), 'title': title}


			elif id not in publishdelay:

				publishdelay[id] = {'datetime': convertDatetime(article['publishedAt']), 'title':  title}

	# Get time of earliest published article (time zero)
	time_zero = min([publishdelay[key]['datetime'] for key in publishdelay])


	# Calculate delay time of every other article
	for source in publishdelay:
		publishdelay[source]['delay time'] = (publishdelay[source]['datetime'] - time_zero).total_seconds() / 60.0 

	return publishdelay


delaydict = addEvent('stephen hawking dies')
print(delaydict)
