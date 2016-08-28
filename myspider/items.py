# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Field,Item
from scrapy.loader.processors import TakeFirst,Join

class DoubanItem(scrapy.Item):
    url = Field(output_processor=TakeFirst())
    respond_num = Field(output_processor=TakeFirst())
    title=Field(output_processor=TakeFirst())
    name =Field(output_processor=TakeFirst())
    content=Field(output_processor=Join())
    comment = Field()
