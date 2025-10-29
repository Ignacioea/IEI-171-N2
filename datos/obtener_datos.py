from datos.conexion import Session
from sqlalchemy import func
from modelos.ejemplar import Ejemplar
from modelos.usuarios import Usuarios
from modelos.libro import Libro



sesion = Session()

def obtener_lista_objetos(objetoo):
    listado_objetos = sesion.query(objetoo).all()
    if len(listado_objetos) > 0:
        return listado_objetos
        
def libro_por_titulo(titulo, sesion):
        return sesion.query(Libro).filter(Libro.titulo.ilike(f"%{titulo}%")).all()


def obtener_ejemplar(id_libro, sesion):
        return sesion.query(Ejemplar).filter(
                Ejemplar.id_libro == id_libro,
                Ejemplar.estado == "Disponible"
        ).all()
        
