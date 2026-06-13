from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.views.incapacidad_router import router as incapacidad_router

app = FastAPI(title="MS-Incapacidades - GestorMed")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(incapacidad_router)

@app.get("/")
def root():
    return {"mensaje": "MS-Incapacidades corriendo correctamente", "microservicio": "ms-incapacidades"}