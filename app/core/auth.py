from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt, ExpiredSignatureError
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models.user import User
from dotenv import load_dotenv
from app.utils.response import error_response, success_response
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def verify_token(token: str, db: Session) -> User | dict:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            return {"status": -1, "message": "Invalid token payload" }
    except ExpiredSignatureError:
        return {"status": -1, "message": "Token has expired. Please login again.", "statusCode" : 401}
    except JWTError:
        return {"status": -1, "message": "Invalid token."}

    user = db.query(User).filter(User.email == email).first()
    if not user:
        return {"status": -1, "message": "User not found"}
    return user



def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> User | dict:
    return verify_token(token, db)
    
