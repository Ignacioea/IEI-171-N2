from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Autor(Base):
    __tablename__ = 'autor'
    id = Column(Integer, primary_key = True)
    nombre = Column(String(60), nullable = False)
    apellido = Column(String(60), nullable = False)
    nacionalidad = Column(String(20), nullable = False)
    pseudonimo = Column(String(120), nullable = True)
    biografia = Column(String(255), nullable = False)

