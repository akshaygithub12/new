from django.db import models
from django.contrib import admin

# Create your models here.
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"


class Flights(models.Model):
    origin=models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination=models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()


def __init__(self):
    return f"start from {self.origin} and end {self.destination}"


class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    flights = models.ManyToManyField(Flights, blank=True, related_name="passengers")

    def __str__(self):
        return f"{self.first} {self.last}"
    
