# -*- coding: utf-8 -*-
import sqlite3
# db = 'fato.db'
# sqlite3.paramstyle = 'named'


# Função que abre a conexão
def open_conection(db='aosfatos.db'):
    conn = sqlite3.connect(db)
    return conn


# Função que fecha a conexão
def close_conection(conn):
    conn.close()

    
# Criando tabela para spyder aosfatos
def create_table_fatos():    
    my_conn = open_conection()
    if crud('SELECT NAME FROM SQLITE_MASTER WHERE TYPE = "table" AND NAME = "fatos"'):        
        print('TABELA JÁ EXISTE.')
    else:
        my_conn.execute(
            """                    
            CREATE TABLE fatos (
                FAT_ID INTEGER PRIMARY KEY,
                FAT_TITLE TEXT NOT NULL,
                FAT_FONTS TEXT,
                FAT_CONTENT TEXT,
                FAT_IMG TEXT NOT NULL,
                FAT_DATE TEXT DEFAULT '21/04/2021',
                FAT_AUTHOR TEXT,
                FAT_URL TEXT,
                FAT_DAY TEXT,
                FAT_MONTH TEXT,
                FAT_YEAR TEXT,
                FAT_HOUR TEXT                
                )
            """
            )
        print('TABELA CRIADA!!!')        
    close_conection(my_conn)
    

# Criando tabela para spyder gov
def create_table_gov():        
    my_conn = open_conection('gov.db')
    if crud('SELECT NAME FROM SQLITE_MASTER WHERE TYPE = "table" AND NAME = "gov"', 'gov.db'):        
        print('TABELA JÁ EXISTE.')
    else:
        my_conn.execute(
            """
            CREATE TABLE gov (
                GOV_ID INTEGER PRIMARY KEY,
                GOV_TITLE TEXT,                
                GOV_URL TEXT,
                GOV_CONTENT TEXT,
                GOV_IMG TEXT,
                GOV_DATE TEXT,
                GOV_HOUR TEXT,
                GOV_DAY TEXT,
                GOV_MONTH TEXT,
                GOV_YEAR TEXT
                )
            """
            )
        print('TABELA CRIADA!!!')        
    close_conection(my_conn)
   

# Função utilizada para Criar - Ler - Atualizar - Deletar na base
def crud(query, db='aosfatos.db'):
    my_conn = open_conection(db)
    
    if 'select' in query.lower():
        resp = my_conn.execute(query)
        resp = [x for x in resp]
        close_conection(my_conn)
        return resp
    else:
        my_conn.execute(query)
        my_conn.commit()
    close_conection(my_conn)
