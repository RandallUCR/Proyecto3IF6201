import sqlite3
import psycopg2


def connect_pg():
    _host = "163.178.107.7"
    _dbname = "b61976_aplicada"
    _user = "laboratorios"
    _password = "saucr.120"
    try:
        cnn = psycopg2.connect(f"host={_host} dbname={_dbname} user={_user} password={_password}")
        print("Conexión exitosa")
        return cnn
    except Exception as e:
        print("Error al conectar: " + e)
        return 0

def sqlite_conexion():
    try:
        conexion = sqlite3.connect("C:\Aplicada.db")
        #   conexion = sqlite3.connect("/home/faubricioch/Aplicada.db")
        return conexion
    except IOError as e:
        print("Error en la conexion "+e)

def actualizar_sqlite(bt, nombre):
    try:
        conexion = sqlite_conexion()
        cursor = conexion.cursor()
        cursor.execute(bt, nombre)
        data_ret = cursor.fetchall()

        conexion.commit()

        return data_ret
    except IOError as e:
        print("Error en actualizar SQLite: " + e)
    finally:
        conexion.close()