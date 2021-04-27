# -*- coding: utf-8 -*-
from scrapy.spiders import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor


class GovSpider(CrawlSpider):
    name = 'gov'
    allowed_domains = ['antigo.saude.gov.br']
    start_urls = ['https://antigo.saude.gov.br/fakenews/']
    
    custom_settings = {
        'DOWNLOAD_DELAY': 1.5,
    }
    
    rules = (                        
        Rule(LinkExtractor(allow='fakenews'), callback='parse_news', follow=True),
    )

    def parse_news(self, response):
        yield {'url': response.url}
    
