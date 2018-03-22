import urllib.request
from bs4 import BeautifulSoup

article = 'https://www.washingtonpost.com/world/europe/family-spokesman-says-physicist-stephen-hawking-has-died-at-the-age-of-76/2018/03/13/0e3a1474-273c-11e8-a227-fd2b009466bc_story.html'
page = urllib.request.urlopen(article)

paragraphs = soup.find('article').find("")

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
