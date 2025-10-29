from datos.conexion import Session

sesion = Session()

#funcion para agregar objetos a la bd
def insertar_objeto(objeto):
    sesion.add(objeto)
    try:
        sesion.commit()
        print(f"el objeto se ha guardado correctamente.")
    except Exception as e:
        sesion.rollback()
        print(f"error al guardar el objeto: {e}")
    finally:
        sesion.close()