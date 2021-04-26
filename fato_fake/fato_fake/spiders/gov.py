# -*- coding: utf-8 -*-
import scrapy


class GovSpider(scrapy.Spider):
    name = 'gov'
    # caso precise limitar ou usar mais de um domínio 
    # allowed_domains = ['https://antigo.saude.gov.br/fakenews/?readmore_limit=200']
    start_urls = ['https://antigo.saude.gov.br/fakenews/?readmore_limit=200']

    def parse(self, response):
        divs = response.xpath('//*[@id="adminForm"]/div[2]/div')
        
        for div in divs:
            link = div.xpath('.//h2/a') 
            title = link.xpath('./text()').extract_first() 
            # print(title) 
            content = div.xpath('.//p/text()').extract_first() 
            # print(content)
            href = link.xpath('./@href').extract_first()
            img = div.xpath('.//img[contains(@class, "tileImage")]/@src').extract_first()
            my_datatime = div.xpath('.//li/text()').extract()
            _, date, hour, _ = my_datatime
            # print(date, hour)
            # print(my_datatime)
            yield {
                  'title': title,
                  'href': href,
                  'content': content,
                  'img': img,
                  'date': date,
                  'hour': hour
            }
        btn_proximo = response.xpath('//li[contains(@class, "pagination-next")]/a/@href').extract_first()
        # print('AQUIIIIIIIIIIIIIIIIII ',btn_proximo)
        if btn_proximo:
            yield scrapy.Request(url=f'https://antigo.saude.gov.br/{btn_proximo}', callback=self.parse)
