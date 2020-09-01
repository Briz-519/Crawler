# -*- coding : utf-8 -*-
# @Time : 8/16/2020 14:38
# @Author : Briz
# @File : iframe处理和动作链.py
# @headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.52"}
# @Software: PyCharm

from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains

bro=webdriver.Edge(executable_path='msedgedriver.exe')
bro.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
bro.switch_to.frame('iframeResult')
div=bro.find_element_by_id('draggable')
act=ActionChains(bro)
act.click_and_hold(div)
for i in range(5):
    act.move_by_offset(17,0).perform()
    sleep(0.3)
act.release()
bro.quit()















