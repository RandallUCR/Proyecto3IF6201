import pymssql
import sqlite3

_sql_server = "DESKTOP-V6FAAH1"
_sql_database = "IF6201_Proyecto3"
_sql_server_port = 1433
_sql_user = "Randall"
_sql_password = "randall8"

def mssql_conexion():
    try:
        cnx = pymssql.connect(server=_sql_server, port=_sql_server_port,
                              user=_sql_user, password=_sql_password,
                              database=_sql_database)
        return cnx
    except IOError as e:
        print("Error en la conexion "+e)

def ejecutar(sp):
    try:
        cnx = mssql_conexion()
        cur = cnx.cursor()
        cur.execute(sp)
        data_return = cur.fetchall()

        cnx.commit()


        return data_return
    except IOError as e:
        print("Error en ejecutar: "+e)
    finally:
        cnx.close()

def sqlite_conexion():
    try:
        conexion = sqlite3.connect("Aplicada")
        return conexion
    except IOError as e:
        print("Error en la conexion "+e)

def actualizar_sqlite(bt):
    try:
        conexion = sqlite_conexion()
        cursor = conexion.cursor()
        cursor.execute(bt)
        data_ret = cursor.fetchall()

        conexion.commit()

        return data_ret
    except IOError as e:
        print("Error en actualizar SQLite: " + e)
    finally:
        conexion.close()