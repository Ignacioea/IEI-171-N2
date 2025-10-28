from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Libro(Base):
    __tablename__ = 'libro'
    id = Column(Integer, primary_key = True)
    titulo = Column(String(255), nullable = False)
    editorial = Column(String(50), nullable = False)
    anio_publicacion = Column(Date, nullable = False)
    categoria = Column(String(40), nullable = False)
    ISBN = Column(String(13), nullable = False)
    id_autor = Column(Integer, nullable = False)
    id_biblioteca = Column(Integer, nullable = False)
