from fastapi import APIRouter, Depends, HTTPException, status, Header
from EntornoPeliculas.modelsPydantic import Pelicula
from EntornoPeliculas.models.modelsDB import PeliculaDB
from EntornoPeliculas.tokenGen import verificar_token
from DB.conexion import SessionLocal
from sqlalchemy.orm import Session
from typing import List

router = APIRouter(prefix="/peliculas", tags=["Películas"])

# Dependencia para DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_current_user(token: str = Header(...)) -> dict:
    usuario = verificar_token(token)
    if usuario is None:
        raise HTTPException(status_code=401, detail="Token inválido")
    return usuario

# Crear peliculas
@router.post("/", response_model=dict)
def crear_pelicula(pelicula: Pelicula, db: Session = Depends(get_db)):
    nueva = PeliculaDB(**pelicula.model_dump())
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return {"mensaje": "pelicula guardada", "id": nueva.id}

# endpoint para editar peliculas
@router.put("/{pelicula_id}", response_model=dict)
def editar_pelicula(pelicula_id: int, datos: Pelicula, db: Session = Depends(get_db)):
    peli = db.query(PeliculaDB).filter(PeliculaDB.id == pelicula_id).first()
    if not peli:
        raise HTTPException(status_code=404, detail="pelicula no encontrada")
    for key, value in datos.model_dump().items():
        setattr(peli, key, value)
    db.commit()
    return {"mensaje": "pelicula actualizada"}

#endpoint pa eliminar peliculas (requiere token)
@router.delete("/{pelicula_id}", response_model=dict)
def eliminar_pelicula(pelicula_id: int, db: Session = Depends(get_db), usuario: dict = Depends(get_current_user)):
    peli = db.query(PeliculaDB).filter(PeliculaDB.id == pelicula_id).first()
    if not peli:
        raise HTTPException(status_code=404, detail="pelicula no encontrada")
    db.delete(peli)
    db.commit()
    return {"mensaje": "pelicula eliminada"}

# endpoint para consultar todas las pelis
@router.get("/", response_model=List[Pelicula])
def listar_peliculas(db: Session = Depends(get_db)):
    return db.query(PeliculaDB).all()

# consultar una peli por ID
@router.get("/detalle/{pelicula_id}", response_model=Pelicula)
def obtener_pelicula(pelicula_id: int, db: Session = Depends(get_db)):
    peli = db.query(PeliculaDB).filter(PeliculaDB.id == pelicula_id).first()
    if not peli:
        raise HTTPException(status_code=404, detail="pelicula no encontrada")
    return peli
