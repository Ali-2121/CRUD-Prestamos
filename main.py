'''Maiin donde inicia la app y se traen los endpoints'''
from fastapi import FastAPI
from routes.users import user
from routes.materials import material
from routes.prestamos import prestamo
app = FastAPI(
    title="Prestamos S.A. de C.V",
    description="API de prueba para almacenar registros de prestamo de material"
)

app.include_router(user)
app.include_router(material)
app.include_router(prestamo)
