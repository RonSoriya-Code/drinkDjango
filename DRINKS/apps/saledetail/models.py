from django.db import models
from apps.sale.models import Sale
from apps.product.models import Product

# Create your models here.

class SaleDetail(models.Model):
     sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
     product = models.ForeignKey(Product, on_delete=models.CASCADE)
     qty = models.IntegerField(blank=False, null=False, default=1)
     price = models.DecimalField(max_digits=8, decimal_places=2, blank=False, null=False)

     class Meta:
          unique_together = ('sale', 'product')

     def __str__(self):
          return f"{self.sale} - {self.product}"