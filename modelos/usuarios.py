from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Usuarios(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key = True)
    nombre = Column(String(60), nullable = False)
    apellido = Column(String(60), nullable = False)
    rut = Column(String(15), nullable = False)
    telefono = Column(String(15), nullable = True)
    correo = Column(String(255), nullable = False)
    sancionado = Column(Boolean, nullable = False)
    tipo_usuario = Column(String(20), nullable = False)
