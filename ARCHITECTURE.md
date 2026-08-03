# Diagrama de archivos y arquitectura - syscon-sunat-backend

Este documento describe la organización de archivos y la arquitectura del proyecto "syscon-sunat-backend".

## Árbol de archivos

syscon-sunat-backend/
├── app/
│   ├── main.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── productos.py
│   │   ├── comprobantes.py
│   │   ├── reportes.py
│   │   └── sunat.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── producto.py
│   │   └── comprobante.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── producto.py
│   │   └── comprobante.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── xml_service.py
│   │   └── sunat_service.py
│   └── database/
│       ├── __init__.py
│       └── connection.py
├── tests/
│   └── test_main.py
├── .env
├── .gitignore
├── README.md
└── requirements.txt

---

## Descripción de componentes

- app/main.py
  - Punto de entrada de la aplicación. Configura el servidor, registra rutas y middleware, y arranca la aplicación.

- app/api/
  - Contiene los routers/endpoints agrupados por dominio:
    - productos.py: rutas relacionadas con la gestión de productos (CRUD, listados).
    - comprobantes.py: rutas para crear, listar y obtener comprobantes (facturas, boletas, etc.).
    - reportes.py: endpoints para generación de reportes y consultas analíticas.
    - sunat.py: endpoints que interactúan directamente con la SUNAT o exponen integraciones específicas.

- app/models/
  - Definición de modelos de dominio (POCOs o modelos ORM) usados para persistencia y negocio:
    - producto.py: modelo de producto.
    - comprobante.py: modelo de comprobante/factura.

- app/schemas/
  - Esquemas de validación / serialización (p. ej. pydantic) que definen las estructuras de entrada y salida:
    - producto.py
    - comprobante.py

- app/services/
  - Lógica de negocio y utilidades:
    - xml_service.py: generación/parsing de XML (p. ej. para formatos exigidos por SUNAT).
    - sunat_service.py: comunicación con servicios de la SUNAT (envío de comprobantes, recepción de respuestas, conciliación).

- app/database/connection.py
  - Configuración de la conexión a la base de datos y utilidades para obtener sesiones/clients.

- tests/test_main.py
  - Pruebas unitarias/funcionales iniciales para verificar la integración básica o comportamiento de la app.

- .env
  - Variables de entorno (credenciales, urls, configuraciones específicas del entorno).

- requirements.txt
  - Dependencias del proyecto.

---

## Diagrama de arquitectura (Mermaid)

A continuación un diagrama Mermaid que muestra la relación entre los componentes. GitHub renderiza Mermaid en PRs y VS Code puede hacerlo con extensiones ("Markdown Preview Mermaid Support").

```mermaid
flowchart LR
    Client[Cliente / Frontend / Integrador]
    Main[app/main.py\n(Entrypoint)]

    subgraph API[API - Routers]
      Productos[/app/api/productos.py/]
      Comprobantes[/app/api/comprobantes.py/]
      Reportes[/app/api/reportes.py/]
      SunatApi[/app/api/sunat.py/]
    end

    subgraph Services[Servicios]
      XML[xml_service.py]\n(XML generación/parsing)
      SUNAT[sunat_service.py]\n(Comunicación con SUNAT)
    end

    subgraph Domain[Dominio]
      Models[app/models]\n(productos, comprobantes)
      Schemas[app/schemas]\n(validación/serialización)
    end

    DB[Base de datos\n(app/database/connection.py)]

    Client -->|HTTP| Main
    Main --> API
    API --> Productos
    API --> Comprobantes
    API --> Reportes
    API --> SunatApi

    Productos --> Schemas
    Productos --> Models

    Comprobantes --> Schemas
    Comprobantes --> Models
    Comprobantes --> XML

    SunatApi --> SUNAT
    SUNAT --> XML
    SUNAT --> DB

    XML -->|usa| Models
    API -->|lee/escribe| DB
    Models --> DB

    Reportes --> DB

    classDef infra fill:#f9f,stroke:#333,stroke-width:1px;
    class DB infra
```

---

## Diagrama ASCII (respaldo)

Client --> app/main.py --> [Routers: productos, comprobantes, reportes, sunat]

Routers --> Services (xml_service, sunat_service)
Routers --> Schemas & Models
Models & Services <--> Database (app/database/connection.py)

---

## Cómo visualizar el diagrama Mermaid

- En VS Code: abrir el archivo ARCHITECTURE.md y usar "Open Preview". Si no se muestra Mermaid, instalar la extensión "Markdown Preview Mermaid Support" o usar la vista de GitHub.
- En GitHub: subir el archivo y visualizarlo (GitHub renderiza Mermaid en MD en muchas ubicaciones). Si no se renderiza, usar un previewer Mermaid en línea copiando el bloque mermaid.

---

Si quieres, puedo:
- Generar un diagrama PNG/SVG y añadirlo al repositorio (por ejemplo en docs/diagram.png).
- Extender el diagrama con flujos de datos más detallados (autenticación, colas, cache, etc.).
- Ajustar nombres y descripciones si prefieres términos concretos (por ejemplo, especificar que se usa FastAPI, SQLAlchemy, pydantic, etc.).

Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>
