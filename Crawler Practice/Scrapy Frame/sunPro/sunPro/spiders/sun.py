import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from sunPro.items import SunproItem

class SunSpider(CrawlSpider):
    name = 'sun'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://wz.sun0769.com/political/index/politicsNewest?id=1&page=1']
    Link=LinkExtractor(allow=r'id=1&page=\d+')
    rules = (
        Rule(Link, callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        li_list=response.xpath('/html/body/div[2]/div[3]/ul[2]/li')
        for li in li_list:
            new_num=li.xpath('./span[1]/text()').extract_first()
            new_title=li.xpath('./span[3]/a/text()').extract_first()
            item=SunproItem()
            item['title']=new_title
            item['new_num']=new_num
            yield item
