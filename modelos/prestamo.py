from sqlalchemy import Column, Integer, Date, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Prestamo(Base):
    __tablename__ = 'prestamo'
    id_ = Column(Integer, primary_key = True)
    fecha_prestamo = Column(Date, nullable = False)
    fecha_devolucion_estimado = Column(Date, nullable = True)
    fecha_devolucion_real = Column(Date, nullable = False)
    multa = Column(Boolean, nullable = False)
    id_usuario = Column(Integer, nullable = False)
    id_ejemplar = Column(Integer, nullable = False)
