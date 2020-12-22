from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core import config

engine = create_engine(config.SQLALCHEMY_DATABASE_URI,
                       pool_pre_ping=True,
                       pool_size=20,
                       max_overflow=20,
                       pool_recycle=60)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
