import scrapy
class Test01Item(scrapy.Item):
    bartitle = scrapy.Field()
    title = scrapy.Field()
    info = scrapy.Field()
