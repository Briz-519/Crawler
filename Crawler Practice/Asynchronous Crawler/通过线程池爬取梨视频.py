# -*- coding : utf-8 -*-
# @Time : 8/12/2020 22:15
# @Author : Briz
# @File : 通过线程池爬取梨视频.py
# @Software: PyCharm

import requests
from lxml import etree
import re
from multiprocessing.dummy import Pool

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.52"}
url="https://www.pearvideo.com/category_130"
page_text=requests.get(url=url,headers=headers).text
tree=etree.HTML(page_text)
li_list=tree.xpath('//ul[@class="listvideo-list clearfix"]/li')
urls=[]
for li in li_list:
    detail_url="https://www.pearvideo.com/"+li.xpath('./div/a/@href')[0]
    name=li.xpath('./div/a/div[2]/text()')[0]+'.mp4'
    detail_text=requests.get(url=detail_url,headers=headers).text
    t='srcUrl="(.*?)",vdoUrl'
    detail_video=re.findall(t,detail_text)[0]
    dic={
        'name':name,
        'url':detail_video
    }
    urls.append(dic)

def get_video(dic):
    url=dic['url']
    print(dic['name'],' downloading...')
    video=requests.get(url=url,headers=headers).content
    with open(dic['name'],'wb') as fp:
        fp.write(video)
        print(dic['name'],' download successfully!')
pool=Pool(4)
pool.map(get_video,urls)
pool.close()
pool.join()














