import requests
from bs4 import BeautifulSoup

url = "https://www.runoob.com/"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/139.0.0.0 Safari/537.36",
    "Referer": "https://www.baidu.com/"
}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text,"html.parser")

links = soup.find_all("a")


print(response.status_code)

for links in links:
    title = links.get_text().strip()
    link = links.get("href")

    if title and link:
        print(f"{title}: {link}:")