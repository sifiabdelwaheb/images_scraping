# -*- coding: utf-8 -*-
import scrapy
from images_scraping.items import ImagesScrapingItem
from scrapy.loader import ItemLoader


class JumiaScraperSpider(scrapy.Spider):
    name = 'jumia_scraper'
    allowed_domains = ['www.jumia.com.tn']
    start_urls = ['https://https://www.jumia.com.tn/telephone-tablette']

    start_urls = [
        'https://www.jumia.com.tn/ecouteur-jaune-cliptec-mpg7925.html']

    def parse(self, response):
        for product in response.xpath("//div[@class='sldr _img _prod -rad4 -oh -mbs']"):
            loader = ItemLoader(item=ImagesScrapingItem(), selector=product)
            relative_url = product.xpath(
                ".//a[@class='itm']/@href").extract_first()
            absolute_url = response.urljoin(relative_url)
            loader.add_value('image_urls', absolute_url)

            # loader.add_xpath(
            #   'book_name', ".//div/h2[@class='h3 product-title']/a/text()")
            yield loader.load_item()
