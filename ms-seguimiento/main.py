from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.views.seguimiento_router import router as seguimiento_router

app = FastAPI(title="MS-Seguimiento - GestorMed")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(seguimiento_router)

@app.get("/")
def root():
    return {"mensaje": "MS-Seguimiento corriendo correctamente", "microservicio": "ms-seguimiento"}