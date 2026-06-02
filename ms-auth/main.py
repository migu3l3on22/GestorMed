from fastapi import FastAPI
from app.views.usuario_router import router as usuario_router

app = FastAPI(title="MS-Auth - GestorMed")

app.include_router(usuario_router)

@app.get("/")
def root():
    return {"mensaje": "MS-Auth corriendo correctamente", "microservicio": "ms-auth"}