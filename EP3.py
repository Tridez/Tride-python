import requests
from bs4 import BeautifulSoup

url = "https://api.bilibili.com/x/web-interface/search/type?search_type=video&keyword=python"

heads = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Referer": "https://www.bilibili.com/",
    "Accept": "application/json, text/plain, */*"
}

params = {
    "search_type": "video",
    "keyword": "python",
    "page": 1
}

response = requests.get(url, params = params, headers = heads)

response.encoding = "utf-8"   

soup = BeautifulSoup(response.text, "html.parser")

print(response.status_code)
data = response.json()

for v in data["data"]["result"]:
    title = BeautifulSoup(v["title"], "html.parser").text
    print(title)