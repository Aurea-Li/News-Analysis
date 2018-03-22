import urllib.request
from bs4 import BeautifulSoup

webpage = 'https://www.washingtonpost.com/world/europe/family-spokesman-says-physicist-stephen-hawking-has-died-at-the-age-of-76/2018/03/13/0e3a1474-273c-11e8-a227-fd2b009466bc_story.html'
webpage2 = 'https://www.washingtonpost.com/powerpost/house-prepares-for-rapid-vote-today-on-jam-packed-13-trillion-spending-deal/2018/03/22/2074fe7e-2dd6-11e8-8688-e053ba58f1e4_story.html?utm_term=.28c8b14d411e'
webpage3 = 'https://www.washingtonpost.com/politics/trump-attorney-john-dowd-resigns-amid-shake-up-in-presidents-legal-team/2018/03/22/0472ce74-2de3-11e8-8688-e053ba58f1e4_story.html?utm_term=.4933de724e33'
webpage4 = 'https://www.washingtonpost.com/news/dr-gridlock/wp/2018/03/22/airline-crew-member-tried-to-smuggle-160000-worth-of-cocaine-in-his-pants-prosecutors-say/?utm_term=.e10c90a2e219'


def waposcraper(url, output):

    soup = BeautifulSoup(urllib.request.urlopen(url), 'html.parser')
    text = open(str(output) + '.txt', "w", encoding='utf8')


    # for article in soup.find_all('article'):
    #     print('article found')
    #     if article['class'] == ['paywall']:

    # Determine format


    article = ''

    # Finding all paragraphs
    for p in soup.article.find_all('p'):


        # print(str(p.attrs))

        # Excluding photo captions and author info
        if 'class' not in p.attrs:
            for string in p.strings:
                article += string + "\n"


    text.write(article)
    text.close()



waposcraper(webpage, 'wapo')
waposcraper(webpage2, 'wapo2')
waposcraper(webpage3, 'wapo3')
waposcraper(webpage4,'wapo4')


# soup = BeautifulSoup(page, 'html.parser')
#
# def getText(articleUrl):
#     html = urllib.request.urlopen(articleUrl).read()
#     soup = BeautifulSoup(html)
#     article = soup.body.findAll('article')
#     text = ' '.join([clean(s.text) for s in article[0].findAll('p')])
#
#     print(text)
#     return text
#
#
# getText(article)
