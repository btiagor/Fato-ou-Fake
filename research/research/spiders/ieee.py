# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import scrapy


class IeeeSpider(scrapy.Spider):
    name = 'ieee'
    allowed_domains = ['www.ieee.org', 'https://conferences.ieee.org']
    start_urls = ['https://conferences.ieee.org/conferences_events/conferences/search?q=*']

    rules = (
        Rule(
            LinkExtractor(allow='/conferences_events/conferences/search')
        ),
        Rule(
            LinkExtractor(
                allow='/conferences_events/conferences/conferencedetails/'
                ), callback='parse_conference'
        )
    )
    
    def parse_conference(self, response):
        self.log(response.xpath('//title/text()'),extract_first())
