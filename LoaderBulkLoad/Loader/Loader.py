import AccesoDatos.mainAD as cnn


def insert_in_table(_table_name):
    try:
        conn = cnn.connect_pg()
        if conn == 0:
            print("Error al conectar")
        else:
            cur = conn.cursor()
            _file_name = 'D:\\' + _table_name + ".csv"
#            _file_name = _table_name + ".csv"
            with open(_file_name, 'r') as f:
                next(f)
                cur.copy_from(f, 'aplicada.'+_table_name, sep=',')
            conn.commit()
            print("Carga de datos exitosa")
            conn.close()
    except Exception as e:
        print("Error: "+e)
