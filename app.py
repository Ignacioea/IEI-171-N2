from iu.main_menu import main_menu

from prettytable import PrettyTable
from datos.obtener_datos import obtener_lista_objetos
from modelos.usuarios import Usuarios
from modelos.ejemplar import Ejemplar
from modelos.libro import Libro



#main_menu()

#clase para mostrar los usuarios del sistema
def mostrar_usuarios():
    print("entrando al metodo")
    tabla_usuarios = PrettyTable()
    tabla_usuarios.field_names = ['id','nombre','apellido','rut','telefono','correo','sancionado', 'tipo de usuario']
    lista_usuarios = obtener_lista_objetos(Usuarios)
    if lista_usuarios:
        for usuario in lista_usuarios:
            tabla_usuarios.add_row(
                [usuario.id, usuario.nombre, usuario.apellido, usuario.rut, usuario.telefono, usuario.correo, usuario.sancionado, usuario.tipo_usuario])
        print(tabla_usuarios)
    

mostrar_usuarios()

def mostrar_ejemplar():
    print('Preparando tabla')
    tabla_ejemplar = PrettyTable()
    tabla_ejemplar.field_names = ['id', 'codigo', 'ubicacion', 'estado', 'id_libro']
    lista_ejemplares = obtener_lista_objetos(Ejemplar)
    if lista_ejemplares:
        for ejemplar in lista_ejemplares:
            tabla_ejemplar.add_row(
                [ejemplar.id, ejemplar.codigo, ejemplar.ubicacion, ejemplar.estado, ejemplar.id_libro])
        print(tabla_ejemplar)
            
mostrar_ejemplar()

def mostrar_libros():
    print('Preparando tabla')
    tabla_libros = PrettyTable()
    tabla_libros.field_names = ['id', 'titulo', 'editorial', 'anio_publicacion', 'categoria', 'ISBN', 'id_autor']
    lista_libros = obtener_lista_objetos(Libro)
    if lista_libros:
        for libros in lista_libros:
            tabla_libros.add_row(
                [libros.id, libros.titulo, libros.editorial, libros.anio_publicacion, libros.categoria, libros.ISBN, libros.id_autor])
        print(tabla_libros)

mostrar_libros()