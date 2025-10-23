from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Sede(Base):
    __tablename__ = 'sede'
    id = Column(Integer, primary_key = True)
    nombre = Column(String(100), nullable = False)
    detalle = Column(String(60), nullable = False)
    direccion = Column(String(100), nullable = False)
    region = Column(String(60), nullable = False)
    comuna = Column(String(60), nullable = False)
    ciudad = Column(String(60), nullable = False)
    codigo_postal = Column(Integer, nullable = True)
    id_universidad = Column(Integer, nullable = False)

