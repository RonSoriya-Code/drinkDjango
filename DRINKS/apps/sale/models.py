from django.db import models
from apps.customer.models import Customer

# Create your models here.

class Sale(models.Model):
     saleCode = models.CharField(blank=False, null=False, max_length=20)
     saleData = models.DateField(blank=False, null=False)
     customerId = models.ForeignKey(Customer, on_delete=models.CASCADE)
