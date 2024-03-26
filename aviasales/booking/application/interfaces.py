"""Интерфейс работы с хранилищем данных."""
from abc import ABC, abstractmethod

from datetime import date


class FlightInfoRepo(ABC):
    
    @abstractmethod
    def add(self, data):
        ...

    @abstractmethod
    def update_seats_cnt(self, flight_number: str, flight_date: date, seats_cnt: int):
        ...

    @abstractmethod
    def get_by_dep_dest_date(
        self,
        departure: str,
        destination: str,
        date: date
        ):
        ...
