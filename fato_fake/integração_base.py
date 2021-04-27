import banco as bd
import sqlite3
import os

DB = 'integracao_bases.db'
DB_GOV = 'gov.db'

# Criando tabela para spyder aosfatos
def create_table_integracao():    
    # Abre conexão com o banco
    my_conn = bd.open_conection(DB)    
    # Checa se a tabela já existe caso contrário cria
    if bd.crud('SELECT NAME FROM SQLITE_MASTER WHERE TYPE = "table" AND NAME = "integra"', DB):        
        print('TABELA JÁ EXISTE.')
    else:
        my_conn.execute(
            """                             
            CREATE TABLE integra (
                INT_ID INTEGER PRIMARY KEY,
                INT_TITLE TEXT NOT NULL,
                INT_FONTS TEXT,
                INT_CONTENT TEXT,
                INT_IMG TEXT NOT NULL,
                INT_DATE TEXT DEFAULT '21/04/2021',
                INT_AUTHOR TEXT,
                INT_URL TEXT,
                INT_DAY TEXT,
                INT_MONTH TEXT,
                INT_YEAR TEXT,
                INT_HOUR TEXT,       
                INT_BASE TEXT
                )
            """
            )
        print('TABELA CRIADA!!!')        
    bd.close_conection(my_conn)
    

def integracao_bases():    
    create_table_integracao()
    # consulta a base toda e retorna um lista
    resp = bd.crud("""select FAT_TITLE, FAT_FONTS, FAT_CONTENT, FAT_IMG, FAT_DATE, FAT_AUTHOR, FAT_URL, FAT_DAY, FAT_MONTH, FAT_YEAR, FAT_HOUR from fatos""")
    for i in resp:
        # Para cada resultado checa se já existe na base de integração, caso não exista insere na base integração o elemento
        data_exist = bd.crud(
            f"""select int_id from integra 
            where 
            int_title = "{i[0]}" and
            int_fonts = "{i[1]}" and 
            int_content = "{i[2]}" and 
            int_img = "{i[3]}" and 
            int_date = "{i[4]}" and 
            int_author = "{i[5]}" and 
            int_url = "{i[6]}" and 
            int_day = "{i[7]}" and 
            int_month = "{i[8]}" and 
            int_year = "{i[9]}" and 
            int_hour = "{i[10]}"
            """, DB)
        
        if not data_exist:
            bd.crud(                    
                f"""insert into integra 
                (INT_TITLE, INT_FONTS, INT_CONTENT, INT_IMG, INT_DATE, INT_AUTHOR, INT_URL, INT_DAY, INT_MONTH, INT_YEAR, INT_HOUR, INT_BASE)
                values ("{i[0]}", "{i[1]}", "{i[2]}", "{i[3]}", "{i[4]}", "{i[5]}", "{i[6]}", "{i[7]}", "{i[8]}", "{i[9]}", "{i[10]}", "aosfatos")            
                """, DB)
    
    # mesmo processo que o anterior
    resp = bd.crud("""select GOV_TITLE, GOV_URL, GOV_CONTENT, GOV_IMG, GOV_DATE, GOV_HOUR, GOV_DAY, GOV_MONTH, GOV_YEAR from gov""", DB_GOV)
    for i in resp:
        data_exist = bd.crud(
            f"""select int_id from integra 
            where 
            int_title = "{i[0]}" and            
            int_url = "{i[1]}" and 
            int_content = "{i[2]}" and 
            int_img = "{i[3]}" and 
            int_date = "{i[4]}" and 
            int_hour = "{i[5]}" and
            int_day = "{i[6]}" and 
            int_month = "{i[7]}" and 
            int_year = "{i[8]}"          
            """, DB)        
        if not data_exist:
            bd.crud(                    
                f"""insert into integra 
                (INT_TITLE, INT_FONTS, INT_CONTENT, INT_IMG, INT_DATE, INT_AUTHOR, INT_URL, INT_DAY, INT_MONTH, INT_YEAR, INT_HOUR, INT_BASE)
                values ("{i[0]}", "None", "{i[2]}", "{i[3]}", "{i[4]}", "None", "{i[1]}", "{i[6]}", "{i[7]}", "{i[8]}", "{i[5]}", "gov")            
                """, DB)

integracao_bases()

    