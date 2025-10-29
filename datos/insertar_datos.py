from modelos.prestamo import Prestamo
from modelos.usuarios import Usuarios
from modelos.libro import Libro
from modelos.ejemplar import Ejemplar
from datos.conexion import Session


sesion = Session()

#funciones para agregar objetos a la bd
def insertar_usuario(nombre, apellido, rut, telefono, correo, sancionado, tipo_usuario):
    nuevo_usuario = Usuarios(
        nombre = nombre,
        apellido = apellido,
        rut = rut,
        telefono = telefono,
        correo = correo,
        sancionado = sancionado,
        tipo_usuario = tipo_usuario)
    sesion.add(nuevo_usuario)
    try:
        sesion.commit()
        print(f"el usuario {nuevo_usuario.nombre} se ha registrado correctamente")
    except Exception as e:
        sesion.rollback()
        print(f"error al registrar al ususario: {e}")

    finally:
        sesion.close()
    
