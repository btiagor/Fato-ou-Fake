import sqlite3
db = 'fato.db'

def open_conection():
    conn = sqlite3.connect(db)
    return conn


def close_conection(conn):
    conn.close()

    
def create_database():        
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
   

def crud(query, item={}):
    my_conn = open_conection()
    if 'select' in query.lower():
        resp = my_conn.execute(query)
        return [x for x in resp]
    else:
        my_conn.execute(query, item)
        my_conn.commit()
    close_conection(my_conn)
    

# create_database()
# crud('insert into fatos(fat_title, fat_url, fat_img, fat_date, fat_hour) values("Teste SQLITE", "https://github.com/btiagor/Fato-ou-Fake", "img text", "21/04/2021", "20:57")')
# print('select * from fatos')