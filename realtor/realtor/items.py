# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RealtorItem(scrapy.Item):
    title=scraped.Field()
    streetadd=scraped.Field()
    area=scraped.Field()
    overview=scraped.Field()
    
