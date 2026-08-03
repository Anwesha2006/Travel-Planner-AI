from sqlalchemy import Column, Integer, String, Date, Text, DateTime
from app.database import Base
from datetime import datetime
class Trip(Base):
    __tablename__="trips"
    id=Column(Integer,primary_key=True,index=True)
    destination=Column(String(255),nullable=False)
    budget=Column(Integer,nullable=False)
    travel_style=Column(String(255),nullable=False)
    start_date=Column(Date,nullable=False)
    end_date=Column(Date,nullable=False)
    number_of_travelers=Column(Integer)
    itinerary=Column(Text)
    created_at=Column(DateTime,nullable=False,default=datetime.now)