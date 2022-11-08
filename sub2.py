import json, requests, pyperclip, os
url = 'https://charasheet.vampire-blood.net/m480061f3dfcc3efbf1ef1dee1e416b76'
res = requests.get(url+'.json')
data = json.loads(res.content)
with open('out.json','w',encoding='utf8')as w:
    json.dump(data,w,indent=4)
print(data)
