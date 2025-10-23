from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Universidades(Base):
    __tablename__ = 'universidad'
    id = Column(Integer, primary_key = True)
    nombre = Column(String(100), nullable = False)
    siglas = Column(String(10), nullable = True)
    tipo = Column(String(20), nullable = False)
    web = Column(String(40), nullable = False)

