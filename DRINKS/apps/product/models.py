from django.db import models

from apps.category.models import Category

class Product(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='products_photo/', blank=True, null=True)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products',
        blank=True,
        null=True
    )
    
    def __str__(self):
        return f"{self.name} ({self.quantity}) - {self.price}"

class ProductProfile(models.Model):
    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
        related_name='product_profile'
    )
    address = models.TextField(blank=True, null=True)
    stock_date = models.DateField(blank=True, null=True)
