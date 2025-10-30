from datos.conexion import Session

sesion = Session()
def actualizar_objeto(objeto):
    try:
        sesion.merge(objeto)
        sesion.commit()
        print("El objeto se ha actualizado correctamente.")
    except Exception as e:
        sesion.rollback()
        print(f"Error al actualizar el objeto: {e}")
    finally:
        sesion.close()