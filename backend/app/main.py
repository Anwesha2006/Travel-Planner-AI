from fastapi import FastAPI
from app.database import Base, engine
from app.models import Trip
from app.routers.itinerary import router as itinerary_router
Base.metadata.create_all(bind=engine)
app=FastAPI(
    title="AI Travel Itinerary Builder",
    version="1.0.0",
)
app.include_router(itinerary_router)
@app.get("/")
def root():
    return {"message":"Backend is running!"}