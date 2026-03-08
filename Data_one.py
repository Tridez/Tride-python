from bs4 import BeautifulSoup
import requests
contents = requests.get('http://books.toscrape.com/').text
soup = BeautifulSoup(contents, 'html.parser')
all-titles = soup.findall('h3')
for title in all-titles:
    all-links = title.findall('a')
    for link in all-links:
        print(link.string)