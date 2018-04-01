import urllib.request
from bs4 import BeautifulSoup

filepath = '/Users/Aurea/Desktop/GitHub/News-Analysis/textfiles/'

webpage = 'https://www.washingtonpost.com/world/europe/family-spokesman-says-physicist-stephen-hawking-has-died-at-the-age-of-76/2018/03/13/0e3a1474-273c-11e8-a227-fd2b009466bc_story.html'
webpage2 = 'https://www.washingtonpost.com/powerpost/house-prepares-for-rapid-vote-today-on-jam-packed-13-trillion-spending-deal/2018/03/22/2074fe7e-2dd6-11e8-8688-e053ba58f1e4_story.html?utm_term=.28c8b14d411e'
webpage3 = 'https://www.washingtonpost.com/politics/trump-attorney-john-dowd-resigns-amid-shake-up-in-presidents-legal-team/2018/03/22/0472ce74-2de3-11e8-8688-e053ba58f1e4_story.html?utm_term=.4933de724e33'
webpage4 = 'https://www.washingtonpost.com/news/dr-gridlock/wp/2018/03/22/airline-crew-member-tried-to-smuggle-160000-worth-of-cocaine-in-his-pants-prosecutors-say/?utm_term=.e10c90a2e219'

hill1 = 'http://thehill.com/homenews/media/373312-laura-benanti-i-like-to-think-that-we-are-all-melania-trump-now'
hill2 = 'http://thehill.com/homenews/state-watch/380458-blue-states-sue-trump-over-census-citizenship-question'

ap1 = 'https://apnews.com/7fb0980b01e44421af41e6ef530c20b7'

cnn1 = 'https://www.cnn.com/2018/02/23/asia/ivanka-trump-south-korea-olympics-intl/index.html'
cnn2 = 'https://www.cnn.com/videos/politics/2018/02/21/rachel-crooks-trump-tweet-sot-ctn.cnn'

def waposcraper(url, textname):

    soup = BeautifulSoup(urllib.request.urlopen(url), 'html.parser')
    text = open(str(textname) + '.txt', 'w', encoding='utf8')

    article = ''

    # Finding all paragraphs
    for p in soup.article.find_all('p'):


        # Excluding photo captions and author info
        if 'class' not in p.attrs:
            for string in p.strings:
                article += string + "\n"


    text.write(article)
    text.close()

#TODO: Improve scraper
def hillscraper(url, textname):
    """
    url: string
    textname: string
    Output: text file with textname containing article
    """

    soup = BeautifulSoup(urllib.request.urlopen(url), 'html.parser')
    text = open(str(textname) + '.txt', 'wb')

    firstparagraphs = soup.find('div', {'class':'field-item even', 'property': 'content:encoded'}).find_all(['p'])


    # Getting rid of annoying hyperlinks to other articles
    for p in firstparagraphs:
        for sp in p.find_all('span'):
            for sp2 in sp.find_all('span'):
                sp2.decompose()



    article = b'\n'.join([p.text.encode('utf8') for p in firstparagraphs])       

    secondparagraphs = soup.find_all('div', {'class': 'ra-module'})

    article += b'\n'.join([p.text.encode('utf8') for p in secondparagraphs])



    text.write(article)
    text.close()


def apscraper(url, textname):

    soup = BeautifulSoup(urllib.request.urlopen(url), 'html.parser')
    text = open(str(textname) + '.txt', 'wb')

    paragraphs = soup.find('div', {'class':'articleBody'}).find_all(['p'])
    article = b'\n'.join([p.text.encode('utf8') for p in paragraphs])       

    text.write(article)
    text.close()

#TODO: could refine
def cnnscraper(url, textname):

    soup = BeautifulSoup(urllib.request.urlopen(url), 'html.parser')
    text = open(str(textname) + '.txt', 'wb')

    # Check if link is to video (no article)
    if soup.find('div', {'itemprop':'articleBody'}):

        paragraphs = soup.find('div', {'itemprop':'articleBody'}).find_all(True, {'class': ['zn-body__paragraph', 'zn-body__paragraph speakable']})



        article = b'\n'.join([p.text.encode('utf8') for p in paragraphs])      
        text.write(article)

    else: 
        text.write(b'No text available: video')

    text.close()

    

# from AUTH import news_key
# import requests, json
# url = ('https://newsapi.org/v2/everything?'
#        'q=trump&'
#        'language=en&'
#        'pagesize=20&'
#        'sources=cnn&'
# 	   'sortBy=relevancy&'
#        'apiKey=' + news_key)

# response = requests.get(url).json()

# text = open('JSON.txt', 'w')
# text.write(json.dumps(response, indent=4))
# text.close()



# hillscraper(hill1, 'hill1')
# hillscraper(hill2, 'hill2')
# waposcraper(webpage, 'wapo')
# waposcraper(webpage2, 'wapo2')
# waposcraper(webpage3, 'wapo3')
# waposcraper(webpage4,'wapo4')

# apscraper(ap1, '/Users/Aurea/Desktop/GitHub/News-Analysis/textfiles/ap1')
cnnscraper(cnn1, filepath + 'cnn1')
cnnscraper(cnn2, filepath + 'cnn2')