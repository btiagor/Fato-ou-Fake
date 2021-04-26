# -*- coding: utf-8 -*-
import sqlite3
db = 'fato.db'


# Função que abre a conexão
def open_conection():    
    conn = sqlite3.connect(db)
    return conn


# Função que fecha a conexão
def close_conection(conn):
    conn.close()

    
# Criando tabela para spyder aosfatos
def create_database_fatos():        
    my_conn = open_conection()
    if crud('SELECT NAME FROM SQLITE_MASTER WHERE TYPE = "table" AND NAME = "fatos"'):        
        print('TABELA JÁ EXISTE.')
    else:
        my_conn.execute(
            """
            CREATE TABLE fatos (
                FAT_ID INTEGER PRIMARY KEY,
                FAT_TITLE TEXT NOT NULL,
                FAT_URL TEXT,
                FAT_IMG TEXT NOT NULL,
                FAT_DATE TEXT DEFAULT '21/04/2021',
                FAT_HOUR TEXT DEFAULT '00:00'
                )
            """
            )
        print('TABELA CRIADA!!!')        
    close_conection(my_conn)
    

# Criando tabela para spyder gov
def create_database_gov():        
    my_conn = open_conection()
    if crud('SELECT NAME FROM SQLITE_MASTER WHERE TYPE = "table" AND NAME = "gov"'):        
        print('TABELA JÁ EXISTE.')
    else:
        my_conn.execute(
            """
            CREATE TABLE gov (
                GOV_ID INTEGER PRIMARY KEY,
                GOV_TITLE TEXT NOT NULL,
                GOV_URL TEXT,
                GOV_IMG TEXT NOT NULL,
                GOV_DATE TEXT DEFAULT '21/04/2021',
                GOV_HOUR TEXT DEFAULT '00:00'
                )
            """
            )
        print('TABELA CRIADA!!!')        
    close_conection(my_conn)
   

# Função utilizada para Criar - Ler - Atualizar - Deletar na base
def crud(query, item={}):
    my_conn = open_conection()
    if 'select' in query.lower():
        resp = my_conn.execute(query, item)
        return [x for x in resp]
    else:
        my_conn.execute(query, item)
        my_conn.commit()
    close_conection(my_conn)
    

# t = {'title': 'Teste SQLITE', 'href': 'https://github.com/btiagor/Fato-ou-Fake', 'img': 'img text', 'date': '21/04/2021', 'hour': '20:57'}
# crud('insert into fatos(fat_title, fat_url, fat_img, fat_date, fat_hour) values("Teste SQLITE", "https://github.com/btiagor/Fato-ou-Fake", "img text", "21/04/2021", "20:57")')
# print(crud('select fat_id from fatos where fat_title = "Teste SQLITE" and fat_url = "https://github.com/btiagor/Fato-ou-Fake" and fat_img = "img text" and fat_date = "21/04/2021" and fat_hour = "20:57"'))
# print(crud('select fat_id from fatos where fat_title = :title and fat_url = :href and fat_img = :img and fat_date = :date and fat_hour = :hour', t))

# for i in crud('select * from fatos'):
#     print(i)
