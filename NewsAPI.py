import requests, json
from paralleldots import similarity, ner, taxonomy, sentiment, keywords, intent, emotion, abuse
from AUTH import news_key, pd_key

def printJSON(JSON):
	''' Prints JSON object in readable format'''
	print(json.dumps(JSON, indent=4))


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

# Create matrix of relevancy
relevance = []

# for article in response['articles']:

printJSON(response)



