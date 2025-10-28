#importar las opciones del menu
#from iu.main_menu import main_menu

#importar las funciones de negocio
#from negocio.negocio_usuarios import mostrar_usuarios, registrar_usuario
#from negocio.negocio_ejemplar import mostrar_ejemplar, registrar_ejemplar
#from negocio.negocio_libros import mostrar_libros, registrar_libro


#de momento se importan para crear funciones y probarlas en este apartado
#from auxiliares.app_info import app_name
#from auxiliares.version import version_number

from modelos.usuarios import Usuarios
from datos.obtener_datos import obtener_usuario_individual

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
def buscar_usuario():
    rutuser = input("Ingrese el RUT del usuario: ")
    usuario_encontrado = obtener_usuario_individual(Usuarios, rutuser)

    if usuario_encontrado:
        print(f"""
        ID: {usuario_encontrado.id}
        Nombre: {usuario_encontrado.nombre}
        Apellido: {usuario_encontrado.apellido}
        RUT: {usuario_encontrado.rut}
        Teléfono: {usuario_encontrado.telefono}
        Correo: {usuario_encontrado.correo}
        Sancionado: {usuario_encontrado.sancionado}
        Tipo de usuario: {usuario_encontrado.tipo_usuario}
        """)
    else:
        print("No se encontró un usuario con ese RUT.")
buscar_usuario()