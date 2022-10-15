import scrapy
from..items import Test01Item
from w3lib.html import remove_tags
import requests
from . import testjson


class TestSpider(scrapy.Spider):
    name = 'test'
    start_urls = testjson.travel_spider()
    # start_urls = ['https://www.trip.com/travel-restrictions-covid-19/singapore-to-india']

    def parse(self, response):

        items = Test01Item()

        all_div_content = response.css('div.box-area-item ')

        bartitle = response.css('.bar-title::text').extract()
        items['bartitle'] = bartitle[0]
        # title = response.css('h3.box-area-title::text').extract()
        # info = response.css('div.box-area-content ::text').extract()
        # info = response.xpath("//div[@class='box-area-content']").extract()
        # info = [remove_tags(text) for text in response.xpath("//div[@class='box-area-content']").extract()]
        # summarytext = response.css('.summary-text::text').extract()
        # fontweightnormal = response.css('.font-weight-normal::text').extract()
        # itemcont = response.css('.item-content-bar::text').extract()

        # yield {'bartitle' : bartitle[0], 'title' : title[0:6], 'info' : info[0:6]}
        # items['summarytext'] = summarytext
        # items['fontweightnormal'] = fontweightnormal
        # items['item-content-bar'] = itemcont

        for content in all_div_content[0:6]:

            title = content.css('h3.box-area-title::text').extract()
            info = [remove_tags(text) for text in content.css('.box-area-content').extract()]
            # info = [remove_tags(text) for text in response.xpath("//div[@class='box-area-content']").extract()]
            # info = response.xpath("//div[@class='box-area-content']//text()").extract()

            items['title'] = title
            items['info'] = info

            yield items