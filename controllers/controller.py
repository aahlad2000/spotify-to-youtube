from fastapi import APIRouter
from models.platform_integration import post_platform_integration
from db.models import PlatFormIntegrations as PlatformIntegration
import asyncio
from pydantic import BaseModel
from typing import Optional
from fastapi import APIRouter, HTTPException
from sqlalchemy.exc import SQLAlchemyError # Assuming schema is imported correctly
from db.database import SessionLocal

class PlatformIntegrationSchema(BaseModel):
    id: Optional[int]
    platform_id: int
    access_token: str
    refresh_token: str

    class Config:
        orm_mode = True


router = APIRouter()

# Root route
@router.get("/")
def read_root():
    return {"message": "Welcome to FastAPI Boilerplate!"}


# Example route
@router.get("/api/spotify-link")
def example_endpoint():
    return {"message": "This is an example endpoint!"}

# Health check
@router.post("/databasecheck")
async def database_check(data: PlatformIntegrationSchema):
    try:
        # Convert schema data to the database model
        new_integration = await post_platform_integration(data)
        print("good",new_integration)
    except SQLAlchemyError as e:
        # Handle specific SQLAlchemy exceptions
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    except Exception as e:
        # General exception handling
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")

@router.get("/spotify-webhook")
def health_check():
    return {"status": "OK"}