from fastapi import APIRouter, HTTPException
from EntornoPeliculas.tokenGen import crear_token

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login")
def login(username: str, password: str):
    
    if username == "admin" and password == "123":
        token = crear_token({"usuario": username})
        return {"access_token": token}
    raise HTTPException(status_code=401, detail="Credenciales incorrectas")
