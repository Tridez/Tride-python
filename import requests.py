import requests
from bs4 import BeautifulSoup
html_doc = """
<html>
<head>
    <title>This is my first page</title>
</head>
<body>
    <h1>This is the first title</h1>
    <h1>This is the second title</h1>
    <p>This is a paragraph</p>
</body>
</html>"""
soup = BeautifulSoup(html_doc, 'html.parser')
title = soup.find_all('h1')
for t in title:
    print(f'The title is : {t}')

paragraph = soup.find('p')
print('The paragraph is :')
for p in paragraph:
    print(p.text)
url = 'https://www.baidu.com'
reponse = requests.get(url)
print(reponse.status_code)
