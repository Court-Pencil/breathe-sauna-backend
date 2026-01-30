from django.contrib import admin
from .models import Sauna, TimeSlot, Booking

@admin.register(Sauna)
class SaunaAdmin(admin.ModelAdmin):
    # Customize how Saunas appear in admin panel
    list_display = ['name', 'capacity', 'price_per_hour', 'is_active']
    list_filter = ['is_active']
    search_fields = ['name', 'description']
    list_editable = ['is_active']

@admin.register(TimeSlot)
class TimeSlotAdmin(admin.ModelAdmin):
    # Show TimeSlot in admin and customize it.
    list_display = ['start_time', 'end_time', 'is_available']
    list_filter = ['is_available']
    list_editable = ['is_available']

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    # Customize how Bookings appear in admin panel
    list_display = ['user', 'booking_date', 'time_slot', 'status', 'created_at' ]
    list_filter = ['status', 'booking_date', 'sauna']
    search_fields = ['user__username', 'user__email'] # follow the foreign key to user, then search username 
    date_hierarchy = 'booking_date' # Lets you browse bookings by date, year or month

    fieldsets = (
        ('Booking Information', {
            'fields': ('user', 'sauna', 'time_slot', 'booking_date')
        }),
        ('Details', {
            'fields': ('number_of_guests', 'special_requests', 'status')
        }),
        ('MetaData', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
        )
    readonly_fields = ['created_at', 'updated_at']
    





