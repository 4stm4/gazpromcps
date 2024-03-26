from django.db import models


class FlightInfo(models.Model):
    """Сущность для добавления рейса в БД."""
    number = models.CharField(max_length=15)    # номер рейса
    aviacompany_name = models.CharField(max_length=50)    # название авиавкомпании
    date = models.DateField()    # дата выполнения полёта
    seats_cnt = models.IntegerField()    # количесвто посадочных мест
    price = models.IntegerField()    # стоимость перелёта
    departure = models.CharField(max_length=50)    # город отправления
    destination = models.CharField(max_length=50)    # город прибытия


class OrderFlight(models.Model):
    """Сущность для хранения заказов билетов в БД."""
    flight_number = models.CharField(max_length=15)    # номер рейса
    seats_cnt = models.IntegerField()    # количесвто посадочных мест
    flight_date = models.DateField()    # дата выполнения полёта
