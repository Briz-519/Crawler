# -*- coding : utf-8 -*-
# @Time : 8/12/2020 15:04
# @Author : Briz
# @File : 代理操作.py
# @Software: PyCharm

import requests

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.52"}
url="https://www.baidu.com/s?wd=ip"
page_text=requests.get(url=url,headers=headers,proxies={"https":"222.110.147.50:3128"}).text
with open('./IP.html','w',encoding='utf-8') as fp:
    fp.write(page_text)
















