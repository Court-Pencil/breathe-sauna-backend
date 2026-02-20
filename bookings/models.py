from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.db.models import Sum


class Sauna(models.Model): # what can be booked, represents a physical sauna room
    name = models.CharField(max_length=100)
    display_order = models.PositiveIntegerField(default=0) # for sorting saunas in the UI
    capacity = models.IntegerField(default=6)
    description = models.TextField()
    price_per_hour = models.DecimalField(max_digits=6, decimal_places=2)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['display_order']


class TimeSlot(models.Model): # when it can be booked
    start_time = models.TimeField()
    end_time = models.TimeField()
    # stores times without dates, can reuse across many dates
    is_available = models.BooleanField(default=True)
    # lets admins disable slots e.g. for holidays or maintance

    def __str__(self):
        # Display time in readable format. Example: "09:00 - 10:00" 
        return f"{self.start_time.strftime('%H:%M')} - {self.end_time.strftime('%H:%M')}" 

    class Meta:
        ordering = ['start_time'] # Slots appear chronologically
        unique_together = ['start_time', 'end_time'] # Prevent duplicate time slots


# Main booking model - the CORE of CRUD operations.
class Booking(models.Model): # links users,saunas, dates and times
    STATUS_CHOICES = [
        ('pending', 'Pending'), 
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed')
    ] 

    # Foreign Keys = Relationships to other models
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='bookings'
    )

    sauna = models.ForeignKey(
        Sauna,
        on_delete=models.CASCADE,
        related_name='bookings'
    )

    time_slot = models.ForeignKey(
        TimeSlot,
        on_delete=models.CASCADE
    )

    booking_date = models.DateField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )
    number_of_guests = models.IntegerField(default=1)
    special_requests = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.sauna.name} on {self.booking_date}"

    class Meta:
        ordering = ['-booking_date', '-time_slot__start_time']

    def clean(self):
        if self.booking_date and self.booking_date < timezone.now().date():
            raise ValidationError("Booking date cannot be in the past.")

        
            
        if self.sauna_id:
            if self.number_of_guests > self.sauna.capacity:
                raise ValidationError(
                    f"Number of guests ({self.number_of_guests}) exceeds "
                    f"sauna capacity ({self.sauna.capacity})."
                )

        if not self.sauna_id or not self.booking_date or not self.time_slot_id:
            return

        if self.status != 'cancelled':
            existing_guests = Booking.objects.filter(
                sauna=self.sauna,
                booking_date=self.booking_date,
                time_slot=self.time_slot,
                status__in=['pending', 'confirmed']
            ).exclude(pk=self.pk).aggregate(existing_total=Sum('number_of_guests'))

            existing_total = existing_guests.get('existing_total') or 0

            total_with_this = existing_total + self.number_of_guests

            if total_with_this > self.sauna.capacity:
                available = self.sauna.capacity - existing_total
                raise ValidationError(
                    f"{available} spot(s) available. "
                    f"You requested {self.number_of_guests} guest(s)."
                )


    def save(self, *args, **kwargs):
        self.clean()  # Validate before saving
        super().save(*args, **kwargs)