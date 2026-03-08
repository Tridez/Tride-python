from bs4 import BeautifulSoup
import requests
url = 'http://books.toscrape.com/'
responses = requests.get(url)
soup = BeautifulSoup(responses.text, 'html.parser')
print(responses.status_code)
prices = soup.find_all('p' class_='price_color')
for price in prices:
    print(prices.a['price'])
titles = soup.find_all('h3')
for title in titles:
    print(title.a['title'])
