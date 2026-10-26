#main.py

from sqlmodel import SQLModel

from app.database import engine
from app.models.usuario import Usuario
from app.services.usuario_service import crear_usuario, obtener_usuario_por_email, obtener_usuario_por_id, listar_usuarios


def crear_base_datos()-> None:
    SQLModel.metadata.create_all(engine)
    print("Base de datos creada con existo")



if __name__=="__main__":
    crear_base_datos() 


    new_usuario: Usuario = crear_usuario(
        nombre_completo="Ibar Vivas",
        email="ibar.vivas@cap.com"
    )

    print(new_usuario)


    usuarios = listar_usuarios()


    for usuario in usuarios:
        print(usuario)