import scrapy
from QiuShiPro.items import QiushiproItem

class QiushibaikeSpider(scrapy.Spider):
    name = 'qiushibaike'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.qiushibaike.com/text/']

    # def parse(self, response):
    #     all_data=[]
    #     div_list=response.xpath('//*[@class="col1 old-style-col1"]/div')
    #     for div in div_list:
    #         # xpath返回的是列表，但是列表元素一定是Selector类型的对象
    #         #extract可以将Selector对象中data参数存储的字符串提取出来
    #         author=div.xpath('./div[1]/a[2]/h2/text()')[0].extract()
    #         content=div.xpath('./a[1]/div/span//text()').extract()
    #         # 列表调用了extract之后，则表示将列表中每一个Selector对象中data对应的字符串提取了出来
    #         content=''.join(content)
    #         dic={
    #            'Author':author,
    #            'Content':content
    #         }
    #         all_data.append(dic)
    #     return all_data
    def parse(self, response):
        div_list=response.xpath('//*[@class="col1 old-style-col1"]/div')
        for div in div_list:
            # xpath返回的是列表，但是列表元素一定是Selector类型的对象
            #extract可以将Selector对象中data参数存储的字符串提取出来
            #存在匿名用户的可能而匿名用户的用户名存储在span标签内，因此使用管道符号进行合并
            author=div.xpath('./div[1]/a[2]/h2/text() |./div[1]/span/h2/text()')[0].extract()
            content=div.xpath('./a[1]/div/span//text()').extract()
            # 列表调用了extract之后，则表示将列表中每一个Selector对象中data对应的字符串提取了出来
            content=''.join(content)
            item=QiushiproItem()
            item['author']=author
            item['content']=content
            #将item提交到管道
            yield item
