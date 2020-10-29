# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html


from scrapy import Item, Field

class TextItem(Item):
    title = Field()
    ddate=Field()
    duser=Field()
    content=Field()

    def init_item(self, title, content,duser,ddate):
        self['title'] = title
        self['content']=content
        self['duser']=duser
        self['ddate']=ddate