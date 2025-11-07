def ingresar_datos_ejemplar():
    print("Registro de Nuevo Ejemplar \n")
    codigo = input("ingrese el codigo del ejemplar: ")
    ubicacion = input("ingrese la ubicación del ejemplar: ")
    estado = "Disponible" #todos deben ingresarse en este estado
    idlibro = input("ingrese el id del libro correspondiente")
    return{
        "codigo": codigo,
        "ubicacion": ubicacion,
        "estado": estado,
        "idlibro": idlibro
    }

def ingresar_codigo():
    codigo = input("ingrese el codigo del ejemplar que desea seleccionar: ")
    return codigo

def ingresar_valor_atributo():
    print("seleccione el atributo que desea cambiar")
    atributo = input("escriba el atributo que desea cambiar: ")
    nuevo_valor = input("ingrese el nuevo valor: ")
    return{
        "atributo": atributo,
        "nuevo_valor": nuevo_valor
    }

def pregunta_delete():
    delete = input("seguro que desea eliminar este ejemplar? (s/n): ").lower()
    return delete