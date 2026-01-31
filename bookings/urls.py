from django.urls import path
from .views import (
    HomeView,
    SaunaListView,
    MyBookingsView,
    BookingCreateView,
    BookingDeleteView,
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),  
    path('saunas/', SaunaListView.as_view(), name='sauna_list'),
    path('my-bookings/', MyBookingsView.as_view(), name='my_bookings'),
    path('bookings/new/', BookingCreateView.as_view(), name='booking_create'),
    path('bookings/<int:pk>/delete/', BookingDeleteView.as_view(), name='booking_delete'),
]