from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class PeliculaDB(Base):
    __tablename__ = "peliculas"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    genero = Column(String, nullable=False)
    anio = Column(Integer, nullable=False)
    clasificacion = Column(String(1), nullable=False)
