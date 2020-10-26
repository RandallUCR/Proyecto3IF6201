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
