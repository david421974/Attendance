#app/models/usuario.py
from pydantic import EmailStr
from sqlmodel import Field, SQLModel


class Usuario(SQLModel, table=True):

    __tablename__="usuarios"

    id:int | None = Field(
        default=None,
        primary_key= True
    )
    nombre_completo:str | None = Field(
        max_length=50,
        index=True
    )
    email:EmailStr = Field(
        unique=True,
        index=True
    )

    activo:bool= True

