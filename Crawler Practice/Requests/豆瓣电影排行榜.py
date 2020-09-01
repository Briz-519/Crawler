# -*- coding : utf-8 -*-
# @Time : 8/5/2020 15:29
# @Author : Briz
# @File : 豆瓣电影排行榜.py
# @Software: PyCharm

import json
import requests

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.52"}

url="https://movie.douban.com/j/chart/top_list?"
param={
    'type': '10',
    'interval_id': '100:90',
    'action': '',
    'start': '0', #从库中第几部开始
    'limit': '20'  #一次取出数据的个数
}
response=requests.get(url=url,params=param,headers=headers)
list_data=response.json()
fp=open('./douban.json', 'w', encoding='utf-8')
json.dump(list_data,fp=fp,ensure_ascii=False)
