import sqlite3
from sqlite3.dbapi2 import connect

class Contactos:
    def iniciar_conexion(self):
        conexion = sqlite3.connect('sistema.db')
        conexion.text_factory = lambda b: b.decode(errors = 'ignore')
        return conexion

    def leer_contactos(self):
        conexion = self.iniciar_conexion8
        cursor = conexion.cursor()
        sentenciaSQL = "SELECT * FROM contactos"
        cursor.execute(sentenciaSQL)
        print(cursor.fetchall())
        # db_name = 'sistema.db'
        # query = "SELECT * FROM contactos"
        # with sqlite3.connect(db_name) as conn:
        #     cursor = conn.cursor()
        #     result = cursor.execute(query)
        #     conn.commit()
        # print(result)
    
    

