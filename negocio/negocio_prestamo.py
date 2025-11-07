from prettytable import PrettyTable
from datetime import date, timedelta

#importar datos
from datos.insertar_datos import insertar_objeto
from datos.actualizar_datos import actualizar_objeto
from datos.obtener_datos import obtener_objeto_individual

#importar modelos
from modelos.prestamo import Prestamo
from modelos.usuarios import Usuarios
from modelos.ejemplar import Ejemplar

#importar negocio
from negocio.negocio_ejemplar import mostrar_ejemplares_disponibles

#importar iu
from iu.iu_negocio import ingresar_codigo, ingresar_datos_prestamo

from datos.conexion import Session


def registrar_prestamo(user):
    mostrar_ejemplares_disponibles()
    
    print("Registro de Nuevo Prestamo \n")
    
    codigo_ejemplar = ingresar_codigo()
    ejemplar = obtener_objeto_individual(Ejemplar, "codigo", codigo_ejemplar)
    fecha_actual= date.today()
    fecha_dev = fecha_actual + timedelta(weeks = 2)
    
    prestamo = Prestamo(
        fecha_prestamo= fecha_actual,
        fecha_devolucion_estimado = fecha_dev,
        fecha_devolucion_real = " ",
        multa = False,
        id_usuario = user.id,
        id_ejemplar = ejemplar.id
    )
   
    insertar_objeto(prestamo)
    ejemplar.estado = "No disponible"
    actualizar_objeto(ejemplar)

def mostrar_prestamo_usuario(usuario):
    sesion = Session()
    
    lista_prestamo = sesion.query(Prestamo, Usuarios, Ejemplar).join(Usuarios, Prestamo.id_usuario == Usuarios.id).join(Ejemplar, Prestamo.id_ejemplar == Ejemplar.id).filter(Usuarios.id == usuario.id).all()
    tabla_prestamos = PrettyTable()
    tabla_prestamos.field_names = ["Numero de prestamo", "Nombre usuario", "RUT", "Codigo Ejemplar", "fecha del prestamo", "fecha de devolucion estimada", "fecha de devolucion real", "multa"]
    if not lista_prestamo:
        print("No hay prestamos activos.")
    else:
        for prestamo, usuario, ejemplar in lista_prestamo:
            tabla_prestamos.add_row(
                [prestamo.id, usuario.nombre, usuario.rut, ejemplar.codigo, prestamo.fecha_prestamo, prestamo.fecha_devolucion_estimado, prestamo.fecha_devolucion_real, prestamo.multa]
            )
        print(tabla_prestamos)


def devolver_ejemplar(user):
    mostrar_prestamo_usuario(user)

    datos = ingresar_datos_prestamo()
    ejemplar = obtener_objeto_individual(Ejemplar, "codigo", datos["codigo_ejemplar"])
    prestamo = obtener_objeto_individual(Prestamo, "id", datos["id_prestamo"])
    
    if not prestamo or not ejemplar:
        print("Prestamo o ejemplar incorrecto.")
        return
    
    fecha_actual = date.today()
    prestamo.fecha_devolucion_real = fecha_actual
    
    if fecha_actual > prestamo.fecha_devolucion_estimado:
        prestamo.multa = True
        print("La entrega esta fuera del plazo, por lo que seras multado.")
    
    else: 
        print("La entrega esta dentro del plazo.")
    
    ejemplar.estado = "Disponible"
    
    actualizar_objeto(prestamo)
    actualizar_objeto(ejemplar)