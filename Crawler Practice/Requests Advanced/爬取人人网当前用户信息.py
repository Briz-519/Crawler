# -*- coding : utf-8 -*-
# @Time : 8/11/2020 15:47
# @Author : Briz
# @File : 爬取人人网当前用户信息.py
# @headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.52"}
# @Software: PyCharm

import requests
from lxml import etree
from hashlib import md5

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.52"}
def getCodeText(imgPath,codeType):
    class Chaojiying_Client(object):

        def __init__(self, username, password, soft_id):
            self.username = username
            self.password = md5(password.encode("utf-8")).hexdigest()
            self.soft_id = soft_id
            self.base_params = {
                'user': self.username,
                'pass2': self.password,
                'softid': self.soft_id,
            }
            self.headers = {
                'Connection': 'Keep-Alive',
                'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
            }

        def PostPic(self, im, codetype):
            """
            im: 图片字节
            codetype: 题目类型 参考 http://www.chaojiying.com/price.html
            """
            params = {
                'codetype': codetype,
            }
            params.update(self.base_params)
            files = {'userfile': ('ccc.jpg', im)}
            r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, files=files,
                              headers=self.headers)
            return r.json()

        def ReportError(self, im_id):
            """
            im_id:报错题目的图片ID
            """
            params = {
                'id': im_id,
            }
            params.update(self.base_params)
            r = requests.post('http://upload.chaojiying.net/Upload/ReportError.php', data=params, headers=self.headers)
            return r.json()

    if __name__ == '__main__':
        chaojiying = Chaojiying_Client('Briz123456', '123456', '907088')  # 用户中心>>软件ID 生成一个替换 96001
        im = open(imgPath, 'rb').read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
        return chaojiying.PostPic(im, codeType)
session=requests.Session()
url="http://www.renren.com/SysHome.do"
page_text=requests.get(url=url,headers=headers).text
tree=etree.HTML(page_text)
img=tree.xpath('//*[@id="verifyPic_login"]/@src')[0]
img_data=requests.get(url=img,headers=headers).content
with open('../Auth Code/code.jpg', 'wb') as fp:
    fp.write(img_data)
code_text=getCodeText('code.jpg',1902)
code_result=code_text['pic_str']
print(code_text)
login_url="http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2020711913639"
data={
    'email': '15623178698',
    'icode': code_result,
    'origURL': 'http://www.renren.com/home',
    'domain': 'renren.com',
    'key_id': '1',
    'captcha_type': 'web_login',
    'password': '123456',
    'f': 'http%3A%2F%2Fwww.renren.com%2F974883992'
}
response=session.post(url=login_url,headers=headers,data=data)
login_text=response.text
print(response.status_code,"Login Successfully!")
detail_url="http://www.renren.com/974883992/profile"
detail_text=session.get(url=detail_url,headers=headers).text
with open('人人网用户详情.html', 'w', encoding='utf-8') as fp:
    fp.write(detail_text)