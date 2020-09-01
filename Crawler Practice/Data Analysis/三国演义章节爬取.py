# -*- coding : utf-8 -*-
# @Time : 8/6/2020 21:35
# @Author : Briz
# @File : 三国演义章节爬取.py
# @Software: PyCharm


import requests
from bs4 import BeautifulSoup

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.52"}
url='https://www.shicimingju.com/book/sanguoyanyi.html'
page_text=requests.get(url=url,headers=headers).text
soup=BeautifulSoup(page_text,'lxml')
li_lists=soup.select('.book-mulu>ul>li')
fp=open('./三国演义.txt','w',encoding='utf-8')
for li in li_lists:
    title=li.a.string
    detail_url="https://www.shicimingju.com"+li.a['href']
    detail_page=requests.get(url=detail_url,headers=headers).text
    detail_soup=BeautifulSoup(detail_page,'lxml')
    detail_text=detail_soup.find('div',class_='chapter_content').text
    fp.write(title+':'+detail_text+'\n')
    print(title,"Crawler Finish!")





