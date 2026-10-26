from pydantic import EmailStr
from sqlmodel import Session, select

from app.database import engine
from app.models.usuario import Usuario


def crear_usuario(
    nombre_completo:str,
    email:EmailStr
    ) -> Usuario:


            
    with Session(bind=engine) as session:
        nuevo_usuario= Usuario(
            nombre_completo=nombre_completo,
            email=email
        )

        session.add(instance=nuevo_usuario)
        session.commit()
        session.refresh(nuevo_usuario)
        return nuevo_usuario



def obtener_usuario_por_email(
    email: EmailStr
) -> Usuario | None:


    with Session(engine) as session:

        sentencia = select(Usuario).where(
            Usuario.email == email
        )

        usuario_buscado: Usuario | None = (
            session.exec(sentencia).first()
        )

        return usuario_buscado



def listar_usuarios() ->list[Usuario]:
    
    with Session(engine) as session:

        sentencia = select(Usuario)

        usuarios:list[Usuario] = list(
            session.exec(sentencia)
        )
        return usuarios


def obtener_usuario_por_id(
    id_usuario:int
    )-> Usuario | None:

    with Session(engine) as session:
        
        sentencia_id = select(Usuario).where(
            Usuario.id == id_usuario
        )

        usuario_por_id: Usuario | None = session.exec(
            sentencia_id
        ).first()
        return usuario_por_id


