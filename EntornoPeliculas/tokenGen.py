from datetime import datetime, timedelta
from jose import JWTError, jwt


SECRET_KEY = "clavesecretadeprueba"
ALGORITHM = "HS256"
EXPIRATION_MINUTES = 60

def crear_token(data: dict):
    to_encode = data.copy()
    from datetime import timezone
    expire = datetime.now(timezone.utc) + timedelta(minutes=EXPIRATION_MINUTES)
    to_encode.update({"exp": expire})
    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return token

def verificar_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None
