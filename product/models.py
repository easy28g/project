from django.db import models
from company.models import Company

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=100, decimal_places=2)
    quantity_in_stock = models.IntegerField(default=0)
    companies = models.ManyToManyField(Company, related_name='products', blank=False)
        
    def __str__(self):
        return self.name