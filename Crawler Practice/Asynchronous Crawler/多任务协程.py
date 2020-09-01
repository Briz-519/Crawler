# -*- coding : utf-8 -*-
# @Time : 8/15/2020 12:27
# @Author : Briz
# @File : 多任务协程.py
# @headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.52"}
# @Software: PyCharm

import asyncio
import time

async def request(url):
    print('Downloading...',url)
    # time.sleep(3)
    #time.sleep()为同步模块代码无法实现异步
    await asyncio.sleep(2)
    #在asyncio中遇到阻塞操作需要使用await手动挂起
    print('Download Successfully!')

start=time.time()
urls=[
    'Briz-519.GitHub.io',
    'www.baidu.com',
    'www.sogou.com'
]
tasks=[]
for url in urls:
    c=request(url)
    task=asyncio.ensure_future(c)
    tasks.append(task)
loop=asyncio.get_event_loop()
#需要将任务列表封装到wait中
loop.run_until_complete(asyncio.wait(tasks))
print(time.time()-start)