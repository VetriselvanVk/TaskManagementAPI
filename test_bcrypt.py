from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

password = "string"
hashed = pwd_context.hash(password)
print("Hashed:", hashed)

verified = pwd_context.verify(password, hashed)
print("Verified:", verified)
