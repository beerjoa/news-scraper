# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NavernewsItem(scrapy.Item):
    title = scrapy.Field()
    href = scrapy.Field()
    date = scrapy.Field()
    content = scrapy.Field()
    newsfrom = scrapy.Field()
    # company = scrapy.Field()
