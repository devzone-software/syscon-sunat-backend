from fastapi import APIRouter, HTTPException

from app.schemas.producto import (
    ProductoCrear,
    ProductoActualizar
)


router = APIRouter(
    prefix="/productos",
    tags=["Productos"]
)


productos = [
    {
        "id": 1,
        "nombre": "Cable UTP Cat 6",
        "categoria": "Cableado",
        "precio": 2.50,
        "stock": 500
    },
    {
        "id": 2,
        "nombre": "Router WiFi",
        "categoria": "Redes",
        "precio": 150.00,
        "stock": 30
    },
    {
        "id": 3,
        "nombre": "Cámara IP",
        "categoria": "Seguridad",
        "precio": 220.00,
        "stock": 15
    }
]


@router.get("/")
def listar_productos():
    return {
        "total": len(productos),
        "productos": productos
    }


@router.get("/{producto_id}")
def obtener_producto(producto_id: int):

    for producto in productos:
        if producto["id"] == producto_id:
            return producto

    raise HTTPException(
        status_code=404,
        detail="Producto no encontrado"
    )


@router.post("/", status_code=201)
def crear_producto(datos: ProductoCrear):

    nuevo_id = max(
        [producto["id"] for producto in productos],
        default=0
    ) + 1

    nuevo_producto = {
        "id": nuevo_id,
        **datos.model_dump()
    }

    productos.append(nuevo_producto)

    return {
        "mensaje": "Producto registrado correctamente",
        "producto": nuevo_producto
    }


@router.put("/{producto_id}")
def actualizar_producto(
    producto_id: int,
    datos: ProductoActualizar
):

    for producto in productos:

        if producto["id"] == producto_id:

            datos_actualizados = datos.model_dump(
                exclude_unset=True
            )

            producto.update(datos_actualizados)

            return {
                "mensaje": "Producto actualizado correctamente",
                "producto": producto
            }

    raise HTTPException(
        status_code=404,
        detail="Producto no encontrado"
    )


@router.delete("/{producto_id}")
def eliminar_producto(producto_id: int):

    for producto in productos:

        if producto["id"] == producto_id:

            productos.remove(producto)

            return {
                "mensaje": "Producto eliminado correctamente"
            }

    raise HTTPException(
        status_code=404,
        detail="Producto no encontrado"
    )