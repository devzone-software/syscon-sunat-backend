from fastapi import APIRouter

router = APIRouter(
    prefix="/productos",
    tags=["Productos"]
)


@router.get("/")
def listar_productos():
    return [
        {
            "id": 1,
            "nombre": "Cable UTP Cat 6",
            "categoria": "Cableado",
            "cantidad_vendida": 850
        },
        {
            "id": 2,
            "nombre": "Router TP-Link",
            "categoria": "Redes",
            "cantidad_vendida": 240
        },
        {
            "id": 3,
            "nombre": "Cámara IP",
            "categoria": "Seguridad",
            "cantidad_vendida": 185
        }
    ]