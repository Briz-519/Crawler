# -*- coding : utf-8 -*-
# @Time : 8/5/2020 15:59
# @Author : Briz
# @File : KFC餐厅查询.py
# @Software: PyCharm

import requests
import json

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.52"}
url='http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
area=input("Enter a area:")
data={
    'cname':'',
    'pid':'',
    'keyword':area,
    'pageIndex': '1',
    'pageSize': '10'
}
response=requests.post(url=url,data=data,headers=headers)
html=response.json()
fileName=area+'.json'
json.dump(html,fp=open(fileName,'w',encoding='utf-8'),ensure_ascii=False)

