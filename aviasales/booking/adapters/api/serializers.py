from rest_framework import serializers

from aviasales.booking.adapters.database.models import OrderFlight

class SearchFlightSerializer(serializers.Serializer):
    """Сущность валидации входных параметров для поиска рейса."""
    departure = serializers.CharField(max_length=50)    # город отправления
    destination = serializers.CharField(max_length=50)    # город прибытия
    flight_date = serializers.DateField()    # дата выполнения полёта


class FlightInfoSerializer(serializers.Serializer):
    """Сущность валидации входных параметров для добавления рейса."""
    number = serializers.CharField(max_length=15)    # номер рейса
    aviacompany_name = serializers.CharField(max_length=50)    # название авиавкомпании
    date = serializers.DateField()    # дата выполнения полёта
    seats_cnt = serializers.IntegerField()    # количесвто посадочных мест
    price = serializers.IntegerField()    # стоимость перелёта
    departure = serializers.CharField(max_length=50)    # город отправления
    destination = serializers.CharField(max_length=50)    # город прибытия

class OrderFlightSerializer(serializers.ModelSerializer):
    """Сущность валидации входных параметров для заказа билетов на рейс."""
    class Meta:
        model = OrderFlight
        fields = ['flight_number', 'seats_cnt', 'flight_date']
