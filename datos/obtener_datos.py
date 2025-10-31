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
            seleccionado = sesion.query(objeto).filter(getattr(objeto, atributo) == valor).first()
            return seleccionado
        except Exception as e:
             print(f"error al buscar el objeto: {e}")
             return None
        finally:
             sesion.close()
        
def obtener_objeto_login(objeto, atributo: str, valor, atributo2: str, valor2):
    try:
          seleccionado = sesion.query(objeto).filter(getattr(objeto, atributo) == valor,
                                                     getattr(objeto, atributo2) == valor2).first()
          return seleccionado
    except Exception as e:
          print(f"Error al encontrar al usuario: {e}")
          return None
    finally:
         sesion.close()

def obtener_objeto_join(objeto1, objeto2, atributo1, atributo2):
    try:
        join = sesion.query(objeto1, objeto2).join(objeto2, getattr(objeto1, atributo1) == getattr(objeto2, atributo2)).all()
        return join
    except Exception as e:
         print(f"error al buscar el objeto: {e}")
         return None
    finally:
         sesion.close()