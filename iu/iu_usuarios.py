def ingresar_datos_usuarios():
    print("Registro de Nuevo Usuario \n")
    nombre = input("ingrese nombre: ")
    apellido = input("ingrese apellido: ")
    rut = input("ingrese rut (sin puntos ni guión): ")
    telefono = input("ingrese su numero: ")
    correo = input("ingrese su correo electrónico: ")
    sancionado = False #por ser usuario nuevo la sanción directamente es False
    tipo_usuario = input("ingrese si es estudiante/profesor/administrador: ")
    return{
        "nombre":nombre,
        "apellido": apellido,
        "rut":rut,
        "telefono": telefono,
        "correo": correo,
        "sancionado": sancionado,
        "tipo_usuario":tipo_usuario 
    }

def ingresar_rut_usuario():
    rut = input("ingrese el RUT del usuario: ")
    return rut

def ingresar_valor_atributo():
    print("seleccione el atributo que desea cambiar")
    atributo = input("escriba el atributo que desea cambiar: ")
    nuevo_valor = input("ingrese el nuevo valor: ")
    return{
        "atributo": atributo,
        "nuevo_valor": nuevo_valor
    }

def ingresar_login():
    print("########## LOGIN ##########")
    rut = input("ingrese su RUT: ")
    tipo_usuario = input("ingrese su tipo de usuario (Estudiante/profesor/administrador): ")
    return {
        "rut": rut,
        "tipo_usuario": tipo_usuario
        }
            
