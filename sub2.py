import json, requests, pyperclip, os, time
from bs4 import BeautifulSoup

chdata = []
with open('name.txt','r',encoding='utf8')as r:
    target = r.read().splitlines()
    for i in target:
        res = requests.get(f'https://charasheet.vampire-blood.net/list_nechro.html?name={i}')

        soup = BeautifulSoup(res.content, 'html.parser')
        links = soup.find_all('a')

        for link in links:
            if '.txt' in link.get('href'):
                chdata.append(str(link.get('href')).replace('.txt','.json'))
                print(i,str(link.get('href')).replace('.txt','.json'))
        time.sleep(1)
print(chdata[36])
for i in chdata:
    if len(i) > 1:
        res = requests.get(i)
        data = json.loads(res.content)

        with open(f'out/{i.split("/")[3]}', 'w', encoding='utf8') as w:
            json.dump(data, w, indent=4)
        time.sleep(1)

