#importar las opciones del menu
from iu.main_menu import *

#importar las funciones de negocio
from negocio.negocio_usuarios import login_usuario

#auxiliares
from auxiliares.app_info import app_name
from auxiliares.version import version_number

#modificar_ejemplar() <---- pendiente
#eliminar_ejemplar() <---- pendiente

#modificar_libros() <---- pendiente


#función para buscar usuario, nos puede servir para hacer el update y el delete
#buscar_usuario()


#login (cocinando 🐱‍🚀)
while True:
    print(f"{app_name} v{version_number}")
    user = login_usuario()

    if not user:
        continue

    if user.tipo_usuario.lower() in ["estudiante", "profesor"]:
        print(f"como {user.tipo_usuario.title()}, estas son sus opciones")
        print("[1] ver mi perfil")
        print("[2] ver libros")
        print("[3] ver mis prestamos")
        print("[4] salir")
        numero = int(input("seleccione un numero: "))

        if numero == 1:
            menu_perfil_usuario()
        elif numero == 2:
            menu_libros_usuario()
        elif numero == 3:
            ver_prestamos_usuario()
        elif numero == 4:
            print("saliendo...")
            break
        else:
                print("seleccione una opción valida")

    elif user.tipo_usuario.lower() == "administrador":
        print(f"como {user.tipo_usuario.title()}, estas son sus opciones")
        print("[1] ver usuarios")
        print("[2] ver libros")
        print("[3] ver ejemplares de libros")
        print("[4] ver prestamos")
        print("[5] salir")

        numero = int(input("seleccione un numero: "))
        if numero == 1:
            menu_usuarios_admin()
        elif numero == 2:
            menu_libros_admin()
        elif numero == 3:
            menu_ejemplares_admin()
        elif numero == 4:
            menu_prestamos_administrador()
        elif numero == 5:
            print("saliendo...")
            break
        else:
            print("seleccione una opción valida")
    else:
        print("usuario no encontrado.")