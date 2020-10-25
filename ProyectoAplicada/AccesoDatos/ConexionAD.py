import pymssql

_sql_server = "DESKTOP-C3I87PH"
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