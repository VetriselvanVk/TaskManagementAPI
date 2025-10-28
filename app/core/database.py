from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import DATABASE_URL
from app.models.user import Base  # Import models AFTER config

# Create SQLAlchemy engine
engine = create_engine(
    DATABASE_URL,
    pool_size=2,         # max active connections
    max_overflow=0,      # extra connections beyond pool_size
    pool_pre_ping=True   # test connections before use
)
# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create tables
Base.metadata.create_all(bind=engine)
