import ReglasNegocio.GenerarCsvRN
import AccesoDatos.ConexionAD

def ExtractorPrincipal(fechai,fechaf):
    try:
        ReglasNegocio.GenerarCsvRN.generarClientesCsv(fechai,fechaf)
        ReglasNegocio.GenerarCsvRN.generarTelefonosCsv(fechai,fechaf)
        ReglasNegocio.GenerarCsvRN.generarDireccionesCsv(fechai,fechaf)
        ReglasNegocio.GenerarCsvRN.generarCorreosCsv(fechai,fechaf)
        ReglasNegocio.GenerarCsvRN.generarTarjetasCsv(fechai,fechaf)
        ReglasNegocio.GenerarCsvRN.generarOrdenesCsv(fechai,fechaf)
    except Exception as e:
        print("Error en el extractor final "+e)

def EliminarClientesOrdenes():
    try:
        data= AccesoDatos.ConexionAD.ejecutar("EXEC SP_CLIENTES_ORDENES")
        print(data[0][0])
    except IOError as e:
        print("Error al eliminar Clientes y Ordenes")