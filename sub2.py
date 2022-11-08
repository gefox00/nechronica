import json, requests, pyperclip, os, time
from bs4 import BeautifulSoup

chdata = []
res = requests.get('https://charasheet.vampire-blood.net/list_nechro.html?name=ゴライアス&order=&page=2')
soup = BeautifulSoup(res.content, 'html.parser')
links = soup.find_all('a')
for link in links:
    if '.txt' in link.get('href'):
        chdata.append(str(link.get('href')).replace('.txt','.json'))
for i in chdata:
    res = requests.get(i).content
    data = json.loads(res)

    print(data)
    time.sleep(1)