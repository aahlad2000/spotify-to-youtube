from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
import asyncio

# Load environment variables
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Async database engine
engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Dependency for FastAPI endpoints to get DB sessions
async def get_db():
    async with SessionLocal() as session:
        yield session

# Function to test the database connection
# async def test_db_connection():
#     async with SessionLocal() as session:
#         # Perform a simple query or operation to test the connection
#         result = await session.execute("SELECT 1")
#         print(result.scalar())

# if __name__ == "__main__":
#     asyncio.run(test_db_connection())