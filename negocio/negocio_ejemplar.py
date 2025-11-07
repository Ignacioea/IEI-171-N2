from prettytable import PrettyTable

#importar datos
from datos.obtener_datos import obtener_lista_objetos, obtener_objeto_individual
from datos.insertar_datos import insertar_objeto
from datos.actualizar_datos import actualizar_objeto
from datos.eliminar_datos import eliminar_objeto

#importar modelos
from modelos.ejemplar import Ejemplar
from modelos.libro import Libro

#importar iu
from iu.iu_ejemplar import ingresar_datos_ejemplar, ingresar_codigo, ingresar_valor_atributo, pregunta_delete

from datos.conexion import Session

########################################## FUNCIONES PARA EL MENU DE ADMINISTRADOR ##########################################

def mostrar_ejemplar():
    tabla_ejemplar = PrettyTable()
    tabla_ejemplar.field_names = ['id', 'codigo', 'ubicacion', 'estado', 'id_libro']
    lista_ejemplares = obtener_lista_objetos(Ejemplar)
    if lista_ejemplares:
        for ejemplar in lista_ejemplares:
            tabla_ejemplar.add_row(
                [ejemplar.id, ejemplar.codigo, ejemplar.ubicacion, ejemplar.estado, ejemplar.id_libro])
        print(tabla_ejemplar)
            
#faltan opciones de validación para no agregar ejemplares erroneos
def registrar_ejemplar():
    datos = ingresar_datos_ejemplar()
    ejemplar = Ejemplar(
        codigo = datos["codigo"],
        ubicacion = datos["ubicacion"],
        estado = datos["estado"],
        id_libro = datos["idlibro"]
    )
    insertar_objeto(ejemplar)

def seleccionar_ejemplar():
    codigo_ejemplar = ingresar_codigo()
    ejemplar = obtener_objeto_individual(Ejemplar, "codigo", codigo_ejemplar)

    tabla_ejemplar = PrettyTable()
    tabla_ejemplar.field_names = ['id', 'codigo', 'ubicacion', 'estado', 'id_libro']
    if ejemplar:
        tabla_ejemplar.add_row([ejemplar.id, ejemplar.codigo, ejemplar.ubicacion, ejemplar.estado, ejemplar.id_libro])
        print(tabla_ejemplar)
        return ejemplar
    else:
        print("no se encontró el ejemplar")

def modificar_ejemplar():
    print("Modificar Ejemplar")
    ejemplar = seleccionar_ejemplar()
    if ejemplar:
        datos = ingresar_valor_atributo()
        if not datos["atributo"] or not datos["nuevo_valor"]:
            print("no se ha seleccionado atributo o valor válido")
            return
        setattr(ejemplar, datos["atributo"], datos["nuevo_valor"])
        actualizar_objeto(ejemplar)
    else:
        print("no se ha encontrado el ejemplar")

def eliminar_ejemplar():
    print("Eliminar Ejemplar")
    ejemplar = seleccionar_ejemplar()

    if ejemplar:
        delete = pregunta_delete()
        if delete == "s":
            eliminar_objeto(ejemplar)
        else:
            print("operación cancelada")
    else:
        print("no se ha encontrado el ejemplar")


def mostrar_ejemplar_libro():
    sesion = Session()
    nombre_libro = input("Ingrese el nombre del libro: ").strip()
    
    libro = sesion.query(Libro).filter(Libro.titulo.ilike(f"%{nombre_libro}%")).first()

    if not libro:
        print("No se encontró ningún libro con ese nombre.")
        return

    ejemplares = sesion.query(Ejemplar).filter(Ejemplar.id_libro == libro.id).all()

    if not ejemplares:
        print(f"No hay ejemplares registrados del libro '{libro.nombre}'.")
        return

    tabla = PrettyTable()
    tabla.field_names = ["Código","Ubicacion", "Estado", ]

    for ej in ejemplares:
        tabla.add_row([ej.codigo, ej.ubicacion, ej.estado])

    print(tabla)
########################################## FUNCIONES PARA EL MENU DE USUARIO ##########################################

def mostrar_ejemplares_disponibles():
    sesion = Session()
    lista_ejemplares_disp = sesion.query(Ejemplar, Libro).join(Libro, Ejemplar.id_libro == Libro.id).filter(Ejemplar.estado == "Disponible").all()
    tabla_ejemplares_disp = PrettyTable()
    tabla_ejemplares_disp.field_names = ["Codigo", "Ubicacion", "Libro"]
    if not lista_ejemplares_disp:
        print("No hay ejemplares disponibles")
    else:
        for ejemplar, libro in lista_ejemplares_disp:
            tabla_ejemplares_disp.add_row(
                [ejemplar.codigo, ejemplar.ubicacion, libro.titulo]
            )
        print(tabla_ejemplares_disp)