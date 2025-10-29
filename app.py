#importar las opciones del menu
#from iu.main_menu import main_menu

#importar las funciones de negocio
#from negocio.negocio_usuarios import mostrar_usuarios, registrar_usuario
#from negocio.negocio_ejemplar import mostrar_ejemplar, registrar_ejemplar
#from negocio.negocio_libros import mostrar_libros, registrar_libro


#de momento se importan para crear funciones y probarlas en este apartado
#from auxiliares.app_info import app_name
#from auxiliares.version import version_number

# from modelos.usuarios import Usuarios
# from datos.obtener_datos import obtener_usuario_individual

#main_menu()


#mostrar_ejemplar()
#registrar_ejemplar()
#modificar_ejemplar() <---- pendiente
#eliminar_ejemplar() <---- pendiente

#mostrar_usuarios()
#registrar_usuario()
#modificar_uuario() <---- pendiente
#eliminar_usuario() <---- pendiente


#mostrar_libros()
#registrar_libro() 
#modificar_libros() <---- pendiente
#eliminar_libros() <----- pendiente

#función para buscar usuario, nos puede servir para hacer el update y el delete
# def buscar_usuario():
#     rutuser = input("Ingrese el RUT del usuario: ")
#     usuario_encontrado = obtener_usuario_individual(Usuarios, rutuser)

#     if usuario_encontrado:
#         print(f"""
#         ID: {usuario_encontrado.id}
#         Nombre: {usuario_encontrado.nombre}
#         Apellido: {usuario_encontrado.apellido}
#         RUT: {usuario_encontrado.rut}
#         Teléfono: {usuario_encontrado.telefono}
#         Correo: {usuario_encontrado.correo}
#         Sancionado: {usuario_encontrado.sancionado}
#         Tipo de usuario: {usuario_encontrado.tipo_usuario}
#         """)
#     else:
#         print("No se encontró un usuario con ese RUT.")
# buscar_usuario()

from datos.conexion import Session
from datos.obtener_datos import obtener_ejemplar
from datos.obtener_datos import libro_por_titulo
from prettytable import PrettyTable
from modelos.libro import Libro

sesion = Session()

def mostrar_ejemplar_disponible():
    sesion = Session()
    
    titulo = input("Ingrese el titulo del libro: ")
    libros = libro_por_titulo(titulo, sesion)
    
    if not libros:
        print(f"No se encontraron libro con ese titulo: {titulo}.")
        return
    
    print("Libros encontrados: ")
    tabla_libros = PrettyTable()
    tabla_libros.field_names = ["id", "titulo", "id_autor"]
    for libro in libros:
        tabla_libros.add_row([libro.id, libro.titulo, libro.id_autor])
    print(tabla_libros)
    
    
    id_libro = int(input("Ingrese el ID del libro para buscar ejemplares disponibles: "))
    
    ejemplares = obtener_ejemplar(id_libro, sesion)
    if not ejemplares:
        print("No hay ejemplares disponibles para este libro.")
        return
    print("Ejemplares disponible:")
    tabla_ejemplares = PrettyTable()
    tabla_ejemplares.field_names = ["id", "codigo", "ubicacion", "estado", "id_libro"]
    for ejemplar in ejemplares:
        tabla_ejemplares.add_row([ejemplar.id, ejemplar.codigo, ejemplar.ubicacion, "Disponible" if ejemplar.estado else "No", ejemplar.id_libro])
    print(tabla_ejemplares)

mostrar_ejemplar_disponible()