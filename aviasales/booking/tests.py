from django.test import TestCase

from aviasales.booking.adapters.database.models import FlightInfo, OrderFlight


class TestViews(TestCase):

    def setUp(self):
        FlightInfo.objects.create(
            number='pa_723',
            aviacompany_name = 'Pobeda airlines',
            seats_cnt = 111,
            price = 3150,
            departure = 'Челябинск',
            destination = 'Москва',
            date = '2024-03-28'
        )

    def test_view_search_flight(self):
        url = '/booking/search_flight?departure=Челябинск&destination=Москва&flight_date=2024-03-28'
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

    def test_view_flight_info(self):
        payload = {
            "number": "pa_723",
            "aviacompany_name": "Pobeda airlines",
            "seats_cnt": 111,
            "price": 3150,
            "departure": "Челябинск",
            "destination": "Москва",
            "date": "2024-03-28"
        }
        resp = self.client.put(
            '/booking/flight_info',
            data=payload,
            content_type='application/json'
        )
        self.assertEqual(resp.status_code, 200)

    def test_view_order_flight(self):
        payload = {
            "flight_number": "pa_723",
            "flight_date": "2024-03-28",
            "seats_cnt": 1
        }
        resp = self.client.post(
            '/booking/order_flight',
            data=payload,
            format='json'
        )
        self.assertEqual(resp.status_code, 200)
