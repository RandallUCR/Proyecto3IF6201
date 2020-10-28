import AccesoDatos.mainAD as cnn
import time

def insert_in_table(_table_name,fechai,fechaf):
    try:
        conn = cnn.connect_pg()
        if conn == 0:
            print("Error al conectar")
        else:
            cur = conn.cursor()
#            _file_name = 'D:\\' + _table_name + ".csv"
            _file_name = _table_name +fechai+"_"+fechaf+".csv"
            with open("D:\\"+_file_name, 'r') as f:
                next(f)
                cur.copy_from(f, 'aplicada.'+_table_name, sep=',')
            conn.commit()
            print("Carga de datos exitosa")
            conn.close()
            #hay que obtener la fecha actual para ponerle al data set
            fecha = time.strftime("%y/%m/%d")
            data_set = (True, fecha, _file_name)
            cnn.actualizar_sqlite("UPDATE BITACORA SET CARGADO = ?, FECHA_CARGADO = ? WHERE NOMBRE_CSV = ?", data_set)
    except Exception as e:
        print("Error: "+e)

