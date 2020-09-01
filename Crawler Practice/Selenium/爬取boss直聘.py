# -*- coding : utf-8 -*-
# @Time : 8/21/2020 12:58
# @Author : Briz
# @File : 爬取boss直聘.py
# @Software: PyCharm

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.52"}

import requests
from selenium import webdriver
from lxml import etree
from time import sleep

opt = webdriver.ChromeOptions()
opt .add_argument("–proxy-server=27.43.184.203:9999")# 一定要注意，等号两边不能有空格
bro = webdriver.Chrome(executable_path='chromedriver.exe',chrome_options = opt )
#如何实现让selenium规避被检测到的风险
# bro.get('https://www.zhipin.com/job_detail/?query=python&city=100010000&industry=&position=')
# page_text=bro.page_source
# tree=etree.HTML(page_text)
# li_list=tree.xpath('//*[@id="main"]/div/div[2]/ul/li')
# urls=[]
# for li in li_list:
#     job_name = li.xpath('.//div[@class="info-primary"]/div[1]/div/div[1]/span[1]/a/text()')[0]
#     job_place=li.xpath('.//div[@class="info-primary"]/div[1]/div/div[1]/span[2]/span/text()')[0]
#     print(job_name,job_place)
#     detail_url='https://www.zhipin.com'+li.xpath('.//div[@class="info-primary"]/div[1]/div/div[1]/span[1]/a/@href')[0]
#     urls.append(detail_url)
# bro.quit()

bro.get('https://www.zhipin.com/job_detail/ff69c9fbfe77246c03xy0926GFU~.html?ka=search_list_jname_1_blank&lid=nlp-7dPQsa471yD.search.1')
page_text=bro.page_source
tree=etree.HTML(page_text)
job_desc=tree.xpath('//*[@id="main"]/div[3]/div/div[2]/div[2]/div[1]/div//text()')
print(job_desc)
bro.quit()
















