from django import forms
from .models import Booking, Sauna
from django.db.models import Sum
from django.core.exceptions import ValidationError



class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            "sauna",
            "booking_date",
            "time_slot",
            "number_of_guests",
            "special_requests",
        ]

        widgets = {
            "booking_date": forms.DateInput(attrs={"type": "date"}),
            "special_requests": forms.Textarea(attrs={"rows": 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Only allow active saunas to be booked
        self.fields["sauna"].queryset = Sauna.objects.filter(is_active=True)

    def clean(self):
        cleaned_data = super().clean()
        sauna = cleaned_data.get("sauna") 
        booking_date = cleaned_data.get('booking_date') 
        time_slot = cleaned_data.get('time_slot') 
        number_of_guests = cleaned_data.get('number_of_guests')

        if not sauna or not booking_date or not time_slot or not number_of_guests:
            return cleaned_data

        self.instance.sauna = sauna
        self.instance.booking_date = booking_date
        self.instance.time_slot = time_slot
        self.instance.number_of_guests = number_of_guests

        try:
            self.instance.clean()
        except ValidationError as e:
            self.add_error("number_of_guests", e.message)

        return cleaned_data

