# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NewsItem(scrapy.Item):

    # url地址
    url = scrapy.Field()
    # 标题
    title = scrapy.Field()
    # 发布时间
    publish_date = scrapy.Field()
    # 来源
    source = scrapy.Field()
    # 正文
    article_text = scrapy.Field()
    
    
    