# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql


class NewsspiderPipeline(object):
    comments = []

    def open_spider(self, spider):
        self.conn = pymysql.connect(host="localhost", user="root", passwd="Cs123456.", db="news", charset="utf8")
        self.cursor = self.conn.cursor()



    def process_item(self, item, spider):
        self.comments.append(
            [item['title'], item['newsType'], item['source'], item['newsTime'], item['content'], item['img_list']])
        if len(self.comments) == 1:
            self.insert_to_sql(self.comments)
            # 清空缓冲区
            self.comments.clear()
        return item

    def close_spider(self, spider):
        # print( "closing spider,last commit", len(self.comments))
        self.insert_to_sql(self.comments)
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

    def insert_to_sql(self, data):
        try:
            sql = "insert into news_info (title,newsType,source,newsTime,content,img_list) values(%s, %s,%s,%s,%s,%s)"
            # print(data)
            self.cursor.executemany(sql, data)
            self.conn.commit()
        except:
            print('数据插入有误。。')
            self.conn.rollback()
