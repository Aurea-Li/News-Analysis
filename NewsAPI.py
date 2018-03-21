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



# Get list of all english sources
url = ('https://newsapi.org/v2/sources?'
       'language=en&'
       'country=us&'
       'category=general&'
       'apiKey=' + news_key)

response = requests.get(url).json()

# Initialize publishdelay dictionary and create source list
sources = ''
publishdelay = {}

for source in response['sources']:
	sources = sources + source['id'] + ', '
	publishdelay[source['id']] = []

# Omit last comma
sources = sources[:-2]



def addEvent(query):

	# Publish time, publish time delay dicts
	publishtimes = {}
	publishtitle = {}


	url = ('https://newsapi.org/v2/everything?'
	       'q=' + query + '&'
	       'language=en&'
	       'pagesize=100&'
	       'sources=' + sources + '&'
		   'sortBy=relevancy&'
	       'apiKey=' + news_key)

	response = requests.get(url).json()

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
		minutes = (publishtimes[source] - time_zero).total_seconds() / 60

		# If article is published within 8 hours of first article
		publishdelay[source].append((publishtimes[source] - time_zero).total_seconds() / 60)

	return None


addEvent('rex +tillerson fired')
addEvent('Stephen +hawking died')
# addEvent('shooting great mills high school maryland')
# addEvent('Toys R Us close stores')


# Create average delay dict
publishdelayg = {}
for source in publishdelay:

	if publishdelay[source]:
		publishdelayg[source] = sum(publishdelay[source])/len(publishdelay[source])





# Plot bar graph

plt.bar(range(len(publishdelayg)), list(publishdelayg.values()), align='center')
plt.xticks(range(len(publishdelayg)), list(publishdelayg.keys()))
plt.ylabel('Minutes')
plt.title('Average Publish Delay')

plt.show()
