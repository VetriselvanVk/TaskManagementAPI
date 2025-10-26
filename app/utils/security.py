from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt
from app.core.config import SECRET_KEY, ALGORITHM

pwd_context = CryptContext(schemes=["bcrypt_sha256"], deprecated="auto")
MAX_BCRYPT_BYTES = 72


def hash_password(password: str) -> str:
    # truncate password to max 72 bytes for bcrypt
    password_bytes = password.encode("utf-8")[:MAX_BCRYPT_BYTES]
    truncated_password = password_bytes.decode("utf-8", errors="ignore")
    return pwd_context.hash(truncated_password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    password_bytes = plain_password.encode("utf-8")[:MAX_BCRYPT_BYTES]
    truncated_password = password_bytes.decode("utf-8", errors="ignore")
    return pwd_context.verify(truncated_password, hashed_password)

def create_access_token(data: dict, expires_delta: int = 30):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=expires_delta)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
