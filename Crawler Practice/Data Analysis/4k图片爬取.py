# -*- coding : utf-8 -*-
# @Time : 8/9/2020 13:24
# @Author : Briz
# @File : 4k图片爬取.py
# @Software: PyCharm

import requests
from lxml import etree
import os

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.52"}

url = 'http://pic.netbian.com/4kfengjing/'
response=requests.get(url=url,headers=headers)
page_text=response.text
tree=etree.HTML(page_text)
li_list=tree.xpath('//div[@class="slist"]//li')
if not os.path.exists('./4k图片'):
    os.mkdir('./4k图片')
for li in li_list:
    img_url='http://pic.netbian.com'+li.xpath('./a/img/@src')[0]
    img_name=li.xpath('./a/img/@alt')[0]+'.jpg'
    img_name=img_name.encode('iso-8859-1').decode('gbk')
    img_data=requests.get(url=img_url,headers=headers).content
    img_path='./4k图片/'+img_name
    with open(img_path,'wb') as fp:
        fp.write(img_data)
        print(img_name,"Downloading...")



