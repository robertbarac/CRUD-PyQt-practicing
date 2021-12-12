import sqlite3
from sqlite3.dbapi2 import connect

class Contactos:
    def iniciar_conexion(self):
        conexion = sqlite3.connect('sistema.db')
        conexion.text_factory = lambda b: b.decode(errors = 'ignore')
        return conexion

    def leer_contactos(self):
        conexion = self.iniciar_conexion()
        cursor = conexion.cursor()
        sentenciaSQL = "SELECT * FROM contactos"
        cursor.execute(sentenciaSQL)
        return cursor.fetchall()
        # db_name = 'sistema.db'
        # query = "SELECT * FROM contactos"
        # with sqlite3.connect(db_name) as conn:
        #     cursor = conn.cursor()
        #     result = cursor.execute(query)
        #     conn.commit()
        # print(result)
    
    def crear_contacto(self, datos_contacto):
        conexion = self.iniciar_conexion()
        cursor = conexion.cursor()
        sentenciaSQL = "INSERT INTO contactos(nombre, correo) VALUES(?, ?)"
        cursor.execute(sentenciaSQL, datos_contacto)
        conexion.commit()
        conexion.close()
    
    def borrar_contacto(self, id_contacto):
        conexion = self.iniciar_conexion()
        cursor = conexion.cursor()
        sentenciaSQL = "DELETE FROM contactos WHERE id=(?)"
        cursor.execute(sentenciaSQL, [id_contacto])
        conexion.commit()
        conexion.close()

    def modificar_contacto(self, datos_contacto):
        conexion = self.iniciar_conexion()
        cursor = conexion.cursor()
        sentenciaSQL = "UPDATE contactos SET nombre=?, correo = ? WHERE id=?"
        cursor.execute(sentenciaSQL, datos_contacto)
        conexion.commit()
        conexion.close()
