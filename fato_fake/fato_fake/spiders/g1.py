# -*- coding: utf-8 -*-
import scrapy


class G1Spider(scrapy.Spider):
    name = 'g1'
    # caso precise limitar ou usar mais de um domínio 
    # allowed_domains = ['https://g1.globo.com/fato-ou-fake/coronavirus/']
    start_urls = ['https://g1.globo.com/fato-ou-fake/coronavirus//']

    def parse(self, response):
        pass
