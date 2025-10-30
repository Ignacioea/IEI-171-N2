from prettytable import PrettyTable
from datos.obtener_datos import obtener_lista_objetos, obtener_objeto_individual
from datos.insertar_datos import insertar_objeto
from datos.actualizar_datos import actualizar_objeto
from datos.eliminar_datos import eliminar_objeto
from modelos.ejemplar import Ejemplar

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
    print("Registro de Nuevo Ejemplar \n")
    codigo = input("ingrese el codigo del ejemplar: ")
    ubicacion = input("ingrese la ubicación del ejemplar: ")
    estado = "Disponible" #todos deben ingresarse en este estado
    idlibro = input("ingrese el id del libro correspondiente")

    ejemplar = Ejemplar(
        codigo = codigo,
        ubicacion = ubicacion,
        estado = estado,
        id_libro = idlibro
    )
    insertar_objeto(ejemplar)

def seleccionar_ejemplar():
    codigo_ejemplar = input("ingrese el codigo del ejemplar que desea seleccionar: ")
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
        print("Seleccione el atributo que desea cambiar")
        atributo = input("ingrese el atributo que desea cambiar: ")
        nuevo_valor = input("ingrese el nuevo valor: ")
        if not atributo or not nuevo_valor:
            print("no se ha seleccionado atributo o valor válido")
            return
        setattr(ejemplar, atributo, nuevo_valor)
        actualizar_objeto(ejemplar)
    else:
        print("no se ha encontrado el ejemplar")

def eliminar_ejemplar():
    print("Eliminar Ejemplar")
    ejemplar = seleccionar_ejemplar()

    if ejemplar:
        delete = input("seguro que desea eliminar este ejemplar? (s/n): ").lower()
        if delete == "s":
            eliminar_objeto(ejemplar)
        else:
            print("operación cancelada")
    else:
        print("no se ha encontrado el ejemplar")

########################################## FUNCIONES PARA EL MENU DE USUARIO ##########################################