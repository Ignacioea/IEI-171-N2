from datos.conexion import Session
from sqlalchemy import func

from modelos.usuarios import Usuarios

sesion = Session()

def obtener_lista_objetos(objeto):
    listado_objetos = sesion.query(objeto).all()
    if len(listado_objetos) > 0:
        return listado_objetos
    


def obtener_objeto_individual(objeto, atributo: str, valor,):
        try:
            usuario = sesion.query(objeto).filter(getattr(objeto, atributo) == valor).first()
            return usuario
        except Exception as e:
             print(f"error al buscar el objeto: {e}")
             return None