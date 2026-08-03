from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Trip
from app.schemas.trip import TripCreate, TripResponse
from app.services.gemini_service import generate_itinerary

router = APIRouter(
    prefix="/itinerary",
    tags=["Itinerary"]
)


@router.post("/generate-trip", response_model=TripResponse)
def create_trip(
    trip: TripCreate,
    db: Session = Depends(get_db)
):

    ai_response = generate_itinerary(
        destination=trip.destination,
        budget=trip.budget,
        travel_style=trip.travel_style,
        start_date=trip.start_date,
        end_date=trip.end_date,
        number_of_travelers=trip.number_of_travelers,
    )

    new_trip = Trip(
        destination=trip.destination,
        budget=trip.budget,
        travel_style=trip.travel_style,
        start_date=trip.start_date,
        end_date=trip.end_date,
        number_of_travelers=trip.number_of_travelers,
        itinerary=ai_response,
    )

    db.add(new_trip)
    db.commit()
    db.refresh(new_trip)

    return new_trip