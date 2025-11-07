from negocio.negocio_usuarios import tabla_perfil_usuario, modificar_perfil
from negocio.negocio_libros import mostrar_libros_a_usuario
from negocio.negocio_ejemplar import mostrar_ejemplares_disponibles
from negocio.negocio_prestamo import registrar_prestamo, mostrar_prestamo_usuario, devolver_ejemplar

def menu_perfil_usuario(user):
    while True:
        tabla_perfil_usuario(user)
        print("Estas son sus opciones con respecto a su perfil: \n")
        print("[1] modificar perfil")
        print("[2] salir")
        subnumero = int(input("seleccione un numero: "))
        if subnumero == 1:
            modificar_perfil(user)
            pass
        elif subnumero == 2:
            print("saliendo...")
            break
        else: 
            print("ingrese un numero válido por favor.")

def menu_libros_usuario(user):
    while True:
        mostrar_libros_a_usuario()
        print("Estas son sus opciones con respecto a los libros: \n")
        print("[1] ver ejemplares disponibles de un libro en especifico")
        print("[2] solicitar libro")
        print("[3] salir")

        subnumero = int(input("seleccione un numero: "))
        if subnumero == 1:
            mostrar_ejemplares_disponibles()
            break
        elif subnumero == 2:
            registrar_prestamo(user)
            break
        elif subnumero == 3:
            print("saliendo...")
            break
        else: 
            print("ingrese un numero válido por favor.")

def ver_prestamos_usuario(user):
    while True:
        mostrar_prestamo_usuario(user)
        print("Estas son sus opciones con respecto a los prestamos: \n")
        print("[1] devolver libro")
        print("[2] salir")

        subnumero = int(input("seleccione un numero: "))
        if subnumero == 1:
            devolver_ejemplar(user)
            break
        elif subnumero == 2:
            print("saliendo...")
            break
        else: 
            print("ingrese un numero válido por favor.")