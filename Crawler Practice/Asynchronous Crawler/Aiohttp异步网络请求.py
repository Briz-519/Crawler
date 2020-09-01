# -*- coding : utf-8 -*-
# @Time : 8/15/2020 12:56
# @Author : Briz
# @File : Aiohttp异步网络请求.py
# @headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.52"}
# @Software: PyCharm

import requests
import asyncio
import time
import aiohttp

start=time.time()
urls=[
    'http://127.0.0.1:5000/bobo',
    'http://127.0.0.1:5000/jay',
    'http://127.0.0.1:5000/tom'
]
async def get_page(url):
    print('Downloading...',url)
    async with aiohttp.ClientSession() as session:
        async with await session.get(url=url) as response:
            page_text=await response.text()
    print('Download Successfully!',page_text)

tasks=[]
for url in urls:
    c=get_page(url)
    task=asyncio.ensure_future(c)
    tasks.append(task)

loop=asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
print(time.time()-start)







