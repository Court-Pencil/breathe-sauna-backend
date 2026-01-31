from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView

from .forms import BookingForm
from .models import Booking, Sauna

class HomeView(TemplateView):
    template_name = 'bookings/home.html'

class SaunaListView(ListView):
    model = Sauna
    template_name = 'bookings/sauna_list.html'
    context_object_name = 'saunas'

class MyBookingsView(LoginRequiredMixin, ListView):
    model = Booking
    form_class = BookingForm
    template_name = 'bookings/booking_form.html'
    success_url = reverse_lazy('my_bookings')

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user).order_by('-booking_date', '-time_slot__start_time')

class BookingCreateView(LoginRequiredMixin, CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'bookings/booking_form.html'
    success_url = reverse_lazy('my_bookings')

    def form_valid(self, form):
        booking = form.save(commit=False)
        booking.user = self.request.user
        booking.status = Booking.STATUS_CONFIRMED
        booking.full_clean()
        booking.save()
        messages.success(self.request, 'Booking created successfully.')
        return redirect(self.success_url)

class BookingDeleteView(LoginRequiredMixin, DeleteView):
    model = Booking
    template_name = 'bookings/booking_confirm_delete.html'
    success_url = reverse_lazy('my_bookings')

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Booking cancelled successfully.')
        return super().delete(request, *args, **kwargs)

