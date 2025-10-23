from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Biblioteca(Base):
    __tablename__ = 'biblioteca'
    id = Column(Integer, primary_key = True)
    ubicacion = Column(String(80), nullable = False)
    telefono_contacto = Column(String(20), nullable = True)
    correo_contacto = Column(String(100), nullable = False)
    horario_atencion = Column(String(255), nullable = False)
    id_sede = Column(Integer, nullable = False)
    id_libro = Column(Integer, nullable = False)

