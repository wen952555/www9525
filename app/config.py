import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 使用 Render 提供的 DATABASE_URL 环境变量
DATABASE_URL = os.getenv("DATABASE_URL")

# SQLAlchemy 配置
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()