import requests, json

def printJSON(JSON):
	''' Prints JSON object in readable format'''
	print(json.dumps(JSON, indent=4))

url = ('https://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=19771d3100434feda08963940ac937f6')

      
response = requests.get(url)
printJSON(response.json())
