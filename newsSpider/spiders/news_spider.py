# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider
from newsSpider.userAgent import USER_AGENT_LIST as userAgent_list
import json, time, random
#from newsSpider.items import NewsUrlSpiderItem as newsItem
from newsSpider.items import NewsspiderItem as nsItem


class NewsSpiderSpider(RedisSpider):  # scrapy.Spider
    name = 'new1'
    allowed_domains = ['qq.com']
    redis_key = 'new1s:start_urls'

    def parse(self, response):
        # print('-----访问的url-------')
        # print(response.url)
        if response.body_as_unicode() != 'Access denied':

            # print('----1---进入parse-----------')
            # print(response.body_as_unicode())
            #item = newsItem()
            data = response.body_as_unicode()
            data_json = json.loads(data[9:len(data) - 1])
            user_agent = random.choice(userAgent_list)
            headers = {
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': user_agent
            }
            if data_json['response']['code'] == '0':
                for i in data_json['data']['article_info']:
                    url = i['url']
                    # item['url'] = url
                    print('子级url', url)
                    # yield item
                    yield scrapy.Request(url=url, callback=self.chil_url_content, headers=headers)
            else:
                print('该url今日没有值:', response.url)

        else:
            print('------拒绝连接-------')

    def chil_url_content(self, response):
        print('----2---进入parse-----------')
        item = nsItem()
        title = response.css('.qq_article div[class="hd"] h1::text').extract_first()
        newsType = response.css('div[class="a_Info"] span:nth-child(1)  a::text').extract_first()

        source = response.css('.a_source::text').extract_first()
        newsTime = response.css('.a_time::text').extract_first()
        content_list = response.css('.Cnt-Main-Article-QQ p[style="TEXT-INDENT:2em"]::text').extract()
        content = ''
        for i in content_list:
            content += i + '\t'
        img_url_list = response.css('.Cnt-Main-Article-QQ  img::attr(src)').extract()
        img_list = ''
        for i in img_url_list:
            img_list += 'http:' + i + '|'

        item['title'] = title
        item['newsType'] = newsType
        item['source'] = source
        item['newsTime'] = newsTime
        item['content'] = content
        item['img_list'] = img_list

        yield item
