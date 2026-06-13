from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.views.usuario_router import router as usuario_router

app = FastAPI(title="MS-Auth - GestorMed")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(usuario_router)

@app.get("/")
def root():
    return {"mensaje": "MS-Auth corriendo correctamente", "microservicio": "ms-auth"}