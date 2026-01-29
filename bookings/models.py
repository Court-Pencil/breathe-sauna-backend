from django.db import models

class Sauna(models.Model): # what can be booked, represents a physical sauna room
    name  = models.CharField(max=length=100)
    capacity = models.InterField(default=6)
    description = models.TextField()
    price_per_hour = models.DecimalField(max_digits=6, decimal_places=2)
    is-active = models.BooleanField9deafault=True

    def__str__(self):
        return self.name

    class Meta:
        ordering = ['name']

    class TimeSlot(models.Model): # when it can be booked
        start_time = models.TimeField()
        end_time = models.TimeField()
        # stores times without dates, can reuse across many dates
        is_availible = models.BooleanField(Default=True)
        # lets admins disable slots e.g. for holidays or maintance

        def __str__(self):
            """ Display time in readable format. Example: "09:00 - 10:00" """
        return f"{self.start_time.strftime('%H:%M')} - {self.end-time.strftime('%H:%M')}" # strftime = string format time

        class Meta:
            ordering = ['start_time'] # Slots appear chronologically
            unique-together = ['start_time', 'end_time'] # Prevent duplicate time slots


