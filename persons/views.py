from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404  # Add this import
from .models import Customer, Measurement
from .serializers import CustomerSerializer, MeasurementSerializer
from rest_framework import generics

class MeasurementListByCustomerAPIView(generics.ListAPIView):
    serializer_class = MeasurementSerializer

    def get_queryset(self):
        customer_id = self.kwargs.get('customer_id')
        return Measurement.objects.filter(customer__id=customer_id)


class CustomerListCreateAPIView(APIView):
    def get(self, request, format=None):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        print(request.data)
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomerDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        customer = self.get_object(pk)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        customer = self.get_object(pk)
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        customer = self.get_object(pk)
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class MeasurementListCreateAPIView(APIView):
    def get(self, request, format=None):
        measurements = Measurement.objects.all()
        serializer = MeasurementSerializer(measurements, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        print(request.data)
        serializer = MeasurementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MeasurementDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Measurement.objects.get(pk=pk)
        except Measurement.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        measurement = self.get_object(pk)
        serializer = MeasurementSerializer(measurement)
        return Response(serializer.data, status= status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        measurement = self.get_object(pk)
        serializer = MeasurementSerializer(measurement, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        measurement = self.get_object(pk)
        measurement.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
