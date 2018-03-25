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

	# Publish time, publish time delay dicts
	publishtimes = {}
	publishtitle = {}
	publishdelay = {}


	url = ('https://newsapi.org/v2/everything?'
	       'q=' + query + '&'
	       'language=en&'
	       'pagesize=20&'
	       'sources=' + newsAPI_sources + '&'
		   'sortBy=relevancy&'
	       'apiKey=' + news_key)

	response = requests.get(url).json()

	printJSON(response)

	#TODO: Change data structure to dictionary tuple

	for article in response['articles']:

		# Check if article is deemed relevant enough
		if similarityscore(query, article['title']) >= 3:

			id = article['source']['id']

			# If multiple articles from same source found, save earliest one
			if id in publishtimes and convertDatetime(article['publishedAt']) < publishtimes[id]:

				publishtimes[id] = convertDatetime(article['publishedAt'])
				publishtitle[id] = article['title']


			elif id not in publishtimes:

				publishtimes[id] = convertDatetime(article['publishedAt'])
				publishtitle[id] = article['title']


	# Get time of earliest published article (time zero)
	time_zero = min(publishtimes.values())


	# Calculate delay time of every other article

	for source in publishtimes:
		publishdelay[source] = (publishtimes[source] - time_zero).total_seconds() / 60.0

	# TODO: Save publishdelayg as tuple and use it in plt instead of converting back to dict
	# Sort values
	publishdelayg = dict(sorted(publishdelay.items(), key=lambda x: x[1]))

	
	return publishdelayg

# addEvent('rex +tillerson fired')
delaydict = addEvent('Stephen +hawking died')
# addEvent('shooting great mills high school maryland')
# addEvent('Toys R Us close stores')

 

# print(delaydict)

# Create matplotlib figure
fig, ax = plt.subplots(1)

plt.bar(range(len(delaydict)), list(delaydict.values()), align='center')
plt.xticks(range(len(delaydict)), list(delaydict.keys()))
plt.xticks(rotation=45)
plt.ylabel('Minutes')
plt.title('Average Publish Delay')
plt.tight_layout()
plt.show()
