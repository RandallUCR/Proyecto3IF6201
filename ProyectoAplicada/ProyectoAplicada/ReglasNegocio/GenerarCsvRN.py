import csv
import ReglasNegocio.ExtractorRN

def generarClientesCsv(fechai,fechaf):
    with open('D:\clientes.csv','w',newline='') as f:
        columnas = ["ID_CLIENTE","CEDULA","NOMBRE","APELLIDO_UNO","APELLIDO_DOS","FECHA_INS"]
        escritor = csv.DictWriter(f,fieldnames=columnas)
        escritor.writeheader()

        data = ReglasNegocio.ExtractorRN.clientes(fechai,fechaf);
        for i in range(len(data)):
            escritor.writerow({columnas[0]:data[i][0],columnas[1]:data[i][1],columnas[2]:data[i][2],columnas[3]:data[i][3],columnas[4]:data[i][4],columnas[5]:data[i][5]})
    print('CSV de clientes creado')

def generarTelefonosCsv(fechai,fechaf):
    with open('D:\telefonos.csv','w',newline='') as f:
        columnas = ["ID","NUMERO","ID_CLIENTE","FECHA_INS"]
        escritor = csv.DictWriter(f,fieldnames=columnas)
        escritor.writeheader()

        data = ReglasNegocio.ExtractorRN.telefonos(fechai,fechaf);
        for i in range(len(data)):
            escritor.writerow({columnas[0]:data[i][0],columnas[1]:data[i][1],columnas[2]:data[i][2],columnas[3]:data[i][3]})
    print('CSV de telefonos creado')

def generarDireccionesCsv(fechai,fechaf):
    with open('D:\direcciones.csv','w',newline='') as f:
        columnas = ["ID","DIRECCIONES","ID_CLIENTE","FECHA_INS"]
        escritor = csv.DictWriter(f,fieldnames=columnas)
        escritor.writeheader()

        data = ReglasNegocio.ExtractorRN.direcciones(fechai,fechaf);
        for i in range(len(data)):
            escritor.writerow({columnas[0]:data[i][0],columnas[1]:data[i][1],columnas[2]:data[i][2],columnas[3]:data[i][3]})
    print('CSV de direcciones creado')

def generarCorreosCsv(fechai,fechaf):
    with open('D:\correos.csv','w',newline='') as f:
        columnas = ["ID","CORREO","ID_CLIENTE","FECHA_INS"]
        escritor = csv.DictWriter(f,fieldnames=columnas)
        escritor.writeheader()

        data = ReglasNegocio.ExtractorRN.correos(fechai,fechaf);
        for i in range(len(data)):
            escritor.writerow({columnas[0]:data[i][0],columnas[1]:data[i][1],columnas[2]:data[i][2],columnas[3]:data[i][3]})
    print('CSV de correos creado')
def generarTarjetasCsv(fechai,fechaf):
    with open('D:\tarjetas.csv','w',newline='') as f:
        columnas = ["ID","TARJETA","ID_CLIENTE","FECHA_INS"]
        escritor = csv.DictWriter(f,fieldnames=columnas)
        escritor.writeheader()

        data = ReglasNegocio.ExtractorRN.tarjetas(fechai,fechaf);
        for i in range(len(data)):
            escritor.writerow({columnas[0]:data[i][0],columnas[1]:data[i][1],columnas[2]:data[i][2],columnas[3]:data[i][3]})
    print('CSV de tarjetas creado')

def generarOrdenesCsv(fechai,fechaf):
    with open('D:\ordenes.csv','w',newline='') as f:
        columnas = ["ID","DETALLE","ID_CLIENTE"]
        escritor = csv.DictWriter(f,fieldnames=columnas)
        escritor.writeheader()

        data = ReglasNegocio.ExtractorRN.ordenes(fechai,fechaf);
        for i in range(len(data)):
            escritor.writerow({columnas[0]:data[i][0],columnas[1]:data[i][1],columnas[2]:data[i][2]})
    print('CSV de ordenes creado')