from prettytable import PrettyTable
from datos.obtener_datos import obtener_lista_objetos
from datos.insertar_datos import insertar_ejemplar
from modelos.ejemplar import Ejemplar

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
    insertar_ejemplar(codigo, ubicacion, estado, idlibro)

