from datetime import date
from fastapi import APIRouter, Depends

from app.hotels.dao import HotelDAO
from app.hotels.schemas import HotelsArgs, SHotels

router = APIRouter(
    prefix="/hotels",
    tags=["Отели"],
)


@router.get("/location")
async def get_hotels(location: str, date_from: date, date_to: date):
    result = []
    hotels = {"location": location,
              "date_from": date_from,
              "date_to": date_to,}
    for hotel in await HotelDAO.find_all():
        if location in hotel.location:
            result.append(hotel)
    return result