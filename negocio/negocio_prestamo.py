from negocio.negocio_ejemplar import seleccionar_ejemplar
from datos.insertar_datos import insertar_objeto
from modelos.prestamo import Prestamo
from datetime import date, timedelta

def registrar_prestamo(user):

    print("Registro de Nuevo Prestamo \n")

    ejemplar = seleccionar_ejemplar()
    fecha_actual= date.today()
    fecha_dev = fecha_actual + timedelta(weeks = 2)
    prestamo = Prestamo(
        fecha_prestamo= fecha_actual,
        fecha_devolucion_estimado = fecha_dev,
        fecha_devolucion_real = " ",
        multa = False,
        id_usuario = user.id,
        id_ejemplar = ejemplar.id,
    )

    insertar_objeto(prestamo)
registrar_prestamo()