# NewSpider
本篇文章为scrapy-redis的实例应用，源码已经上传到github:

使用到了：
python 3.x
redis
scrapy-redis
pymysql
Redis-Desktop-Manager(redis可视化工具)
工具安装问题网上有许多，我就不一一赘述了。

这个实例主要是爬取腾讯滚动新闻模块的数据，做了去重，自增量，可以分布爬取，定时关闭爬虫；一键启动，每半个小时自动获取一次数据。（若这些还不满足，可以继续在run方法中新构一个redis-key，保存在redis中，然后做一个slave接收这个key里的url）
如果想做一个时实咨询的app或者网站的话，拿这个实例直接修改下就OK了。
