from fastapi import APIRouter

router = APIRouter(
    prefix="/productos",
    tags=["Productos"]
)


@router.get("/")
def listar_productos():
    return {
        "mensaje": "Lista de productos de SYSCON",
        "productos": [
            {
                "id": 1,
                "nombre": "Cable UTP Cat 6",
                "categoria": "Cableado",
                "precio": 2.50
            },
            {
                "id": 2,
                "nombre": "Router WiFi",
                "categoria": "Redes",
                "precio": 150.00
            },
            {
                "id": 3,
                "nombre": "Cámara IP",
                "categoria": "Seguridad",
                "precio": 220.00
            }
        ]
    }