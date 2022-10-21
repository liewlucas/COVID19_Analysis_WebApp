# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Test01Item(scrapy.Item):
    # define the fields for your item here like:
    bartitle = scrapy.Field()
    # summarytext = scrapy.Field()
    # fontweightnormal = scrapy.Field()
    title = scrapy.Field()
    info = scrapy.Field()
    # itemcont = scrapy.Field()
