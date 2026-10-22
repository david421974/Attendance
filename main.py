from sqlmodel import SQLModel

from app.database import engine
from app.models import *


def crear_base_datos()-> None:
    SQLModel.metadata.create_all(engine)
    print("Base de datos creada con existo")



if __name__=="__main__":
    crear_base_datos()  