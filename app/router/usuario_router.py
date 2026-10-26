from pygments.styles.night_owl import NightOwlStyle
from fastapi import APIRouter

from app.models.usuario import Usuario
from app.services.usuario_service import listar_usuarios, obtener_usuario_por_email, obtener_usuario_por_id


router = APIRouter(
    prefix="/usuarios",
    tags=["Usuarios"]
)



@router.get("")
def get_usuarios()-> list[Usuario]:
    return listar_usuarios()



@router.get("/{id_usuario}")
def get_usuario_por_id(
    id_usuario:int
    )-> Usuario | None:


    return obtener_usuario_por_id(
        id_usuario
    )
    

    