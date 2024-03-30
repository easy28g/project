from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    country = models.CharField(max_length=255)
    settlement_city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    OPENING_HOURS_CHOICES = (
        ('08:00-18:00', '08:00-18:00'),
        ('09:00-17:00', '09:00-17:00'),
        ('10:00-18:00', '10:00-18:00'),
    )
    opening_hours = models.CharField(max_length=20, choices=OPENING_HOURS_CHOICES)
        
    def __str__(self):
        return self.name