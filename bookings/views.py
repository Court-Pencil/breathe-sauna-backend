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

class SaunaView(TemplateView):
    template_name = "bookings/sauna_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        sauna = Sauna.objects.filter(is_active=True).first()
        context["sauna"] = sauna

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
    template_name = "bookings/booking_form.html"
    success_url = reverse_lazy("my_bookings")


    def form_valid(self, form):
        booking = form.save(commit=False)
        booking.user = self.request.user
        
        sauna = Sauna.objects.filter(is_active=True).first()

        if sauna is None:
            form.add_error(None, "No active sauna is available. Please contact the admin.")
            return self.form_invalid(form)

        booking.sauna = sauna
        booking.status = "confirmed"

        try:
            booking.save()
            messages.success(self.request, 'Booking created successfully.')
            return redirect(self.success_url)
        except Exception as e:
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
    template_name = 'bookings/booking_confirm_delete.html'
    success_url = reverse_lazy('my_bookings')

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Booking cancelled successfully.')
        return super().delete(request, *args, **kwargs)

