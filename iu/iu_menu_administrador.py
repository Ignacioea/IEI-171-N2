from negocio.negocio_usuarios import mostrar_usuarios, registrar_usuario, modificar_usuario, eliminar_usuario
from negocio.negocio_libros import mostrar_libros, registrar_libro, modificar_libro
from negocio.negocio_ejemplar import mostrar_ejemplar, registrar_ejemplar, modificar_ejemplar, eliminar_ejemplar, mostrar_ejemplar_libro
from negocio.negocio_prestamo import mostrar_prestamos

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
            mostrar_ejemplar_libro()
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
        mostrar_prestamos()
        print("Estas son sus opciones con respecto a los prestamos: \n")
        print("[1] salir")
        subnumero = int(input("seleccione un numero: "))
        if subnumero == 1:
            print("saliendo...")
            break
        else: 
            print("ingrese un numero válido por favor.")