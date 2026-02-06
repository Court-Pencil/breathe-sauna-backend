from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView


from django.core.exceptions import ValidationError
from django.db.models import Count, Q
import json
from datetime import date, timedelta

from .forms import BookingForm
from .models import Booking, Sauna, TimeSlot

class HomeView(TemplateView):
    template_name = 'bookings/home.html'

class SaunaView(TemplateView):
    template_name = "bookings/sauna_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        sauna = Sauna.objects.filter(is_active=True)
        context["saunas"] = sauna

        return context

class MyBookingsView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = 'bookings/my_bookings.html'
    context_object_name = 'bookings'

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user).order_by('-booking_date', '-time_slot__start_time')

class BookingCreateView(LoginRequiredMixin, CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'bookings/booking_form.html'
    success_url = reverse_lazy('my_bookings')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Get availability data for next 60 days
        context['available_slots_json'] = self.get_availability_json()
        
        return context

    def get_availability_json(self):
        """
        Generate JSON data for calendar showing availability
        Format: {'2026-02-06': [{'time': '09:00', 'available': 1, 'id': 1}]}
        """
        availability = {}
        sauna = Sauna.objects.filter(is_active=True).first()
        
        if not sauna:
            return json.dumps({})
        
        # Get all available time slots
        time_slots = TimeSlot.objects.filter(is_available=True)
        
        # Check next 60 days
        start_date = date.today()
        end_date = start_date + timedelta(days=60)
        
        current_date = start_date
        while current_date <= end_date:
            date_key = current_date.isoformat()
            availability[date_key] = []
            
            for slot in time_slots:
                # Check how many bookings exist for this date/time
                existing_bookings = Booking.objects.filter(
                    sauna=sauna,
                    booking_date=current_date,
                    time_slot=slot,
                    status__in=['pending', 'confirmed']
                ).count()
                
                # Calculate available spots
                available_spots = sauna.capacity - existing_bookings
                
                availability[date_key].append({
                    'time': slot.start_time.strftime('%H:%M'),
                    'available': available_spots,
                    'id': slot.id
                })
            
            current_date += timedelta(days=1)
        
        return json.dumps(availability)

    def form_valid(self, form):
        booking = form.save(commit=False)
        booking.user = self.request.user

        sauna = Sauna.objects.filter(is_active=True).first()
        if sauna is None:
            form.add_error(None, "No active sauna is available.")
            return self.form_invalid(form)

        booking.sauna = sauna
        booking.status = "confirmed"

        try:
            booking.save()
            messages.success(self.request, 'Booking created successfully.')
            return redirect(self.success_url)
        except ValidationError as e:
            form.add_error(None, str(e))
            return self.form_invalid(form)
        

class BookingUpdateView(LoginRequiredMixin, UpdateView):
    model = Booking
    form_class = BookingForm
    template_name = 'bookings/booking_form.html'  
    success_url = reverse_lazy('my_bookings')

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)

    def form_valid(self, form):
        booking = form.save(commit=False)
        booking.user = self.request.user

        if not booking.sauna:
            sauna = Sauna.objects.filter(is_active=True).first()
            if sauna is None:
                form.add_error(None, "No active sauna is available.")
                return self.form_invalid(form)
            booking.sauna = sauna
        
        try:
            booking.full_clean()
            booking.save()
            messages.success(self.request, 'Booking updated successfully.')
            return redirect(self.success_url)
        except Exception as e:
            form.add_error(None, str(e))
            return self.form_invalid(form)

    


class BookingDeleteView(LoginRequiredMixin, DeleteView):
    model = Booking
    template_name = 'bookings/bookings_confirm_delete.html'
    success_url = reverse_lazy('my_bookings')

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Booking cancelled successfully.')
        return super().delete(request, *args, **kwargs)

