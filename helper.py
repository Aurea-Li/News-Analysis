import requests, json
import matplotlib.pyplot as plt
import urllib.request
from datetime import datetime
from paralleldots import similarity, ner, taxonomy, sentiment, keywords, intent, emotion, abuse
from AUTH import news_key, pd_key
from textanalysis import wordcounter
from scraper import scrapArticle


def printJSON(JSON):
	''' Prints JSON object in readable format'''
	print(json.dumps(JSON, indent=4))

def convertDatetime(datet):
    return datetime.strptime(datet, '%Y-%m-%dT%H:%M:%SZ')

def similarityscore(title1, title2):
		return similarity(title1,title2)['normalized_score']

def isvalidLink(url):
	try:
		urllib.request.urlopen(url)
	except:
		return False
	return True


def getQuery(query):

	url = ('https://newsapi.org/v2/everything?'
	       'q=' + query + '&'
	       'language=en&'
	       'pagesize=100&'
	       'sources=' + newsAPI_sources + '&'
		   'sortBy=relevancy&'
	       'apiKey=' + news_key)

	return requests.get(url).json()

def extractInfo(response, query):

	publishdelay = {}

	for article in response['articles']:

		title = article['title']

		# Check if article link is valid and title relevant enough, and article is not a video
		if similarityscore(query, title) >= 3.5 and isvalidLink(article['url']) and article['author']:

			id = article['source']['id']

			# Scrap article and determine word count
			textfp = scrapArticle(article['url'], id)
			wordcount = wordcounter(textfp)

			# If first article from source or the earliest article from said source, save
			if id not in publishdelay:
				publishdelay[id] = [{'datetime': convertDatetime(article['publishedAt']), 'title': title, 'word count': wordcount}]

			elif len(publishdelay[id]) < 3:
				if convertDatetime(article['publishedAt']) < publishdelay[id][0]['datetime']:
					publishdelay[id].insert(0, {'datetime': convertDatetime(article['publishedAt']), 'title': title, 'word count': wordcount})

				else:
					publishdelay[id].append({'datetime': convertDatetime(article['publishedAt']), 'title': title, 'word count': wordcount})

	# Get time of earliest published article (time zero)
	time_zero = min([publishdelay[key][0]['datetime'] for key in publishdelay])


	# Calculate delay time of every other article
	for source in publishdelay:
		publishdelay[source][0]['delay time'] = (publishdelay[source][0]['datetime'] - time_zero).total_seconds() / 60.0 

	return publishdelay




def addEvent(query):

	response = getQuery(query)

	return extractInfo(response, query)



newsAPI_sources = 'associated-press, cnn, the-new-york-times, the-washington-post'

# print(addEvent('stephen hawking dies'))
# # import urllib.request
# # from bs4 import BeautifulSoup
# url = 'http://thehill.com/homenews/house/382176-ryan-responsible-nations-cant-tolerate-chemical-attack-in-syria'
# print(isvalidLink(url))