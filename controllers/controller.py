from fastapi import APIRouter

router = APIRouter()

# Root route
@router.get("/")
def read_root():
    return {"message": "Welcome to FastAPI Boilerplate!"}


# Example route
@router.get("/api/example")
def example_endpoint():
    return {"message": "This is an example endpoint!"}

# Health check
@router.get("/health")
def health_check():
    return {"status": "OK"}