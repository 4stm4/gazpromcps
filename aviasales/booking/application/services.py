"""Сервис приложения с бизнес логикой."""
from typing import Any

from .entities import SearchFlight, FlightInfo, OrderFlight
from .interfaces import FlightInfoRepo


class SearchFlightService:
    flight_info_repo: FlightInfoRepo

    def __init__(self, flight_info_repo: FlightInfoRepo):
        self.flight_info_repo = flight_info_repo

    def search_by_flight_data(self, search_request: SearchFlight):
        flights_info = self.flight_info_repo.get_by_dep_dest_date(
            departure=search_request['departure'],
            destination=search_request['destination'],
            date=search_request['flight_date'],
        )
        return flights_info


class FlightInfoService:
    flight_info_repo: FlightInfoRepo

    def __init__(self, flight_info_repo: FlightInfoRepo):
        self.flight_info_repo = flight_info_repo

    def add_flight_info(self, flight_info: FlightInfo):
        self.flight_info_repo.add(data=flight_info)

    def order_flight(self, order_flight: OrderFlight):
        return self.flight_info_repo.update_seats_cnt(
            flight_number=order_flight['flight_number'],
            flight_date=order_flight['flight_date'],
            seats_cnt=order_flight['seats_cnt'],
        )
