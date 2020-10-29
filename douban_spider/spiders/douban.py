# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request


from douban_spider.items import TextItem

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    host = 'https://www.douban.com/group/692739/discussion?start={}'
    def start_requests(self):
        print('begin crawling...')
        # 这里应该是对每个字符串，生成一个url
        # for query in querys:
        start=19875
        plen=25
        # pages=[start-p*25 for p in  range(int(start/25))]
        pages=[start-p*25 for p in  range(int(start/25))]
        for page_num in pages:  # 暂时只爬三页，只有一页咋办？好像也没关系，可以过滤避免重爬
            url = self.host.format(page_num)
            print('当前爬取的页', url)
            # 在Request中用meta参数给response传递参数
            yield Request(url=url, callback=self.parse, dont_filter=True)
    def parse(self, response):
        print('parsing........')
        data_title=response.xpath('//td[@class="title"]/a/text()').extract()
        data_link=response.xpath('//td[@class="title"]/a/@href').extract()
        # print(datas)
        for title,link in zip(data_title,data_link):
            print(title,link)
            link=link.strip()
            title=title.strip()
            yield Request(url=link,meta={'title': title}, callback=self.subparse, dont_filter=True)
    def subparse(self, response):
        text_item = TextItem()
        print('sub parsing........')
        dtitle=response.meta.get('title')
        duser=response.xpath('//div[@class="topic-doc"]/h3//span[1]/a/text()')[0].extract()
        ddate=response.xpath('//div[@class="topic-doc"]/h3/span[2]/text()')[0].extract()
        ps=response.xpath('//div[@class="topic-doc"]/div/div/div/p/text()')
        # print(ps)
        dcontent=''
        for p in ps:
            dcontent+=p.extract()
        text_item.init_item(title=dtitle,content=dcontent,duser=duser,ddate=ddate)
        return text_item