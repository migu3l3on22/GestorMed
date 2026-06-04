from fastapi import FastAPI
from app.views.empleado_router import router as empleado_router

app = FastAPI(title="MS-Empleados - GestorMed")

app.include_router(empleado_router)

@app.get("/")
def root():
    return {"mensaje": "MS-Empleados corriendo correctamente", "microservicio": "ms-empleados"}