# -*- coding : utf-8 -*-
# @Time : 8/15/2020 16:38
# @Author : Briz
# @File : Selenium基础用法.py
# @headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.52"}
# @Software: PyCharm

from selenium import webdriver
from time import sleep

bro=webdriver.Edge(executable_path=r'msedgedriver.exe')
bro.get('https://www.taobao.com/')
search=bro.find_element_by_id('q')
search.send_keys('mihoyo')
btn=bro.find_element_by_css_selector('.btn-search')
btn.click()
bro.get('https://www.baidu.com')
sleep(2)
bro.back()
sleep(2)
bro.forward()
sleep(5)
bro.quit()












