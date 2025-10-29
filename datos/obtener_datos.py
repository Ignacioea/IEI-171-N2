from datos.conexion import Session
from sqlalchemy import func

from modelos.usuarios import Usuarios

sesion = Session()

def obtener_lista_objetos(objetoo):
    listado_objetos = sesion.query(objetoo).all()
    if len(listado_objetos) > 0:
        return listado_objetos

def obtener_usuario_individual(objeto, rut: str):
        usuario = sesion.query(objeto).filter_by(rut=rut).first()
        return usuario

