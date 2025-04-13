from pydantic import BaseModel, Field
from typing import Literal

class Pelicula(BaseModel):
    titulo: str = Field(min_length=2)
    genero: str = Field(min_length=4)
    anio: int = Field(ge=1000, le=9999) #no jala si le pongo aÑo jasjaja
    clasificacion: Literal["A", "B", "C"]
