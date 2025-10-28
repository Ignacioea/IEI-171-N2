from prettytable import PrettyTable
from datos.obtener_datos import obtener_lista_objetos
from modelos.usuarios import Usuarios
from datos.insertar_datos import insertar_usuario


def mostrar_usuarios():
    tabla_usuarios = PrettyTable()
    tabla_usuarios.field_names = ['id','nombre','apellido','rut','telefono','correo','sancionado', 'tipo de usuario']
    lista_usuarios = obtener_lista_objetos(Usuarios)
    if lista_usuarios:
        for usuario in lista_usuarios:
            tabla_usuarios.add_row(
                [usuario.id, usuario.nombre, usuario.apellido, usuario.rut, usuario.telefono, usuario.correo, usuario.sancionado, usuario.tipo_usuario])
        print(tabla_usuarios)

def registrar_usuario():
    print("Registro de Nuevo Usuario \n")
    nombre = input("ingrese nombre: ")
    apellido = input("ingrese apellido: ")
    rut = input("ingrese rut (sin puntos ni guión): ")
    telefono = input("ingrese su numero: ")
    correo = input("ingrese su correo electrónico: ")
    sancionado = False #por ser usuario nuevo la sanción directamente es False
    tipo_usuario = input("imgrese si es estudiante/profesor/administrador: ")
    insertar_usuario(nombre, apellido, rut, telefono, correo, sancionado, tipo_usuario)

