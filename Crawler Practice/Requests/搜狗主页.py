# -*- coding : utf-8 -*-
# @Time : 8/4/2020 16:08
# @Author : Briz
# @File : 搜狗主页.py
# @Software: PyCharm

import requests

if __name__=="__main__":
    url="https://www.sogou.com/"
    headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.52"
    }
    response=requests.get(url=url,headers=headers)
    page_text=response.text
    print(page_text)
    with open('./sogou.html','w',encoding='utf-8') as fp:
        fp.write(page_text)
    print("Finish!!")