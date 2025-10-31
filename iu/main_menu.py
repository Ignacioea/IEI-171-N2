from negocio.negocio_usuarios import mostrar_usuarios, registrar_usuario, modificar_usuario, eliminar_usuario, tabla_perfil_usuario
from negocio.negocio_libros import mostrar_libros, registrar_libro, modificar_libro, mostrar_libros_a_usuario
from negocio.negocio_ejemplar import mostrar_ejemplar, registrar_ejemplar, modificar_ejemplar, eliminar_ejemplar


########################################## FUNCIONES PARA EL MENU DE ADMINISTRADOR ##########################################
def menu_usuarios_admin():
    while True:
        mostrar_usuarios()
        print("Estas son sus opciones con respecto a los usuarios: \n")
        print("[1] agregar un usuario")
        print("[2] modificar usuario")
        print("[3] eliminar usuario")
        print("[4] salir")
        subnumero = int(input("seleccione un numero: "))
        if subnumero == 1:
            registrar_usuario()
            break
        elif subnumero == 2:
            modificar_usuario()
            break
        elif subnumero == 3:
            eliminar_usuario()
            break
        elif subnumero == 4:
            print("saliendo...")
            break
        else:
            print("ingrese un numero válido por favor.")

def menu_libros_admin():
    while True:
        mostrar_libros()
        print("Estas son sus opciones con respecto a los libros: \n")
        print("[1] agregar un libro")
        print("[2] modificar libro")
        print("[3] buscar ejemplares de un libro")
        print("[4] salir")
        subnumero = int(input("seleccione un numero: "))
        if subnumero == 1:
            registrar_libro()
        elif subnumero == 2:
            modificar_libro()
            break
            
        elif subnumero == 3:
            #buscar_ejemplar() la idea esta en hacer algo similar con lo de buscar usuario
            break
        elif subnumero == 4:
            print("saliendo...")
            break
        else: 
            print("ingrese un numero válido por favor.")

def menu_ejemplares_admin():
    while True:
        mostrar_ejemplar()
        print("Estas son sus opciones con respecto a los ejemplares: \n")
        print("[1] agregar un ejemplar")
        print("[2] modificar ejemplar")
        print("[3] eliminar ejemplar")
        print("[4] salir")
        subnumero = int(input("seleccione un numero: "))
        if subnumero == 1:
            registrar_ejemplar()
            break
        elif subnumero == 2:
            modificar_ejemplar()
            break
        elif subnumero == 3:
            eliminar_ejemplar()
            break
        elif subnumero == 4:
            print("saliendo...")
            break
        else: 
            print("ingrese un numero válido por favor.")

def menu_prestamos_administrador(): 
    while True:       
        #mostrar_prestamos()
        print("Estas son sus opciones con respecto a los prestamos: \n")
        print("[1] mostrar prestamos retrasados")
        print("[2] aplicar sanción")
        print("[3] ver sanciones")
        print("[3] salir")
        subnumero = int(input("seleccione un numero: "))
        if subnumero == 1:
            #mostrar_retrasos()
            break
        elif subnumero == 2:
            #aplicar_sancion()
            break
        elif subnumero == 3:
            #ver_sanciones()
            break
        elif subnumero == 4:
            print("saliendo...")
            break
        else: 
            print("ingrese un numero válido por favor.")

########################################## FUNCIONES PARA EL MENU DE USUARIO ##########################################
def menu_perfil_usuario(user):
    while True:
        tabla_perfil_usuario(user)
        print("Estas son sus opciones con respecto a su perfil: \n")
        print("[1] modificar perfil")
        print("[2] salir")
        subnumero = int(input("seleccione un numero: "))
        if subnumero == 1:
            #modificar_perfil()
            pass
        elif subnumero == 2:
            print("saliendo...")
            break
        else: 
            print("ingrese un numero válido por favor.")
def menu_libros_usuario():
    while True:
        mostrar_libros_a_usuario()
        print("Estas son sus opciones con respecto a los libros: \n")
        print("[1] ver ejemplares disponibles de un libro en especifico")
        print("[2] solicitar libro")
        print("[3] salir")

        subnumero = int(input("seleccione un numero: "))
        if subnumero == 1:
            #ver_ejemplares_disponibles()
            break
        elif subnumero == 2:
            #solicitar_libro()
            break
        elif subnumero == 3:
            print("saliendo...")
            break
        else: 
            print("ingrese un numero válido por favor.")

def ver_prestamos_usuario():
    while True:
        #mostrar_prestamos() para el usuario en especifico
        print("Estas son sus opciones con respecto a los prestamos: \n")
        print("[1] devolver libro")
        print("[2] salir")

        subnumero = int(input("seleccione un numero: "))
        if subnumero == 1:
            #devolver_libro
            break
        elif subnumero == 2:
            print("saliendo...")
            break
        else: 
            print("ingrese un numero válido por favor.")