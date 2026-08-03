from pydantic import BaseModel
from datetime import date,datetime
class TripCreate(BaseModel):
    destination: str
    budget: int
    travel_style: str
    start_date: date
    end_date: date
    number_of_travelers: int
class TripResponse(BaseModel):
    id: int

    destination: str

    budget: int

    travel_style: str

    itinerary: str

    created_at: datetime

    class Config:
     from_attributes = True