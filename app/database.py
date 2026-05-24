from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config import database

DATABASE_URL = f"postgresql://{database['user']}:{database['password']}@{database['host']}:{database['port']}/{database['name']}"
    
engine = create_engine(DATABASE_URL,
                       pool_size=10,
                       max_overflow=20,
                       pool_pre_ping=True,
                        echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()