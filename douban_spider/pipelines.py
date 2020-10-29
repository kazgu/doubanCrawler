# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import douban_spider.config as cfg
class SpiderDB(object):  # 这里的类名要和setting中对应
    def __init__(self, host, port, dbname,colname, authdb=None, username=None, password=None):
        self.host = host
        self.port = port
        self.dbname = dbname
        self.authdb = authdb
        self.username = username
        self.password = password
        self.colname=colname

        # 建立数据库连接
        self.client = pymongo.MongoClient("mongodb://%s:%s/"%(self.host,self.port))
        if authdb:
            self.client = pymongo.MongoClient("mongodb://%s:%s@%s:%s/"%(self.username,self.password,self.host,self.port))

    def __get_client(self):
        """
        拿到数据库连接
        """
        if self.client and self.client.is_primary:
            pass
        else:
            # 重新建立连接
            self.client.close()
            self.client = pymongo.MongoClient("mongodb://%s:%s/"%(self.host,self.port))
            if self.authdb:
                self.client = pymongo.MongoClient("mongodb://%s:%s@%s:%s/"%(self.username,self.password,self.host,self.port))
        return self.client

    def insert_item(self, text_item):
        client = self.__get_client()
        db = client[self.dbname]
        coll = db[self.colname]
        coll.insert(dict(text_item))
    def get_item(self, text_item):
        client = self.__get_client()
        db = client[self.dbname]
        coll = db[self.colname]
        return coll.find_one(dict(text_item))

class DoubanSpiderPipeline:
    def process_item(self, item, spider):

        mongo_client = SpiderDB(cfg.db_host, cfg.db_port, cfg.db_name,cfg.colname,True,cfg.dbuser,cfg.dbpass)

        # 接口字典
        switcher = {
            'TextItem': mongo_client.insert_item,
            'GetItem': mongo_client.get_item
        }

        # 匹配对应集合的存储方法
        def __no_support_item():
            print('no supprt')
            pass

        fun = switcher.get(item.__class__.__name__, __no_support_item)
        fget = switcher.get('GetItem', __no_support_item)
        if not fget(item):
            fun(item)
        return item
