# #!/usr/bin/env python
# # encoding: utf-8
# from pathlib import Path

# def is_Chinese(word):
#     for ch in word:
#         if not '\u4e00' <= ch <= '\u9fff':
#             return False
#     return True
# """ 初始的待爬队列 """
# # querys = [
# #     '一了百了+成语',
# #     '室内+客厅',
# #     '摆件+工艺品'
# # ]
# import re
# print('beginnnnnnn')
# import pymongo
# myclient = pymongo.MongoClient("mongodb://root:Hasanjan005@121.36.10.165:7027/")
# # mydb = myclient["baidu"]
# # mycol = mydb["Text"]

# # mydb2 = myclient["kazgu"]
# # mycol2 = mydb2["babelnet"]

# mydb = myclient["testDB"]
# mycol = mydb["words"]

# querys=[]
# ii=0
# # for x in mycol.find():
# #     try:
# #         # x={}
# #         # ww=re.split('[和并与而或]',w['word'])
# #         # # print(ww)
# #         # if len(ww)==2:
# #         #     x['word']=ww[0]
# #         #     x['Hypernym']=ww[1]
# #         if 'word' in x and x['word'] and is_Chinese(x['word']) and is_Chinese(x['Hypernym']) and (x['word']!=x['Hypernym']):
# #             query =x['word']+'+'+x['Hypernym']
# #             if not mycol2.find_one({'word':x['word'],'Hypernym':x['Hypernym']}):
# #                 del x['_id']
# #                 mycol2.insert_one(x)
# #                 querys.append(query)
# #                 ii+=1
# #         # if ii>100:
# #         #     break
# #     except:
# #         pass
# for c in mycol.find():
# #     for ss in c['tagging']:
#         # if int(ss['value'])!=-1:
#     querys.append(c['search_words'])
# print(len(querys),ii)
# # querys = []
# # with Path('./dataset.txt').open('r') as fr:
# #     for line in fr:
# #         l = line.split()
# #         query = l[0] + '+' + l[1]
# #         querys.append(query)

# # querys = ['嵇康+晋朝人']

""" 数据库相关"""
db_host = '0.0.0.0'
db_port = 27027
db_name = 'douban'
colname='collll'
dbuser='root'
dbpass='123456'
# 代理IP池？
PROXYPOOL = []