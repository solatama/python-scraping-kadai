import requests
from bs4 import BeautifulSoup as bs

url = 'https://news.yahoo.co.jp/articles/703d1768362d140f966b86a410eab88bdf214c91'

response = requests.get(url)
soup = bs(response.text, 'html.parser')
sentences = soup.selecｔ('#uamods > .article_body > div > p')
article_text = ''.join([sentence.text for sentence in sentences])
print(article_text)
