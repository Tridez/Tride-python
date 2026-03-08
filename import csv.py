import requests
from bs4 import BeautifulSoup
url = 'https://news.sina.com.cn/'
heads = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)' 
        'AppleWebKit/537.36 (KHTML, like Gecko)' 
        'Chrome/139.0.0.0 Safari/537.36'}
reponse = requests.get(url, headers=heads)
reponse.encoding = 'utf-8'
if reponse.status_code == 200:
    soup = BeautifulSoup(reponse.text, 'html.parser')
    titles = soup.find_all('a', class_='linkNewsTopBold')
    for t in titles:
        print(t)