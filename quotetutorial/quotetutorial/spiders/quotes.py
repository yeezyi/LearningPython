# -*- coding: utf-8 -*-
import scrapy
from quotetutorial.items import QuotesItem

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        quotes = response.css('.quote')
        for quote in quotes:
            item = QuotesItem()
            text = quote.css('.text::text').extract_first()
            author = quote.css('.author::text').extract_first()
            tags = quote.css('.tags .tag::text').extract()
            item['text'] = text
            item['author'] = author
            item['tags'] = tags
            # yield item
        next = response.css('.pager .next a::attr(href)').extract_first()
        url = response.urljoin(next)
        print('get NEXT', url)
        yield scrapy.Request(url, callback=self.parse)
