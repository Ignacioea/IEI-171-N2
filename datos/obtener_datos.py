from datos.conexion import Session
from sqlalchemy import func

sesion = Session()

def obtener_lista_objetos(objetoo):
    listado_objetos = sesion.query(objetoo).all()
    if len(listado_objetos) > 0:
        return listado_objetos
        
