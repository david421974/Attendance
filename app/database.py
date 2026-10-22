from sqlmodel import create_engine

DATABASE_URL = "sqlite:///database/attendance.db"

engine= create_engine(
    DATABASE_URL,
    echo=True,
)

