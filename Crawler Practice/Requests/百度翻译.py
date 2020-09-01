# -*- coding : utf-8 -*-
# @Time : 8/5/2020 14:57
# @Author : Briz
# @File : 百度翻译.py
# @Software: PyCharm

import requests
import json

url="https://fanyi.baidu.com/sug"
word=input("Enter a word to translate:")
data={
    'kw':word
}
headers={
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.52"
}
response=requests.post(url=url,data=data,headers=headers)
dic_obj=response.json()
#print(dic_obj)
fileName=word+'.json'
json.dump(dic_obj,fp=open(fileName,'w',encoding='utf-8'),ensure_ascii=False)