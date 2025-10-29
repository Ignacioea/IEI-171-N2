from prettytable import PrettyTable
from datos.obtener_datos import obtener_lista_objetos, obtener_objeto_individual
from datos.insertar_datos import insertar_objeto
from datos.eliminar_datos import eliminar_objeto
from modelos.libro import Libro


def mostrar_libros():
    tabla_libros = PrettyTable()
    tabla_libros.field_names = ['Id', 'Título', 'Editorial', 'Año', 'Categoria', 'ISBN', 'ID autor', 'ID Biblioteca']
    lista_libros = obtener_lista_objetos(Libro)
    if lista_libros:
        for libros in lista_libros:
            tabla_libros.add_row(
                [libros.id, libros.titulo, libros.editorial, libros.anio, libros.categoria, libros.ISBN, libros.id_autor, libros.id_biblioteca])
        print(tabla_libros)

#falta una confirmación para agregar datos validos y mostrar un mensaje de error
def registrar_libro():
    print("Registro de un Nuevo Libro\n")
    titulo = input("Ingrese el nombre del libro: ")
    editorial = input("Ingrese el nombre de la editorial: ")
    anio = input("Ingrese el año de emisión: ")
    categoria = input("Ingrese la categoría del libro: ")
    ISBN = input("ingrese el ISBN: ")
    autor = input("ingrese la ID del autor: ")
    biblioteca = input("Ingrese la ID de la biblioteca: ")
    libro = Libro(
        titulo = titulo,
        editorial = editorial,
        anio = anio,
        categoria = categoria,
        ISBN = ISBN,
        id_autor = autor,
        id_biblioteca = biblioteca
        )
    
    insertar_objeto(libro)