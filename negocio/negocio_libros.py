from prettytable import PrettyTable
#importar datos
from datos.obtener_datos import obtener_lista_objetos, obtener_objeto_individual, obtener_objeto_join
from datos.insertar_datos import insertar_objeto
from datos.actualizar_datos import actualizar_objeto

#importar modelos
from modelos.libro import Libro
from modelos.autor import Autor

#importar iu
from iu.iu_libros import ingresar_datos_libros, seleccionar_nombre_libro, ingresar_valor_atributo


########################################## FUNCIONES PARA EL MENU DE ADMINISTRADOR ##########################################

def mostrar_libros():
    tabla_libros = PrettyTable()
    tabla_libros.field_names = ['Id', 'Título', 'Editorial', 'Año', 'Categoria', 'ISBN', 'ID autor', 'ID Biblioteca']
    lista_libros = obtener_lista_objetos(Libro)
    if lista_libros:
        for libros in lista_libros:
            tabla_libros.add_row(
                [libros.id, libros.titulo, libros.editorial, libros.anio, libros.categoria, libros.ISBN, libros.id_autor, libros.id_biblioteca])
        print(tabla_libros)

#falta una confirmación para agregar datos validos y mostrar un mensaje de error
def registrar_libro():
    datos = ingresar_datos_libros()
    libro = Libro(
        titulo = datos["titulo"],
        editorial = datos["editorial"],
        anio = datos["anio"],
        categoria = datos["categoria"],
        ISBN = datos["ISBN"],
        id_autor = datos["autor"],
        id_biblioteca = datos["biblitoeca"]
        )
    
    insertar_objeto(libro)

def seleccionar_libro():
    titulo = seleccionar_nombre_libro()
    libro = obtener_objeto_individual(Libro, "titulo", titulo)

    tabla_libros = PrettyTable()
    tabla_libros.field_names = ["id", "titulo", "editorial", "año", "categoria", "ISBN", "id_autor", "id_biblioteca"]

    if libro:
        tabla_libros.add_row([libro.id, libro.titulo, libro.editorial, libro.anio, libro.categoria, libro.ISBN, libro.id_autor, libro.id_biblioteca])
        print(tabla_libros)
        return libro
    else:
        print("no se encontro el libro")


def modificar_libro():
    print("modificar libro")
    libro = seleccionar_libro()
    if libro:
        datos = ingresar_valor_atributo()

        if not datos["atributo"] or not datos["nuevo_valor"]:
            print("no se ha seleccionado atributo o valor válido")
            return
        
        setattr(libro, datos["atributo"], datos["nuevo_valor"])
        actualizar_objeto(libro)
    else:
        print("no se ha encontrado el libro")

########################################## FUNCIONES PARA EL MENU DE USUARIO ##########################################

def mostrar_libros_a_usuario():
    libro = Libro
    autor = Autor
    lista_libros = obtener_objeto_join(libro, autor, "id_autor", "id")
    tabla_libros = PrettyTable()
    tabla_libros.field_names = ['Título', 'Editorial', 'Año', 'Categoria', 'ISBN', 'Autor']
    if lista_libros:
        for libros, autor in lista_libros:
            tabla_libros.add_row(
                [libros.titulo, libros.editorial, libros.anio, libros.categoria, libros.ISBN, autor.nombre])
        print(tabla_libros)