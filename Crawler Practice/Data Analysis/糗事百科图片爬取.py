# -*- coding : utf-8 -*-
# @Time : 8/6/2020 11:07
# @Author : Briz
# @File : 糗事百科图片爬取.py
# @Software: PyCharm

import requests
import re
import os

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.52"}
url='https://www.qiushibaike.com/imgrank/page/%d/'
if not os.path.exists('./糗图'):
    os.mkdir('./糗图')
img=re.compile(r'<div class="thumb">.*?<img src="(.*?)" alt.*?</div>',re.S)
for pageNum in range(1,14):
    new_url=format(url%pageNum)
    html=requests.get(url=new_url,headers=headers).text
    img_src=re.findall(img,html)
    for src in img_src:
        src='https:'+src
        img_data=requests.get(url=src,headers=headers).content
        img_name=src.split('/')[-1]
        imgPath='./糗图/'+img_name
        with open(imgPath,'wb') as fp:
            fp.write(img_data)
            print(img_name +" download successful!")



