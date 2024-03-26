"""Репозиторий для работы с данными."""
from datetime import date

from .serializers import FlightInfoSerializer
from .models import FlightInfo


class FlightInfoRepo:
    
    def add(self, data):
        serializer = FlightInfoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        else:
            return serializer.errors

    def update_seats_cnt(self, flight_number: str, flight_date: date, seats_cnt: int):
        flight_info = FlightInfo.objects.filter(number=flight_number, date=flight_date).first()
        if flight_info:
            if flight_info.seats_cnt >= seats_cnt:
                new_seats_cnt = flight_info.seats_cnt - seats_cnt
            else:
                return False
            FlightInfo.objects.filter(number=flight_number, date=flight_date).update(seats_cnt=new_seats_cnt)
            return True
        return False

    def get_by_dep_dest_date(
        self,
        departure: str,
        destination: str,
        date: date
        ):
        flight_info = FlightInfo.objects.filter(
            departure=departure,
            destination=destination,
            date__gte=date,
        ).all()
        return flight_info
