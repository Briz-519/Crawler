# -*- coding : utf-8 -*-
# @Time : 8/9/2020 12:10
# @Author : Briz
# @File : 58二手房爬取.py
# @Software: PyCharm

import requests
from lxml import etree

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.52"}
url="https://bengbu.58.com/ershoufang/"
page_text=requests.get(url=url,headers=headers).text
tree=etree.HTML(page_text)
li_list=tree.xpath('//ul[@class="house-list-wrap"]/li')
fp=open('58.txt','w',encoding='utf-8')
for li in li_list:
    title=li.xpath('./div[2]/h2/a/text()')[0]
    price=li.xpath('./div[3]/p[2]//text()')[0]
    size=li.xpath('./div[2]/p/span[2]/text()')[0]
    detail=li.xpath('./div[2]/h2/a/@href')[0]
    print(title)
    print(price)
    print(size)
    print(detail)
    fp.write('Title:'+title+'\n'+'Price:'+price+'\n'+'Size:'+size+'\n'+'Detail:'+detail+'\n'+'\n')





