# -*- coding: utf-8 -*-
import banco as bd


"""
    classe para cada spyder onde faz o processamento dos itens coletados
"""
class GovPipeline(object):
    def process_item(self, item, spider):
        query = """INSERT INTO gov 
                        (FAT_TITLE, FAT_URL ,FAT_IMG ,FAT_DATE ,FAT_HOUR)
                        VALUES(:title, :href, :img, :date, :hour)"""
        
        # Checa na base se o elemento existe caso contrário insere na tabela
        data_exist = crud('select fat_id from gov where fat_title = :title and fat_url = :href and fat_img = :img and fat_date = :date and fat_hour = :hour', item)
        if not data_exist:
            bd.crud(query, item)
        return item
    
    
    # Abre conexão com o banco
    def open_spider(self, spider):
        bd.create_database_gov()

class AosFatosPipeline(object):
    def process_item(self, item, spider):
        query = """INSERT INTO fatos 
                        (FAT_TITLE, FAT_URL ,FAT_IMG ,FAT_DATE ,FAT_HOUR)
                        VALUES(:title, :href, :img, :date, :hour)"""
        
        # Checa na base se o elemento existe caso contrário insere na tabela
        data_exist = crud('select fat_id from fatos where fat_title = :title and fat_url = :href and fat_img = :img and fat_date = :date and fat_hour = :hour', item)
        if not data_exist:
            bd.crud(query, item)
        return item
    
        
    # Abre conexão com o banco
    def open_spider(self, spider):
        bd.create_database_fatos()        
        