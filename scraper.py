import urllib.request
from bs4 import BeautifulSoup

# article = 'https://www.washingtonpost.com/world/europe/family-spokesman-says-physicist-stephen-hawking-has-died-at-the-age-of-76/2018/03/13/0e3a1474-273c-11e8-a227-fd2b009466bc_story.html'
webpage = 'https://www.washingtonpost.com/business/economy/trump-moves-to-crack-down-on-china-trade-with-50-billion-in-tariffs-on-imported-products/2018/03/22/c09309e8-2de3-11e8-8ad6-fbc50284fce8_story.html?utm_term=.b90e191c097c'
soup = BeautifulSoup(urllib.request.urlopen(webpage), 'html.parser')



article = ''

# for string in soup.article.p.strings:
#     sentence += string
#
# print(sentence)

for p in soup.article.find_all('p'):
    for string in p.strings:
        article += string


text = open('wapo.txt', "w")
text.write(article)
text.close()

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
