from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config import database

database_url = f"mysql+pymysql://{database['user']}:{database['password']}@{database['host']}:{database['port']}/"
if(database['env'] == 'development'):
    engine_no_db = create_engine(database_url, echo=True)
    with engine_no_db.connect() as conn:
        conn.execute(text(f"create database if not exists {database['name']}"))
        conn.commit()
DATABASE_URL = database_url + database['name']

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()