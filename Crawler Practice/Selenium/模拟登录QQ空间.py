# -*- coding : utf-8 -*-
# @Time : 8/16/2020 15:02
# @Author : Briz
# @File : 模拟登录QQ空间.py
# @headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.52"}
# @Software: PyCharm

from selenium import webdriver
from time import sleep

bro=webdriver.Edge(executable_path='msedgedriver.exe')
bro.get('https://qzone.qq.com/')
bro.switch_to.frame('login_frame')
a_tag=bro.find_element_by_id('switcher_plogin')
a_tag.click()
u_tag=bro.find_element_by_id('u')
sleep(1)
u_tag.send_keys('')#Input your QQnum

p_tag=bro.find_element_by_id('p')
sleep(1)
p_tag.send_keys('')#Input your password

login_tag=bro.find_element_by_id('login_button')
sleep(1)
login_tag.click()

sleep(3)
bro.quit()












