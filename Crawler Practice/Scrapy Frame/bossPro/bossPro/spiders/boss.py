import scrapy
#from bossPro.item import BossproItem

class BossSpider(scrapy.Spider):
    name = 'boss'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.zhipin.com/job_detail/?query=python&city=100010000&industry=&position=']

    # def parse_detail(self,resopnse):
    #     job_desc=resopnse.xpath('//*[@id="main"]/div[3]/div/div[2]/div[2]/div[1]/div//text()')
    #     job_desc=''.join(job_desc)
    #     print(job_desc)
    def parse(self, response):
        li_list=response.xpath('//*[@id="main"]/div/div[2]/ul')
        for li in li_list:
            job_name=li.xpath('.//div[@class="info-primary"]/div[1]/div/div[1]/span[1]/a/text()').extract_first()
            print(job_name)
            detail_url='https://www.zhipin.com'+li.xpath('.//div[@class="info-primary"]/div[1]/div/div[1]/span[1]/a/@href').extract_first()
            yield scrapy.Request(detail_url,callback=self.parse_detail)