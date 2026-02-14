from django.urls import path
from .views import (
    HomeView,
    SaunaView,
    MyBookingsView,
    BookingCreateView,
    BookingUpdateView,
    BookingDeleteView,
    validate_booking_form,
    )

urlpatterns = [
    path('', HomeView.as_view(), name='home'), 
    path('sauna/', SaunaView.as_view(), name='sauna'),
    path('my-bookings/', MyBookingsView.as_view(), name='my_bookings'),
    path('validate/', validate_booking_form, name='validate_booking_form'),
    path('bookings/new/', BookingCreateView.as_view(), name='booking_create'),
    path('bookings/<int:pk>/edit/', BookingUpdateView.as_view(), name='booking_update'),
    path('bookings/<int:pk>/delete/', BookingDeleteView.as_view(), name='booking_delete'),
]