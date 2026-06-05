from fastapi import FastAPI
from app.views.incapacidad_router import router as incapacidad_router

app = FastAPI(title="MS-Incapacidades - GestorMed")

app.include_router(incapacidad_router)

@app.get("/")
def root():
    return {"mensaje": "MS-Incapacidades corriendo correctamente", "microservicio": "ms-incapacidades"}