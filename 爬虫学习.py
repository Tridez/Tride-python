from bs4 import BeautifulSoup
import requests
heads = {
   "User-Agent" : 
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
        "AppleWebKit/537.36 (KHTML, like Gecko)" 
        "Chrome/139.0.0.0 Safari/537.36"
    }
for page_num in range(0, 250, 25):
    Url = 'https://movie.douban.com/top250?start={page_num}'
    response = requests.get(Url, headers = heads)
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.find_all('span', class_ = 'title')
    for q in quotes:
        title = q.get_text(strip = True).replace("\xa0", "").replace("\n", "")
        print(title)
print(response.status_code)

