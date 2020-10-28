import sys
import AccesoDatos.ConexionAD
import time

def clientes(fechai,fechaf):
    array = []
    try:
        data = AccesoDatos.ConexionAD.ejecutar(f"EXEC SP_CLIENTES '{fechai}','{fechaf}'")
        if len(data) <= 0:
            print("Clientes Vacio")

        else:
            fecha = time.strftime("%y/%m/%d")
            data_set = ('clientes'+fechai+'_'+fechaf+'.csv', True, fecha)
            AccesoDatos.ConexionAD.actualizar_sqlite("INSERT INTO BITACORA (NOMBRE_CSV, EXTRAIDO, FECHA_EXTRAIDO) VALUES (?,?,?);", data_set)
            for row in data:
                array.append(row)
        return array
    except IOError as e:
        print("Error en clientes" + e)

def telefonos(fechai, fechaf):
    array = []
    try:
        data = AccesoDatos.ConexionAD.ejecutar(f"EXEC SP_TELEFONOS '{fechai}','{fechaf}'")
        if len(data) <= 0 :
            print("Telefonos Vacio")

        else:
            fecha = time.strftime("%y/%m/%d")
            data_set = ('telefonos'+fechai+'_'+fechaf+'.csv', True, fecha)
            AccesoDatos.ConexionAD.actualizar_sqlite("INSERT INTO BITACORA (NOMBRE_CSV, EXTRAIDO, FECHA_EXTRAIDO) VALUES (?,?,?);", data_set)
            for row in data:
                array.append(row)
        return array
    except IOError as e:
        print("Error en telefonos"+e)

def direcciones(fechai, fechaf):
    array = []
    try:
        data = AccesoDatos.ConexionAD.ejecutar(f"EXEC SP_DIRECCIONES '{fechai}','{fechaf}'")
        if len(data) <= 0 :
            print("Direcciones Vacio")

        else:
            fecha = time.strftime("%y/%m/%d")
            data_set = ('direcciones'+fechai+'_'+fechaf+'.csv', True, fecha)
            AccesoDatos.ConexionAD.actualizar_sqlite("INSERT INTO BITACORA (NOMBRE_CSV, EXTRAIDO, FECHA_EXTRAIDO) VALUES (?,?,?);", data_set)
            for row in data:
                array.append(row)
        return array
    except IOError as e:
        print("Error en direcciones"+e)

def correos(fechai, fechaf):
    array = []
    try:
        data = AccesoDatos.ConexionAD.ejecutar(f"EXEC SP_CORREOS '{fechai}','{fechaf}'")
        if len(data) <= 0 :
            print("Correos Vacio")

        else:
            fecha = time.strftime("%y/%m/%d")
            data_set = ('correos'+fechai+'_'+fechaf+'.csv', True, fecha)
            AccesoDatos.ConexionAD.actualizar_sqlite("INSERT INTO BITACORA (NOMBRE_CSV, EXTRAIDO, FECHA_EXTRAIDO) VALUES (?,?,?);", data_set)
            for row in data:
                array.append(row)
        return array
    except IOError as e:
        print("Error en correos"+e)

def tarjetas(fechai, fechaf):
    array = []
    try:
        data = AccesoDatos.ConexionAD.ejecutar(f"EXEC SP_TARJETAS '{fechai}','{fechaf}'")
        if len(data) <= 0 :
            print("Tarjetas Vacio")

        else:
            fecha = time.strftime("%y/%m/%d")
            data_set = ('tarjetas'+fechai+'_'+fechaf+'.csv', True, fecha)
            AccesoDatos.ConexionAD.actualizar_sqlite("INSERT INTO BITACORA (NOMBRE_CSV, EXTRAIDO, FECHA_EXTRAIDO) VALUES (?,?,?);", data_set)
            for row in data:
                array.append(row)
        return array
    except IOError as e:
        print("Error en tarjetas"+e)

def ordenes(fechai, fechaf):
    array = []
    try:
        data = AccesoDatos.ConexionAD.ejecutar(f"EXEC SP_ORDENES '{fechai}','{fechaf}'")
        if len(data[0]) <= 0 :
            print("Ordenes Vacio")

        else:
            fecha = time.strftime("%y/%m/%d")
            data_set = ('ordenes'+fechai+'_'+fechaf+'.csv', True, fecha)
            AccesoDatos.ConexionAD.actualizar_sqlite("INSERT INTO BITACORA (NOMBRE_CSV, EXTRAIDO, FECHA_EXTRAIDO) VALUES (?,?,?);", data_set)
            for row in data:
                array.append(row)
        return array
    except IOError as e:
        print("Error en Ordenes"+e)



