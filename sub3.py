import json,glob

for i in glob.glob('out/*'):
    with open(i,'r',encoding='utf8')as r:
        data = json.load(r)
        print(data['data_title'],data['pc_name'])
        if data['pc_name'] == '':
            print(data)