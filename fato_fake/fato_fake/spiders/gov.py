# -*- coding: utf-8 -*-
import scrapy


class GovSpider(scrapy.Spider):
    name = 'gov'
    # caso precise limitar ou usar mais de um domínio 
    # allowed_domains = ['https://antigo.saude.gov.br/fakenews/?readmore_limit=200']
    start_urls = ['https://antigo.saude.gov.br/fakenews/?readmore_limit=200']

    def parse(self, response):
        # Conjunto de DIVs do target
        divs = response.xpath('//*[@id="adminForm"]/div[2]/div')
        
        # Para cada DIV pegamos os campos necessários
        for div in divs:
            link = div.xpath('.//h2/a') 
            title = link.xpath('./text()').extract_first()             
            content = div.xpath('.//p/text()').extract_first()             
            href = link.xpath('./@href').extract_first()
            img = div.xpath('.//img[contains(@class, "tileImage")]/@src').extract_first()
            my_datatime = div.xpath('.//li/text()').extract()
            _, date, hour, _ = my_datatime            
            yield {
                  'title': title,
                  'href': href,
                  'content': content,
                  'img': img,
                  'date': date,
                  'hour': hour
            }
        
        # Encontrando o botão de next do site para varrer todas as páginas
        next_page = response.xpath('//li[contains(@class, "pagination-next")]/a/@href').extract_first()
        
        # Caso encontre o botão next fazemos a chamada do parse passando a nova URL de pesquisa
        # Como o next_page retorna uma URL relativa e não a completa, precisamos concatenar com o nosso Domínio
        # antes de chamar o parse
        if next_page:
            yield scrapy.Request(url=f'https://antigo.saude.gov.br/{next_page}', callback=self.parse)
