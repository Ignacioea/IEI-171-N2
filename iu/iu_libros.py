def ingresar_datos_libros():
    print("Registro de un Nuevo Libro\n")
    titulo = input("Ingrese el nombre del libro: ")
    editorial = input("Ingrese el nombre de la editorial: ")
    anio = input("Ingrese el año de emisión: ")
    categoria = input("Ingrese la categoría del libro: ")
    ISBN = input("ingrese el ISBN: ")
    autor = input("ingrese la ID del autor: ")
    biblioteca = input("Ingrese la ID de la biblioteca: ")
    return{
        "titulo":titulo,
        "editorial": editorial,
        "anio": anio,
        "categoria": categoria,
        "ISBN": ISBN,
        "autor": autor,
        "biblioteca":biblioteca
    }

def seleccionar_nombre_libro():
    nombre = input("ingrese el nombre del libro")
    return nombre

def ingresar_valor_atributo():
    print("seleccione el atributo que desea cambiar")
    atributo = input("escriba el atributo que desea cambiar: ")
    nuevo_valor = input("ingrese el nuevo valor: ")
    return{
        "atributo": atributo,
        "nuevo_valor": nuevo_valor
    }