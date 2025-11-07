def ingresar_codigo():
    codigo = input("Ingrese el codigo del ejemplar: ")
    return codigo

def ingresar_datos_prestamo():
    id_prestamo = input("Ingrese el numero de prestamo: ")
    codigo_ejemplar = input("Ingrese el codigo del ejemplar a devolver: ")
    return {
        "id_prestamo": id_prestamo,
        "codigo_ejemplar": codigo_ejemplar
    }