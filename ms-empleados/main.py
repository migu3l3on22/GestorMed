from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.views.empleado_router import router as empleado_router

app = FastAPI(title="MS-Empleados - GestorMed")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(empleado_router)

@app.get("/")
def root():
    return {"mensaje": "MS-Empleados corriendo correctamente", "microservicio": "ms-empleados"}