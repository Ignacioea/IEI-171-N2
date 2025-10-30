from prettytable import PrettyTable
from datos.obtener_datos import obtener_lista_objetos, obtener_objeto_individual, obtener_objeto_login
from modelos.usuarios import Usuarios
from datos.insertar_datos import insertar_objeto
from datos.eliminar_datos import eliminar_objeto
from datos.actualizar_datos import actualizar_objeto



########################################## FUNCIONES PARA EL MENU DE ADMINISTRADOR ##########################################
def mostrar_usuarios():
    tabla_usuarios = PrettyTable()
    tabla_usuarios.field_names = ['id','nombre','apellido','rut','telefono','correo','sancionado', 'tipo_usuario']
    lista_usuarios = obtener_lista_objetos(Usuarios)
    if lista_usuarios:
        for usuario in lista_usuarios:
            tabla_usuarios.add_row(
                [usuario.id, usuario.nombre, usuario.apellido, usuario.rut, usuario.telefono, usuario.correo, usuario.sancionado, usuario.tipo_usuario])
        print(tabla_usuarios)


#faltan opciones de validación para no agregar usuarios erroneos
def registrar_usuario():
    print("Registro de Nuevo Usuario \n")
    nombre = input("ingrese nombre: ")
    apellido = input("ingrese apellido: ")
    rut = input("ingrese rut (sin puntos ni guión): ")
    telefono = input("ingrese su numero: ")
    correo = input("ingrese su correo electrónico: ")
    sancionado = False #por ser usuario nuevo la sanción directamente es False
    tipo_usuario = input("imgrese si es estudiante/profesor/administrador: ")

    usuario = Usuarios(
        nombre=nombre,
        apellido = apellido,
        rut = rut,
        telefono = telefono,
        correo = correo,
        sancionado = sancionado,
        tipo_usuario = tipo_usuario
    )

    insertar_objeto(usuario)

#función para buscar un usuario en especifico por su rut
def buscar_usuario():
    rutuser = input("imgrese el RUT del usuario: ")
    usuario = obtener_objeto_individual(Usuarios, "rut", rutuser)

    tabla_usuario = PrettyTable()
    tabla_usuario.field_names = ["id", "nombre", "apellido", "rut", "telefono", "correo", "sanción", "tipo_usuario"]
    if usuario:
        tabla_usuario.add_row([usuario.id, usuario.nombre, usuario.apellido, usuario.rut, usuario.telefono, usuario.correo, usuario.sancionado, usuario.tipo_usuario])
        print(tabla_usuario)
        return usuario
    else:
        print("No se encontró el usuario")
    
#funcion para eliminar un usuario
def eliminar_usuario():
    print("Eliminar Usuario")
    usuario = buscar_usuario()

    if usuario:
        delete = input("seguro que desea eliminar este usuario? (s/n): ").lower()
        if delete == "s":
            eliminar_objeto(usuario)
        else:
            print("operación cancelada")
    else:
        print("no se ha encontrado el usuario")

#funcion para modificar un usuario
def modificar_usuario():
    print("Modificar Usuario")
    usuario = buscar_usuario()
    if usuario:
        print("seleccione el atributo que desea cambiar")
        atributo = input("escriba el atributo que desea cambiar: ")
        nuevo_valor = input("ingrese el nuevo valor: ")
    
        if not atributo or not nuevo_valor:
            print("no se ha seleccionado un atributo o valor válido")
            return
    
        setattr(usuario, atributo, nuevo_valor)
        actualizar_objeto(usuario)
    else:
        print("no se ha encontrado al usuario")

#funcion de login para los usuarios
def login_usuario():
    print("########## LOGIN ##########")
    rut = "15.111.222-4"#input("ingrese su RUT: ") de momento no se va a usar input, para pruebas
    tipo_usuario = "administrador" #input("ingrese su tipo de usuario (Estudiante/profesor/administrador): ") de momento no se va a usar input, para pruebas
    usuario = obtener_objeto_login(Usuarios, "rut", rut, "tipo_usuario", tipo_usuario)

    if usuario:
        print(f"Bienvenido {usuario.nombre} {usuario.apellido}\n")
        return usuario
    else:
        print("ingrese un usuario valido porfavor")
        return None

########################################## FUNCIONES PARA EL MENU DE USUARIO ##########################################