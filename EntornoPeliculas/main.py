from fastapi import FastAPI
from fastapi.responses import JSONResponse
from EntornoPeliculas.routers import peliculas, auth
from DB.conexion import crear_tablas

app = FastAPI(
    title="API de Películas",
    description="ayuda esto no es un meme PRECIADO MARTINEZ URIEL IVAN",
    version="1.0.0"
)

# Crea las tablas de la BD
crear_tablas()

app.include_router(auth.router)
app.include_router(peliculas.router)

@app.get('/', tags=['Inicio'])
def main():
    return {'hola FastApi''Preciado'}