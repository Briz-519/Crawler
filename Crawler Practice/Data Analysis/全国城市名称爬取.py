# -*- coding : utf-8 -*-
# @Time : 8/9/2020 13:24
# @Author : Briz
# @File : 全国城市名称爬取.py
# @Software: PyCharm

import requests
from lxml import etree

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.52"}

url = 'https://www.aqistudy.cn/historydata/'
page_text=requests.get(url=url,headers=headers).text
tree=etree.HTML(page_text)
li_list=tree.xpath('//div[@class="bottom"]/ul/div[2]/li')
all_city_names=[]
for li in li_list:
    city_name=li.xpath('./a/text()')[0]
    all_city_names.append(city_name)
print(all_city_names,len(all_city_names))

















