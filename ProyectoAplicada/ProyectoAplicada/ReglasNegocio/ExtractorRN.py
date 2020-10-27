import sys
import AccesoDatos.ConexionAD

def clientes(fechai,fechaf):
    array = []
    try:
        data = AccesoDatos.ConexionAD.ejecutar(f"EXEC SP_CLIENTES '{fechai}','{fechaf}'")
        if len(data) <= 0:
            print("Clientes Vacio")
            sys.exit(0)
        else:
            AccesoDatos.ConexionAD.actualizar_sqlite(f"INSERT INTO BITACORA VALUES (0,'clientes.csv', true, getdate(), false, null);")
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
            sys.exit(0)
        else:
            AccesoDatos.ConexionAD.actualizar_sqlite(f"INSERT INTO BITACORA VALUES (0,'telefonos.csv', true, getdate(), false, null);")
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
            sys.exit(0)
        else:
            AccesoDatos.ConexionAD.actualizar_sqlite(f"INSERT INTO BITACORA VALUES (0,'direcciones.csv', true, getdate(), false, null);")
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
            sys.exit(0)
        else:
            AccesoDatos.ConexionAD.actualizar_sqlite(f"INSERT INTO BITACORA VALUES (0,'correos.csv', true, getdate(), false, null);")
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
            sys.exit(0)
        else:
            AccesoDatos.ConexionAD.actualizar_sqlite(f"INSERT INTO BITACORA VALUES (0,'tarjetas.csv', true, getdate(), false, null);")
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
            sys.exit(0)
        else:
            AccesoDatos.ConexionAD.actualizar_sqlite(f"INSERT INTO BITACORA VALUES (0,'ordenes.csv', true, getdate(), false, null);")
            for row in data:
                array.append(row)
        return array
    except IOError as e:
        print("Error en Ordenes"+e)



