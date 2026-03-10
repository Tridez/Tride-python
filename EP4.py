import requests
from bs4 import BeautifulSoup

url = "https://www.youtube.com/"


response = requests.get(url)
soup = BeautifulSoup(response.text,"html.parser")
titles = soup.find_all('a')


print(response.status_code)

for title in titles:
    text = title.get_text().strip()
    link = title.get("href")

    if text and link:
        print(f"Title:{text} Link:{link}")


