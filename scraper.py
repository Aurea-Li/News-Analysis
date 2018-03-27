import urllib.request
from bs4 import BeautifulSoup

webpage = 'https://www.washingtonpost.com/world/europe/family-spokesman-says-physicist-stephen-hawking-has-died-at-the-age-of-76/2018/03/13/0e3a1474-273c-11e8-a227-fd2b009466bc_story.html'
webpage2 = 'https://www.washingtonpost.com/powerpost/house-prepares-for-rapid-vote-today-on-jam-packed-13-trillion-spending-deal/2018/03/22/2074fe7e-2dd6-11e8-8688-e053ba58f1e4_story.html?utm_term=.28c8b14d411e'
webpage3 = 'https://www.washingtonpost.com/politics/trump-attorney-john-dowd-resigns-amid-shake-up-in-presidents-legal-team/2018/03/22/0472ce74-2de3-11e8-8688-e053ba58f1e4_story.html?utm_term=.4933de724e33'
webpage4 = 'https://www.washingtonpost.com/news/dr-gridlock/wp/2018/03/22/airline-crew-member-tried-to-smuggle-160000-worth-of-cocaine-in-his-pants-prosecutors-say/?utm_term=.e10c90a2e219'

hill1 = 'http://thehill.com/homenews/media/373312-laura-benanti-i-like-to-think-that-we-are-all-melania-trump-now'
hill2 = 'http://thehill.com/homenews/state-watch/380458-blue-states-sue-trump-over-census-citizenship-question'
def waposcraper(url, output):

    soup = BeautifulSoup(urllib.request.urlopen(url), 'html.parser')
    text = open(str(output) + '.txt', "w", encoding='utf8')

    article = ''

    # Finding all paragraphs
    for p in soup.article.find_all('p'):


        # Excluding photo captions and author info
        if 'class' not in p.attrs:
            for string in p.strings:
                article += string + "\n"


    text.write(article)
    text.close()

def hillscraper(url, output):

    soup = BeautifulSoup(urllib.request.urlopen(url), 'html.parser')
    text = open(str(output) + '.txt', "w", encoding='utf8')

    article = ''

    # Finding all paragraphs
    for div in soup.article.find_all('div'):
        # for p in div.find_all('p'):

        if 'content-wrp' in div['class']:
            for div in div.find_all('div'):
                print(div.attrs)
                for string in div.strings:
                    print(string)



    text.write(article)
    text.close()


# from AUTH import news_key
# import requests, json
# url = ('https://newsapi.org/v2/everything?'
#        'q=trump&'
#        'language=en&'
#        'pagesize=20&'
#        'sources=the-hill&'
# 	   'sortBy=relevancy&'
#        'apiKey=' + news_key)
#
# response = requests.get(url).json()
#
# text = open('JSON.txt', 'w')
# text.write(json.dumps(response, indent=4))
# text.close()



hillscraper(hill1, 'hill1')
# hillscraper(hill2, 'hill2')
# waposcraper(webpage, 'wapo')
# waposcraper(webpage2, 'wapo2')
# waposcraper(webpage3, 'wapo3')
# waposcraper(webpage4,'wapo4')
