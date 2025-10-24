def mostrar_ejemplar():
    print('Preparando tabla')
    tabla_ejemplar = PrettyTable()
    tabla_ejemplar.field_names = ['id', 'codigo', 'ubicacion', 'estado', 'id_libro']
    lista_ejemplares = obtener_lista_objetos(Ejemplar)
    if lista_ejemplares:
        for ejemplar in lista_ejemplares:
            tabla_ejemplar.add_row(
                [ejemplar.id, ejemplar.codigo, ejemplar.ubicacion, ejemplar.estado, ejemplar.id_libro])
        print(tabla_ejemplar)
            
mostrar_ejemplar()