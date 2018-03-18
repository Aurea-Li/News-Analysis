import requests, json
from paralleldots import similarity, ner, taxonomy, sentiment, keywords, intent, emotion, abuse
from AUTH import news_key, pd_key

def printJSON(JSON):
	''' Prints JSON object in readable format'''
	print(json.dumps(JSON, indent=4))


url = ('https://newsapi.org/v2/everything?'
       'q=rex tillerson fired&'
       'language=en&'
       'pagesize=100&'
       'apiKey=' + news_key)


# Get list of articles
response = requests.get(url).json()

print(similarity("Sachin is the greatest batsman",
           "Tendulkar is the finest cricketer"))

# printJSON(response)

