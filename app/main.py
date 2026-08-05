from fastapi import FastAPI
from app.api import productos

app = FastAPI(
    title="SYSCON - Sistema de Gestión de Facturas",
    description=(
        "API para gestionar productos, facturas, boletas "
        "y generar reportes de ventas."
    ),
    version="0.1.0"
)

app.include_router(productos.router)


@app.get("/")
def inicio():
    return {
        "sistema": "SYSCON",
        "estado": "Activo",
        "mensaje": "Backend funcionando correctamente"
    }


@app.get("/salud")
def verificar_sistema():
    return {
        "estado": "OK",
        "servicio": "API SYSCON"
    }