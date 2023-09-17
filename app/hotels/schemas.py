from datetime import date
from pydantic import BaseModel


class SHotels(BaseModel):
    id: int
    name: str
    location: str
    services: str
    rooms_quantity: int
    image_id: int
    rooms_left: int
    
    
class HotelsArgs:
    def __init__(
        self,
        location: str,
        date_from: date,
        date_to: date,
    ):
        self.location = location
        self.date_from = date_from
        self.date_to = date_to
    