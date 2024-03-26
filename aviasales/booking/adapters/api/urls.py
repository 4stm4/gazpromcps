from django.urls import path

from .views import (
    SearchFlightView,
    FlightInfoView,
    OrderFlightView,
)


urlpatterns = [
    path('search_flight', SearchFlightView.as_view()),
    path('flight_info', FlightInfoView.as_view()),
    path('order_flight', OrderFlightView.as_view())
]
