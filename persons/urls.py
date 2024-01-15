# urls.py
from django.urls import path
from .views import (
    CustomerListCreateAPIView,
    CustomerDetailAPIView,
    MeasurementListCreateAPIView,
    MeasurementDetailAPIView,
    MeasurementListByCustomerAPIView  # Add this import
)
urlpatterns = [
    path('api/v1/customers/', CustomerListCreateAPIView.as_view(), name='customer-list-create'),
    path('api/v1/customers/<int:pk>/', CustomerDetailAPIView.as_view(), name='customer-detail'),
    path('api/v1/measurements/', MeasurementListCreateAPIView.as_view(), name='measurement-list-create'),
    path('api/v1/measurements/<int:pk>/', MeasurementDetailAPIView.as_view(), name='measurement-detail'),
    path('api/v1/measurements/customer/<int:customer_id>/', MeasurementListByCustomerAPIView.as_view(), name='measurement-list-by-customer'),
]
