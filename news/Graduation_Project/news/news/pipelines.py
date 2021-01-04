# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv


class NewsPipeline:
    
    def __init__(self):
        # self.file = open('../file/news1.csv', 'w', encoding='utf-8',newline='')
        self.file = open('../../../data/news.csv', 'w', encoding='utf-8',newline='')
        self.csvwriter = csv.writer(self.file)
        self.csvwriter.writerow(['url', 'title', 'publish_date', 'source', 'article_text'])
    
    def process_item(self, item, spider):
        self.csvwriter.writerow([item["url"], item["title"], item["publish_date"], item["source"], item["article_text"]])
        return item
    
    def close_spider(self, spider):
        self.file.close()
        
