import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from myspider.items import DoubanItem
from scrapy.loader import ItemLoader


class MySpider(CrawlSpider):
    name = 'douban.com'
    allowed_domains = ['douban.com']
    start_urls = ['https://www.douban.com/group/jianshen/discussion?start=0']

    rules = (
        Rule(LinkExtractor(allow=('discussion\?start=0')),follow=False,callback='parse_list'),
        Rule(LinkExtractor(allow=('discussion\?start=[0-9]*'), restrict_xpaths=("//span[@class='next']/a")),follow=True,callback='parse_list'),
        # Rule(LinkExtractor(allow=('/group/topic/[0-9]+', )), callback='parse_item'),
    )

    def parse_list(self, response):
        for le in response.xpath('//table[@class="olt"]//tr[position()>1]'):
            loader = ItemLoader(DoubanItem(),le)
            loader.add_xpath('respond_num','td[3]/text()')
            loader.add_xpath('url','td[@class="title"]/a/@href')
            item = loader.load_item()
            yield scrapy.Request(url=item['url'],callback=self.parse_item,meta={'item':item})


    def parse_item(self, response):
        item = response.meta['item']
        loader = ItemLoader(item,response=response)
        loader.add_xpath('title','//h1/text()')
        loader.add_xpath('content','//div[@class="topic-content"]/*/text()')

        return loader.load_item()