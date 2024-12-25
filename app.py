from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db.database import engine
from db.models import Base
from controllers.controller import router
# import firebase_admin
# from firebase_admin import credentials, firestore

# cred = credentials.Certificate("path/to/serviceAccountKey.json")
# firebase_admin.initialize_app(cred)

# Initialize the FastAPI app
app = FastAPI(
    title="SpotifyToYoutube",
    description="Spotify to Youtube API",
    version="0.1.0",
)

# cred = credentials.Certificate("firebase-credentials.json")
# firebase_admin.initialize_app(cred)
# db = firestore.client()

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        
# CORS configuration
origins = [
    "http://localhost",
    "http://localhost:3000",  # Add your frontend domains here
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)