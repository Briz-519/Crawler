# -*- coding : utf-8 -*-
# @Time : 8/5/2020 21:58
# @Author : Briz
# @File : 药监总局相关数据爬取.py
# @Software: PyCharm

import requests
import json

id_list=[]
all_data_list=[]
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.52"}
for i in range(1,6):
    i=str(i)
    home_url='http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsList'
    home_data={
        'on': 'true',
        'page': i,
        'pageSize': '15',
        'productName':'',
        'conditionType': '1',
        'applyname':'',
        'applysn':''
    }
    json_ids=requests.post(url=home_url,data=home_data,headers=headers).json()
    for ids in json_ids['list']:
        id_list.append(ids['ID'])

    detail_url='http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsById'
    for id in id_list:
        detail_data={
            'id':id
        }
        detail_json=requests.post(url=detail_url,headers=headers,data=detail_data).json()
        all_data_list.append(detail_json)
        json.dump(all_data_list,fp=open('./药监总局数据.json','w',encoding='utf-8'),ensure_ascii=False)
print("Crawler Finish!")




