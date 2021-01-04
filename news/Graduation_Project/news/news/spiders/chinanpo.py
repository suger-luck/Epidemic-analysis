import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from pprint import pprint
from news.items import NewsItem

class ChinanpoSpider(CrawlSpider):
    name = 'chinanpo'
    allowed_domains = ['chinanpo.gov.cn']
    # start_urls = ['http://www.chinanpo.gov.cn/pageindex.html']
    start_urls = ['http://www.chinanpo.gov.cn/1944/128010/index.html']
    # start_urls = ['http://www.chinanpo.gov.cn/1944/124117/nextindex.html']
    rules = (
        # 下一页的url地址
        # Rule(LinkExtractor(allow=r'/1944/\d+/index.html'), follow=True),
        
        # 每一页中连接的url地址
        Rule(LinkExtractor(allow=r'/1944/\d+/nextindex.html'), callback='parse_item', follow=True),
        # Rule(LinkExtractor(restrict_xpaths=("//li[@class='word-22 bscx-li-11']//a[2]")),callback='parse_item', follow=True)
    )
    
    def parse_item(self, response):
        item = NewsItem()
        # print(response.url)
        # print(response.text)
        
        # url
        item["url"] = response.url
        
        # 标题
        item["title"] = response.xpath("//*[@id='fontinfo']/p[2]//text()").extract()
        item["title"] = "".join(item["title"]).replace('\r\n', '').replace("\xa0", "").replace("\t", "")
        if item["title"] == "":
            item["title"] = response.xpath("//*[@id='fontinfo']/p[3]//text()").extract()
            item["title"] = "".join(item["title"]).replace('\r\n', '').replace("\xa0", "").replace("\t", "")
        
        # 来源
        source_text = response.xpath("//*[@id='fontinfo']/p[last()]//text()").extract_first()
        print(source_text)
        source_text = response.xpath("//*[@id='fontinfo']//p[last()-1]//text()").extract_first() if source_text is None else source_text
        print("*"*10)
        print(source_text)
        
        item["source"] = source_text[3:]
        
        # 发布时间
        item["publish_date"] = response.xpath("//li[@class='word-7 bscx-li-4']/strong/text()").extract_first()
        item["publish_date"] = item["publish_date"].replace("发布时间：","")
        print(item)
        print('*'*50)
        # 正文
        text_list = response.xpath("//*[@id='fontinfo']//text()").extract()
        print(text_list)
        item["article_text"] = "".join(text_list).replace('\r\n', '').replace("\xa0", "").replace("\t","").replace(source_text,"").replace(item["title"],"")
        # pprint(item)
        return item
