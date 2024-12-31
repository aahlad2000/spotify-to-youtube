from db.database import SessionLocal 
from db.models import PlatFormIntegrations as PlatformIntegration 
from sqlalchemy.exc import SQLAlchemyError # Assuming schema is imported correctly

db = SessionLocal()



async def post_platform_integration(data):
    try:
        # Convert schema data to the database model
        new_integration = PlatformIntegration(**data.dict())
        async with SessionLocal() as db:  # Create an async session
                db.add(new_integration)      # Add the new entry
                await db.commit()            # Commit the transaction
                await db.refresh(new_integration)
        return new_integration
    except SQLAlchemyError as e:
        # Handle specific SQLAlchemy exceptions
        raise e
    except Exception as e:
        # General exception handling
        raise e

