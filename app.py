from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db.database import engine
from db.models import Base
# Initialize the FastAPI app
app = FastAPI(
    title="SpotifyToYoutube",
    description="Spotify to Youtube API",
    version="0.1.0",
)
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

# Root route
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI Boilerplate!"}


# Example route
@app.get("/api/example")
def example_endpoint():
    return {"message": "This is an example endpoint!"}

# Health check
@app.get("/health")
def health_check():
    return {"status": "OK"}