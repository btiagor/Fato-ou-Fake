# -*- coding: utf-8 -*-
import scrapy


class AosfatosSpider(scrapy.Spider):
    name = 'aosfatos'    
    # URL inicial da pesquisa
    start_urls = ['https://www.aosfatos.org/noticias']

    # Alterando o tempo entre as requisições
    custom_settings = {
        'DOWNLOAD_DELAY': 1.5,
    }
    
    
    def parse(self, response):
        # Lista âncoras encontrados na start_urls
        hrefs = response.xpath('/html/body/main/section/div/section/div/a')        
        
        # Para cada âncora pegamos o atributo href e fazemos uma requisição passando o link encontrado
        for mat in hrefs:               
            url=f'https://www.aosfatos.org{mat.xpath("./@href").extract_first()}'
            # self.log(url)     
            yield scrapy.Request(url=url, callback=self.parse_detail)
            
        # Encontrando o botão de next do site para varrer todas as páginas
        next_page = response.xpath('/html/body/main/section/div/div[2]/span/a[last()]/@href').extract_first() # precisa do domínio        
        # self.log(next_page)
        
        # Caso encontre o botão next fazemos a chamada do parse passando a nova URL de pesquisa
        # Como o next_page retorna uma URL relativa e não a completa, precisamos concatenar com o nosso Domínio
        # antes de chamar o parse
        if next_page:
            yield scrapy.Request(url=f'https://www.aosfatos.org/noticias{next_page}', callback=self.parse)


    def parse_detail(self, response):                
        title = response.xpath('//h1/text()').extract_first()
        author = response.xpath('//p[@class="author"]/text()').extract_first()
        date = response.xpath('//p[@class="author"]/following-sibling::p/text()').extract_first()
        img = response.xpath('//img[@data-image-id]/@src').extract_first()
        content = response.xpath('/html/body/main/section/article/p[1]/text()').extract()
        font = response.xpath('//p[contains(text(), "Referências:")]/following-sibling::p/a/@href').extract()
        yield {
                  'title': title,
                  'href': font,
                  'content': content,
                  'img': img,
                  'date': date,
                  'author': author
            }
