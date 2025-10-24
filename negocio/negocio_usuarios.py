def mostrar_usuarios():
    print("entrando al metodo")
    tabla_usuarios = PrettyTable()
    tabla_usuarios.field_names = ['id','nombre','apellido','rut','telefono','correo','sancionado', 'tipo de usuario']
    lista_usuarios = obtener_lista_objetos(Usuarios)
    if lista_usuarios:
        for usuario in lista_usuarios:
            tabla_usuarios.add_row(
                [usuario.id, usuario.nombre, usuario.apellido, usuario.rut, usuario.telefono, usuario.correo, usuario.sancionado, usuario.tipo_usuario])
        print(tabla_usuarios)
    

mostrar_usuarios()