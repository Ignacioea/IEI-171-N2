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
    
def insertar_libro(titulo, editorial, anio, categoria, ISBN, id_autor, id_biblioteca):
    nuevo_libro = Libro(
        titulo = titulo,
        editorial = editorial,
        anio = anio,
        categoria = categoria,
        ISBN = ISBN,
        id_autor = id_autor,
        id_biblioteca = id_biblioteca)
    sesion.add(nuevo_libro)
    try:
        sesion.commit()
        print(f"el libro {nuevo_libro.titulo} se ha registrado correctamente!.")
    
    except Exception as e:
        sesion.rollback()
        print(f"error al registrar el libro: {e}")
    finally:
        sesion.close()

def insertar_ejemplar(codigo, ubicacion, estado, id_libro):
    nuevo_ejemplar = Ejemplar(
        codigo = codigo,
        ubicacion = ubicacion,
        estado = estado,
        id_libro = id_libro
    )
    sesion.add(nuevo_ejemplar)
    try:
        sesion.commit()
        print(f"el ejemplar {nuevo_ejemplar.codigo} se ha registrado correctamente!.")
    except Exception as e:
        sesion.rollback()
        print(f"error al registrar el ejemplar: {e}")
    finally:
        sesion.close()
