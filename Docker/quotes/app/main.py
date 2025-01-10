from fastapi import FastAPI
import os

from .models import quote
from .routers import quote

# Database connection
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Get variables from .env file
USER = os.getenv("POSTGRES_USER")
PASSWORD = os.getenv("POSTGRES_PASSWORD")
HOST = os.getenv("POSTGRES_HOST")
DATABASE = os.getenv("POSTGRES_DB")

# Check if the variables are set
if not USER:
    raise ValueError("POSTGRES_USER is not set")
if not PASSWORD:
    raise ValueError("POSTGRES_PASSWORD is not set")
if not HOST:
    raise ValueError("POSTGRES_HOST is not set")
if not DATABASE:
    raise ValueError("POSTGRES_DB is not set")

SQLALCHEMY_DATABASE_URL = f"postgresql://{USER}:{PASSWORD}@{HOST}/{DATABASE}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

app = FastAPI()

app.include_router(quote.router)
