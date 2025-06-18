import mysql.connector
from mysql.connector import Error

class conexion:
    def __init__(self):
        self.conn = None

    def open(self):
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="farmaciadb",
                port=3306
            )
            if self.conn.is_connected():
                print("Conexión exitosa a la base de datos")
                return self.conn
        except Error as err:
            print(f"Error al conectar con la base de datos: {err}")
            return None

    def close(self):
        if self.conn and self.conn.is_connected():
            self.conn.close()
            print("Conexión cerrada")
