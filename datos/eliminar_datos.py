from datos.conexion import Session

sesion = Session()

#funciones para agregar objetos a la bd
def eliminar_usuario_por_rut(usuario):
    if usuario:
        try:
            usuario = sesion.merge(usuario)
            sesion.delete(usuario)
            sesion.commit()
            print(f"el usuario {usuario.nombre} se ha eliminado correctamente")
        except Exception as e:
            sesion.rollback()
            print(f"error al eliminar al ususario: {e}")

        finally:
            sesion.close()
    else:
        print("no se recibió un usuario valido para eliminar")