from django import forms
from django.utils import timezone
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["sauna", "start_at", "duration_minutes", "notes"]
        widgets = {
            "start_at": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }

    def clean_start_at(self):
        start_at = self.cleaned_data.get("start_at")

        if start_at and start_at < timezone.now():
            raise forms.ValidationError("Please choose a future date/time.")
        return start_at

    def clean(self):
        cleaned = super().clean()

        booking = Booking(
            sauna=cleaned.get("sauna"),
            start_at=cleaned.get("start_at"),
            duration_minutes=cleaned.get("duration_minutes"),
            notes=cleaned.get("notes"),
        )

        if self.instance and self.instance.pk:
            booking.pk = self.instance.pk
            booking.user = self.instance.user
        try:
            booking.clean()
        except Exception as e:
            raise forms.ValidationError(str(e))
        return cleaned
