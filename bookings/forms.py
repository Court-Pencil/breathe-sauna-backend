from django import forms
from .models import Booking, Sauna


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
