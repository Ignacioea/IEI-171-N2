from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Ejemplar(Base):
    __tablename__ = 'ejemplar'
    id = Column(Integer, primary_key = True)
    codigo = Column(String(50), nullable = False)
    ubicacion = Column(String(60), nullable = True)
    estado = Column(String(30), nullable = False)
    id_libro = Column(Integer, nullable = False)