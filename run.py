import redis
import os
import datetime
import time


def run():
    now_time = datetime.datetime.now().strftime('%Y-%m-%d')
    t = time.time()
    times = str(round(t * 1000))
    type_list = ['news', 'ent', 'sports', 'finance', 'tech', 'games', 'auto', 'edu', 'house']
    start_url = []
    for types in type_list:
        start_url.append(
            'http://roll.news.qq.com/interface/cpcroll.php?callback=rollback&site=%s&mode=1&cata=&date=%s&page=1&_=%s' % (
                types, now_time, times))

    r = redis.StrictRedis(host='127.0.0.1', port=6379, password='123456')

    r.delete('new1s:start_urls')


    for url in start_url:
        r.lpush('new1s:start_urls', url)

        result = r.smembers('redisspider:start_url')
        if result is not 0:
            print('加入start_urls成功')
    r.connection_pool.disconnect()




if __name__ == '__main__':
    while True:
        run()
        os.system("scrapy crawl new1")
        time.sleep(1800)
