# -*- coding: utf-8 -*-
import banco as bd
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class FatoFakePipeline(object):
    def process_item(self, item, spider):
        query = """INSERT INTO fatos 
                        (FAT_TITLE, FAT_URL ,FAT_IMG ,FAT_DATE ,FAT_HOUR)
                        VALUES(:title, :href, :img, :date, :hour)"""
        bd.crud(query, item)
        return item
    
        
    def open_spider(self, spider):
        bd.create_database()
        
        