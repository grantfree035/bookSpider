
import os
import scrapy
from bookBNTC.items import BookImages
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.selector import Selector

class BookImagesSpider (scrapy.Spider):
    name = "bookImagePages"
    allowed_domain = "http://online.vitalsource.com/"
    start_urls = ["http://online.vitalsource.com/#/books/9781465246738/pages/110684433"]
    num = 110684433
    maxNum = 110684727
    '''
    while num <= maxNum:
        start_urls.append("http://online.vitalsource.com/#/books/9781465246738/pages/" + str(num))
        num += 1
    '''
    
    def parse(self, response):
        sel = Selector(response)
        items = []

        item = BookImages()
        item['image_url'] = sel.xpath('//img[@class="page"]/@src').extract()
        
        items.append(item)
        return item
