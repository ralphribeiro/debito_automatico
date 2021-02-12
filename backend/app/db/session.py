from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core import config

engine = create_engine(config.SQLALCHEMY_DATABASE_URI,
                       pool_pre_ping=True,
                       pool_size=100,
                       max_overflow=50)
                       
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
