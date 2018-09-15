# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NewsspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    newsType = scrapy.Field()
    source = scrapy.Field()
    newsTime = scrapy.Field()
    content = scrapy.Field()
    img_list = scrapy.Field()


#
# class NewsUrlSpiderItem(scrapy.Item):
#     url = scrapy.Field()
