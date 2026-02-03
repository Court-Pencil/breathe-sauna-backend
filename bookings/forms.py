from django import forms
from django.utils import timezone
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["booking_date", "time_slot", "number_of_guests", "special_requests"]
        widgets = {
            "booking_date": forms.DateInput(attrs={"type": "date"}),
            "special_requests": forms.Textarea(attrs={"rows": 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["time_slot"].queryset = self.fields["time_slot"].queryset.filter(is_available=True)


    def clean_booking_date(self):
        booking_date = self.cleaned_data.get("booking_date")

        if booking_date and booking_date < timezone.now().date():
            raise forms.ValidationError("Booking date cannot be in the past.")
        return booking_date

    

    def clean(self):
        cleaned = super().clean()

        booking = Booking(
            booking_date=cleaned.get("booking_date"),
            time_slot=cleaned.get("time_slot"),
            number_of_guests=cleaned.get("number_of_guests"),
            special_requests=cleaned.get("special_requests"),
        )

        if self.instance and self.instance.pk:
            booking.pk = self.instance.pk
            booking.user = self.instance.user
            booking.sauna = self.instance.sauna 
        try:
            booking.clean()
        except Exception as e:
            raise forms.ValidationError(str(e))
        return cleaned
