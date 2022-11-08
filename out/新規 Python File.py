import glob,os,shutil,csv,json


for i in glob.glob('*.json'):
    with open(i,'r',encoding='utf8')as r:
        data = json.load(r)
        
        print(data['pc_name'])
