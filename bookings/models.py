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
        
