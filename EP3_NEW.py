import requests
from bs4 import BeautifulSoup

url = "https://api.bilibili.com/x/web-interface/search/type?search_type=video&keyword=司空震"

heads = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",  #我是 Chrome 浏览器
    "Referer": "https://www.bilibili.com/", #我是从B站网页跳过来的
    "Accept": "application/json, text/plain, */*",
    "Cookie": "buvid3=AE8E16E7-8CDA-63E7-A0E4-16806814374653512infoc; b_nut=1755567553; _uuid=D574A447-7CB9-CF86-6463-BF193A8A449251603infoc; enable_web_push=DISABLE; buvid_fp=b9448f401c52429ea6734f3f35d43828; DedeUserID=1352487065; DedeUserID__ckMd5=2d1275d88c6e9922; theme-tip-show=SHOWED; rpdid=0zbfVGpdlX|rPgeDZdJ|19R|3w1UObll; theme-avatar-tip-show=SHOWED; CURRENT_BLACKGAP=0; buvid4=397A0AC0-100E-66B7-DFE8-4E2FDCAC6FFB54711-025081909-efn5ML6MX66Z06T6LKoLCFuSG08tYqwHcTDTJG5CVYiztTbb/HgRMmuw71qDNxKU; LIVE_BUVID=AUTO8217577773217110; SESSDATA=22edc203%2C1773386057%2Cedd5f%2A92CjAPvnhM9Vsziq2xGIC2-PETYzZOIMRX2AaxOOmGpGevVD6Nbygmqxj5vNPExbgERE8SVlFZWFdTTE8xLTZ3djNrOS1SdTZOR2kwQW4taC11VzFsQ0xxcXl4eFRjOGhnbnFhc1NQblp2UVFiRDYxQUkyS3BOcHpHRUdid293Q3lROS14T2xuN1V3IIEC; bili_jct=0d9e4d6899c1d864cb95585c72b6e631; theme-switch-show=SHOWED; CURRENT_QUALITY=127; hit-dyn-v2=1; theme_style=light; CURRENT_LANGUAGE=; PVID=1; ogv_device_support_hdr=1; ogv_device_support_dolby=0; bp_t_offset_1352487065=1175833321179971584; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NzMxOTYwNTIsImlhdCI6MTc3MjkzNjc5MiwicGx0IjotMX0.-1NSLHDk43mvH7EgTHIC5aeWWrSuoBQlgxyzkYsveAk; bili_ticket_expires=1773195992; home_feed_column=4; CURRENT_FNVAL=4048; sid=6uhbvaac; browser_resolution=150-804; b_lsid=26229227_19CD032C0A0"

}

params = {
    "search_type": "video",
    "keyword": "司空震",
    "page": 1
}

response = requests.get(url, params = params, headers = heads)

response.encoding = "utf-8"   
soup = BeautifulSoup(response.text, "html.parser")

print(response.status_code)
data = response.json()

for v in data["data"]["result"]:
    title = BeautifulSoup(v["title"], "html.parser").text
    bvid = v["bvid"]

    link = f"https://www.bilibili.com/video/{bvid}"

    print(title)
    print(link)