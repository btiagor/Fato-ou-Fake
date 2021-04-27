# -*- coding: utf-8 -*-
from scrapy.spiders import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor


class AosfatosSpider(CrawlSpider):
    name = 'aosfatos'
    # Domnínio do site
    allowed_domains = ['aosfatos.org']
    # URL inicial para pesquisa
    start_urls = ['https://www.aosfatos.org/noticias']

    # Alterando o tempo entre as requisições
    custom_settings = {
        'DOWNLOAD_DELAY': 1.5,
    }
    
    # Conjunto de regras
    rules = (        
        Rule(LinkExtractor(allow='noticias'), callback='parse_news', follow=True),
    )

    def parse_news(self, response):
        # self.log(response.xpath('//title/text()').extract_first())
        # Retorno da URL
        yield {'url': response.url}
