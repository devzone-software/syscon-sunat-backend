from pydantic import BaseModel, Field


class ProductoCrear(BaseModel):
    nombre: str = Field(
        min_length=3,
        max_length=150,
        description="Nombre del producto"
    )

    categoria: str = Field(
        min_length=3,
        max_length=100,
        description="Categoría del producto"
    )

    precio: float = Field(
        gt=0,
        description="Precio del producto"
    )

    stock: int = Field(
        ge=0,
        description="Cantidad disponible"
    )


class ProductoActualizar(BaseModel):
    nombre: str | None = None
    categoria: str | None = None
    precio: float | None = None
    stock: int | None = None