from fastapi import FastAPI
from app.api.productos import router as productos_router

app = FastAPI(
    title="SYSCON SUNAT API",
    description="Sistema de gestión y análisis de ventas",
    version="1.0.0"
)

app.include_router(productos_router)


@app.get("/")
def inicio():
    return {
        "mensaje": "Backend de SYSCON funcionando correctamente"
    }