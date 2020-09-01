# -*- coding : utf-8 -*-
# @Time : 8/9/2020 14:20
# @Author : Briz
# @File : 站长之家简历模板爬取.py
# @Software: PyCharm

import requests
from lxml import etree
import os

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.52"}

if not os.path.exists('./简历模板'):
    os.mkdir('./简历模板')
home_url="http://sc.chinaz.com/jianli/free.html"
page_text=requests.get(url=home_url,headers=headers).text
tree=etree.HTML(page_text)
a_list=tree.xpath('//div[@class="main_list jl_main"]/div')
for a in a_list:
    detail_url=a.xpath('./a/@href')[0]
    detail_text=requests.get(url=detail_url,headers=headers).text
    detail_tree=etree.HTML(detail_text)
    title=detail_tree.xpath('//div[@class="ppt_tit clearfix"]/h1/text()')[0]+'.rar'
    title=title.encode('iso-8859-1').decode('utf-8')
    deteil_download=detail_tree.xpath('//div[@class="clearfix mt20 downlist"]//li[1]/a/@href')[0]
    detail_data=requests.get(url=deteil_download,headers=headers).content
    detail_path='./简历模板/'+title
    with open(detail_path,'wb') as fp:
        fp.write(detail_data)
        print(title,"Downloading...")
for i in range(2,11):
    i=str(i)
    home_url = "http://sc.chinaz.com/jianli/free_"+i+".html"
    page_text = requests.get(url=home_url, headers=headers).text
    tree = etree.HTML(page_text)
    a_list = tree.xpath('//div[@class="main_list jl_main"]/div')
    for a in a_list:
        detail_url = a.xpath('./a/@href')[0]
        detail_text = requests.get(url=detail_url, headers=headers).text
        detail_tree = etree.HTML(detail_text)
        title = detail_tree.xpath('//div[@class="ppt_tit clearfix"]/h1/text()')[0] + '.rar'
        title = title.encode('iso-8859-1').decode('utf-8')
        deteil_download = detail_tree.xpath('//div[@class="clearfix mt20 downlist"]//li[1]/a/@href')[0]
        detail_data = requests.get(url=deteil_download, headers=headers).content
        detail_path = './简历模板/' + title
        with open(detail_path, 'wb') as fp:
            fp.write(detail_data)
            print(title, "Downloading...")












