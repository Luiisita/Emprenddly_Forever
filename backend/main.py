# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db import Base, engine
from auth import router as auth_router

app = FastAPI(title="Auth mínimo Emprenddly")

# Crear tablas
Base.metadata.create_all(bind=engine)

# Configurar CORS 
origins = [
    "http://localhost:5173",  # Vite
    "http://127.0.0.1:5500",  # Live Server
    "http://localhost:5500",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir rutas de autenticación
app.include_router(auth_router)

@app.get("/")
def root():
    return {"status": "ok", "message": "Bienvenido a Emprenddly API 🚀"}
