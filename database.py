import psycopg2
from psycopg2 import Error

class ConexionDB:
    def __init__(self, host="localhost", database="SISTEMA SIPU", user="postgres", password="adonism2006"):
        # CAMBIA 'TU_CONTRASEÑA_AQUI' POR LA TUYA DE PGADMIN
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = None
        self.cursor = None

    def conectar(self):
        try:
            self.connection = psycopg2.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            self.cursor = self.connection.cursor()
            # print("Conexión establecida") # Descomenta si quieres ver cuando conecta
        except Error as e:
            print(f"❌ Error conectando a PostgreSQL: {e}")

    def ejecutar_consulta(self, query, params=None):
        """Para selects (Lectura)"""
        if self.connection:
            try:
                self.cursor.execute(query, params)
                return self.cursor.fetchall()
            except Error as e:
                print(f"❌ Error en consulta: {e}")
                return []

    def cerrar(self):
        if self.cursor: self.cursor.close()
        if self.connection: self.connection.close()