from prettytable import PrettyTable
from datos.obtener_datos import obtener_lista_objetos
from modelos.libro import Libro


def mostrar_libros():
    tabla_libros = PrettyTable()
    tabla_libros.field_names = ['id', 'titulo', 'editorial', 'anio_publicacion', 'categoria', 'ISBN', 'id_autor']
    lista_libros = obtener_lista_objetos(Libro)
    if lista_libros:
        for libros in lista_libros:
            tabla_libros.add_row(
                [libros.id, libros.titulo, libros.editorial, libros.anio_publicacion, libros.categoria, libros.ISBN, libros.id_autor])
        print(tabla_libros)
