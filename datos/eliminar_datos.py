from datos.conexion import Session

sesion = Session()

#funcion para eliminar objetos de la bd
def eliminar_objeto(objeto):
    try:
        objeto = sesion.merge(objeto)
        sesion.delete(objeto)
        sesion.commit()
        print("objeto eliminado correctamente")
    except Exception as e:
        sesion.rollback()
        print(f"error al eliminar el objeto: {e}")
    finally:
        sesion.close()
