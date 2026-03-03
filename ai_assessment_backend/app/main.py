from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.log_routes import router as log_router
from app.core.database import engine, Base

app = FastAPI()

# 🔥 Add CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "AI Assessment Backend Running"}

Base.metadata.create_all(bind=engine)

app.include_router(log_router)