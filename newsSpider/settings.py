# -*- coding: utf-8 -*-

# Scrapy settings for newsSpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import random
from newsSpider.userAgent import USER_AGENT_LIST

BOT_NAME = 'newsSpider'

SPIDER_MODULES = ['newsSpider.spiders']
NEWSPIDER_MODULE = 'newsSpider.spiders'

ROBOTSTXT_OBEY = False


CONCURRENT_REQUESTS = 30

DOWNLOAD_DELAY = 0.25

DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Referer': 'http://news.qq.com/articleList/rolls/',
    'Upgrade-Insecure-Requests': '1',
    'User_Agent': random.choice(USER_AGENT_LIST)
}

EXTENSIONS = {
    'newsSpider.extensions.RedisSpiderSmartIdleClosedExensions': 500,
}

ITEM_PIPELINES = {
    'newsSpider.pipelines.NewsspiderPipeline': 300,
    'scrapy_redis.pipelines.RedisPipeline': 400

}

DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
SCHEDULER_PERSIST = True
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderPriorityQueue'
REDIS_URL = None
REDIS_HOST = '127.0.0.1'
REDIS_PORT = '6379'
REDIS_PARAMS = {
    'password': '123456',
}

# SCHEDULER_QUEUE_KEY = '%(spider)s:requests'  # 调度器中请求存放在redis中的key
# SCHEDULER_SERIALIZER = "scrapy_redis.picklecompat"  # 对保存到redis中的数据进行序列化，默认使用pickle
#
# SCHEDULER_FLUSH_ON_START = False  # 是否在开始之前清空 调度器和去重记录，True=清空，False=不清空
# # SCHEDULER_IDLE_BEFORE_CLOSE = 10  # 去调度器中获取数据时，如果为空，最多等待时间（最后没数据，未获取到）。
# SCHEDULER_DUPEFILTER_KEY = '%(spider)s:dupefilter'  # 去重规则，在redis中保存时对应的key  chouti:dupefilter
# SCHEDULER_DUPEFILTER_CLASS = 'scrapy_redis.dupefilter.RFPDupeFilter'  # 去重规则对应处理的类
# DUPEFILTER_DEBUG = False

MYEXT_ENABLED = True  # 开启扩展
IDLE_NUMBER = 10  # 配置空闲持续时间单位为 10个 ，一个时间单位为5s

#如果为True，则使用redis的'spop'进行操作。
#如果需要避免起始网址列表出现重复，这个选项非常有用。开启此选项urls必须通过sadd添加，否则会出现类型错误。
#REDIS_START_URLS_AS_SET = True