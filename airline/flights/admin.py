from django.contrib import admin
from .models import Airport,Flights,Passenger
# Register your models here.

class FlightAdmin(admin.ModelAdmin):
    list_display = ("id", "origin", "destination", "duration")

admin.site.register(Airport)
admin.site.register(Passenger)
admin.site.register(Flights, FlightAdmin)
