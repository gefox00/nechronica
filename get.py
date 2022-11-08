import json, requests, pyperclip, os, time
from bs4 import BeautifulSoup
url = 'https://charasheet.vampire-blood.net/list_nechro.html?order=&page='
chdata = []

for i in range(201):
    res = requests.get(url + f'{i}')
    soup = BeautifulSoup(res.content, 'html.parser')
    links = soup.find_all('a')
    for link in links:
        if '.txt' in link.get('href'):
            chdata.append(str(link.get('href')).replace('.txt','.json'))

    time.sleep(1)

for i in chdata:
    res = requests.get(i)
    data = json.loads(res.content)
    with open(f'out/{i.split("/")[3]}', 'w', encoding='utf8') as w:
        json.dump(data, w, indent=4)
    time.sleep(1)