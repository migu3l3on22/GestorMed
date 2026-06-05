from fastapi import FastAPI
from app.views.seguimiento_router import router as seguimiento_router

app = FastAPI(title="MS-Seguimiento - GestorMed")

app.include_router(seguimiento_router)

@app.get("/")
def root():
    return {"mensaje": "MS-Seguimiento corriendo correctamente", "microservicio": "ms-seguimiento"}