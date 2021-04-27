# -*- coding: utf-8 -*-
import banco as bd
import re
dict_month = {
    'janeiro': '01','fevereiro': '02', 'março': '03', 'abril': '04', 'maio': '05', 'junho': '06',
    'julho': '07','agosto': '08', 'setembro': '09', 'outubro': '10', 'novembro': '11', 'dezembro': '12',    
    }

"""
    classe para cada spyder onde faz o processamento dos itens coletados
"""
class GovPipeline(object):
    
    def process_item(self, item, spider):
        title = item['title']
        url = item['url']
        content = item['content']
        img = item['img']
        date = item['date'].strip()
        day = date[:2]
        month = date[3:5]
        year = date[6:]
        hour = item['hour']
        
        query = f"""INSERT INTO gov 
                        (GOV_TITLE, GOV_URL, GOV_CONTENT, GOV_IMG, GOV_DATE, GOV_HOUR, GOV_DAY, GOV_MONTH, GOV_YEAR)
                        VALUES("{title}", "{url}", "{content}", "{img}", "{date}", "{hour}", "{day}", "{month}", "{year}")"""
        
        # Checa na base se o elemento existe caso contrário insere na tabela
        data_exist = bd.crud(f'select gov_id from gov where gov_title = "{title}" and gov_url = "{url}" and gov_content = "{content}" and gov_img = "{img}" and gov_date = "{date}" and gov_hour = "{hour}" and gov_day = "{day}" and gov_month = "{month}" and gov_year = "{year}"', 'gov.db')
        if not data_exist:
            bd.crud(query, 'gov.db')
        return item
    
    
    # Abre conexão com o banco
    def open_spider(self, spider):
        bd.create_table_gov()

class AosFatosPipeline(object):
    def process_item(self, item, spider):
        title = ''.join(item['title']).replace('\n', '').strip() if item['title'] != 'None' else 'None'
        fonts = ';'.join(item['fonts']) if item['fonts'] != 'None' else 'None'
        # content = ''.join(item['content'])
        content = ''.join(item['content']) if item['content'] != 'None' else 'None'
        img = item['img'] if item['img'] != 'None' else 'None'
        date = re.sub(r'\s+', ' ', item['date'].replace('\n', '').strip())
        day, month, year, hour = 'None'
        if date:
            d = date.split(' de ')
            day = d[0]
            month = dict_month[d[1]]
            year = re.findall(r'\d{4}', d[2])[0]
            hour = re.findall(r'\d+h\d+', d[2])[0]        
        author = item['author'][4:].replace(', ', ';').replace(' e ', ';') if item['author'] != 'None' else 'None'
        url = item['url']
               
        
        query = f"""INSERT INTO fatos 
                        (FAT_TITLE, FAT_FONTS , FAT_CONTENT, FAT_IMG ,FAT_DATE ,FAT_AUTHOR, FAT_URL, FAT_DAY, FAT_MONTH, FAT_YEAR, FAT_HOUR)
                        VALUES("{title}", "{fonts}", "{content}", "{img}", "{date}", "{author}", "{url}", "{day}", "{month}", "{year}", "{hour}")
                        """
        
        # Checa na base se o elemento existe caso contrário insere na tabela                
        data_exist = bd.crud(
            f"""select fat_id from fatos 
            where fat_title = "{title}" and fat_fonts = "{fonts}" and fat_content = "{content}" 
            and fat_img = "{img}" and fat_date = "{date}" and fat_author = "{author}" and fat_url = "{url}"
            """)
        if not data_exist:
            bd.crud(query)
        return item   
    
        
    # Abre conexão com o banco    
    def open_spider(self, spider):
        bd.create_table_fatos()        
        