from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from .serializers import SearchFlightSerializer, FlightInfoSerializer, OrderFlightSerializer
from aviasales.booking.application import FlightInfoService, SearchFlightService
from aviasales.booking.adapters.database import FlightInfoRepo



class SearchFlightView(APIView):
    search_flight_info_service = SearchFlightService(
        flight_info_repo=FlightInfoRepo(),
    )
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        serializer = SearchFlightSerializer(data=request.query_params, many=False)
        if serializer.is_valid():
            flights_info = self.search_flight_info_service.search_by_flight_data(serializer.validated_data)
            result = []
            for flight in flights_info:
                result.append({
                    'number': flight.number,
                    'aviacompany_name': flight.aviacompany_name,
                    'date': flight.date,
                    'seats_cnt': flight.seats_cnt,
                    'price': flight.price,
                    'departure': flight.departure,
                    'destination': flight.destination
                })
            return Response(result, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FlightInfoView(APIView):
    flight_info_service = FlightInfoService(flight_info_repo=FlightInfoRepo())
    permission_classes = [permissions.AllowAny]

    def put(self, request, *args, **kwargs):
        serializer = FlightInfoSerializer(data=request.data, many=False)
        if serializer.is_valid():
            self.flight_info_service.add_flight_info(serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderFlightView(APIView):
    flight_info_service = FlightInfoService(flight_info_repo=FlightInfoRepo())
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = OrderFlightSerializer(data=request.data, many=False)
        if serializer.is_valid():
            serializer.save()
            result = self.flight_info_service.order_flight(serializer.validated_data)
        return Response({'operation_result': result}, status=status.HTTP_200_OK)
