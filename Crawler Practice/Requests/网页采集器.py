# -*- coding : utf-8 -*-
# @Time : 8/4/2020 16:26
# @Author : Briz
# @File : 网页采集器.py
# @Software: PyCharm

import requests

headers={
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.52"
}
url="https://www.baidu.com/s?"
kw=input('Enter a word:')
param={
    'wd':kw
}
response=requests.get(url=url,params=param,headers=headers)
page_text=response.text
fileName=kw+'.html'
with open(fileName,'w',encoding='utf-8')as fp:
    fp.write(page_text)
