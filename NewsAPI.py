import requests, json
from AUTH import news_key

def printJSON(JSON):
	''' Prints JSON object in readable format'''
	print(json.dumps(JSON, indent=4))

# url = ('https://newsapi.org/v2/top-headlines?'
#        'country=us&'
#        'apiKey=' + news_key)

url = ('https://newsapi.org/v2/everything?'
       'q=rex tillerson fired&'
       'language=en&'
       'apiKey=' + news_key)


response = requests.get(url)
printJSON(response.json())
