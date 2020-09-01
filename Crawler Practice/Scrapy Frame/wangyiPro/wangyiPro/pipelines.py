# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class WangyiproPipeline:
    fp=None
    def open_spider(self,spider):
        # 重写父类的一个方法：该方法只在开始爬虫的时候被调用一次
        print("Crawler Start...")
        self.fp=open('./wangyi.txt','w',encoding='utf-8')
        # 专门用来处理item类型对象
        # 该方法可以接收爬虫文件提交过来的item对象
        # 该方法没接收到一个item就会被调用一次
    def process_item(self, item, spider):
        title=item['title']
        content=item['content']
        self.fp.write(title+':'+content+'\n')
        return item
    def close_spider(self,spider):
        print('Crawler Over!')
        self.fp.close()
