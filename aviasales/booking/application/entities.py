"""Сущности для сервиса."""
from dataclasses import dataclass
from datetime import date


@dataclass
class SearchFlight:
    """Сущность входных параметров для поиска рейса."""
    departure: str    # город отправления
    destination: str    # город прибытия
    flight_date: date   # предполагаемая дата выполнения полёта

@dataclass
class FlightInfo:
    """Сущность входных параметров для добавления рейса."""
    number: str    # номер рейса
    aviacompany_name: str    # название авиавкомпании
    date: date    # дата выполнения полёта
    seats_cnt: int    # количесвто посадочных мест
    price: int    # стоимость перелёта
    departure: str    # город отправления
    destination: str    # город прибытия

@dataclass
class OrderFlight:
    """Сущность входных параметров для заказа билетов на рейс."""
    flight_number: str    # номер рейса
    flight_date: date    # дата выполнения полёта
    seats_cnt: int    # количесвто посадочных мест
