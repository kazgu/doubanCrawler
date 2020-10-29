# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import random

from scrapy import signals

from douban_spider.user_agents import agents
from douban_spider.ip_pool import ip_queue


class UserAgentMiddleware(object):
    """ 换User-Agent """
    def process_request(self, request, spider):
        agent = random.choice(agents)
        request.headers["User-Agent"] = agent


class ProxyMiddleware(object):
    def __init__(self):
        self.ip_lists = ip_queue("douban_spider/ips.txt")    # 读取存放代理IP的文件
        self.ip_pools = self.ip_lists.find_proxy()

    def process_request(self, request, spider):
        ip = random.choice(self.ip_pools)   # 随机选取IP
        print('***********current ip**************: {}'.format(ip))
        request.meta['proxy'] = 'http://{}'.format(ip)

