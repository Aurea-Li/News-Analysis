import requests, json
from datetime import datetime
from paralleldots import similarity, ner, taxonomy, sentiment, keywords, intent, emotion, abuse
from AUTH import news_key, pd_key

def printJSON(JSON):
	''' Prints JSON object in readable format'''
	print(json.dumps(JSON, indent=4))

def convertDatetime(datet):
    return datetime.strptime(datet, '%Y-%m-%dT%H:%M:%SZ')


# Get list of all english sources
url = ('https://newsapi.org/v2/sources?'
       'language=en&'
       'country=us&'
       'category=general&'
       'apiKey=' + news_key)

response = requests.get(url).json()

sources = ''



for source in response['sources']:
    sources = sources + source['id'] + ', '

# Omit last comma
sources = sources[:-2]


# Save query
url = ('https://newsapi.org/v2/everything?'
       'q=rex tillerson fired&'
       'language=en&'
       'pagesize=5&'
       'sources=' + sources + '&'
       'apiKey=' + news_key)
response = requests.get(url).json()

# Verify relevancy of articles

# Create matrix of relevancy
relevance = []

# Publish time, publish time delay dicts
publishtimes = {}
publishdelay = {}
test = {}

# Save each time
for article in response['articles']:
    publishtimes[article['source']['id']] = convertDatetime(article['publishedAt'])
    test[article['source']['id']] = article['publishedAt']


# Get time of earliest published article (time zero)
time_zero = min(publishtimes.values())


# Calculate delay time of every other article

for source in publishtimes:
    publishdelay[source] = (publishtimes[source] - time_zero).total_seconds() / 60

print(publishdelay)
print(test)

# Plot bar graph

# delta = publish_delay['cbs-news'][1] - publish_delay['cnn'][1]

# rdelta = publish_delay['cnn'] - publish_delay['cbs-news']



# print(min(publish_delay,key=publish_delay.get))







