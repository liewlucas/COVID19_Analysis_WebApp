import scrapy
from..items import Test01Item
from w3lib.html import remove_tags
import requests
from . import testjson


class TestSpider(scrapy.Spider):
    name = 'test'
    start_urls = testjson.travel_spider()
    def parse(self, response):
        items = Test01Item()
        all_div_content = response.css('div.box-area-item ')
        bartitle = response.css('.bar-title::text').extract()
        items['bartitle'] = bartitle[0]
        for content in all_div_content[0:6]:
            title = content.css('h3.box-area-title::text').extract()
            info = [remove_tags(text) for text in content.css('.box-area-content').extract()]
            items['title'] = title
            items['info'] = info
            yield items
