from negocio.negocio_ejemplar import seleccionar_ejemplar
from datos.insertar_datos import insertar_objeto
from modelos.prestamo import Prestamo
from datetime import date, timedelta
from prettytable import PrettyTable
from datos.obtener_datos import obtener_lista_objetos, obtener_objeto_join
from modelos.usuarios import Usuarios



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
#registrar_prestamo(usuario)


def mostrar_prestamo_usuario(user):
    prestamo = Prestamo
    usuario = Usuarios
    lista_prestamo = obtener_objeto_join(prestamo, usuario, "id_usuario", "id")
    tabla_prestamos = PrettyTable()
    tabla_prestamos.field_names = ["Nombre usuario", "RUT", "fecha del prestamo", "fecha de devolucion estimada", "fecha de devolucion real", "multa"]
    if not lista_prestamo:
        print("No hay prestamos activos.")
    else:
        for prestamo, usuario in lista_prestamo:
            tabla_prestamos.add_row(
                [usuario.nombre, usuario.rut, prestamo.fecha_prestamo, prestamo.fecha_devolucion_estimado, prestamo.fecha_devolucion_real, prestamo.multa]
            )
        print(tabla_prestamos)