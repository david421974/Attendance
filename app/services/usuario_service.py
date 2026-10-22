from typing import List
from this import s

from pydantic import EmailStr
from sqlmodel import Session, select

from app.database import engine
from app.models.usuario import Usuario


def crear_usuario(
    nombre_completo:str,
    email:EmailStr
    ) -> Usuario | None:


    try:
            
        with Session(bind=engine) as session:
            nuevo_usuario= Usuario(
                nombre_completo=nombre_completo,
                email=email
            )
    
            session.add(instance=nuevo_usuario)
            session.commit()
            session.refresh(nuevo_usuario)
            return nuevo_usuario
    
    except Exception as error:
        print(f"Error al crear usuario {error}")
        return None
        # Aquí irá le llamda a loguru, similar a logger.exception("tal tal tal")


def obtener_usuario_por_email(
    email: EmailStr
) -> Usuario | None:

    try:
        with Session(engine) as session:

            sentencia = select(Usuario).where(
                Usuario.email == email
            )

            usuario_buscado: Usuario | None = (
                session.exec(sentencia).first()
            )

            if usuario_buscado is None:
                print(f"No existe ningún usuario con el email {email}")
                return None
            return usuario_buscado

    except Exception as error:
        print(f"Error dentro de obtener_usuario_por_email: {error}")
        return None



def listar_usuarios() ->list[Usuario] | None:
    pass