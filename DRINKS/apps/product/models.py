from django.db import models


class Product(models.Model):
	name = models.CharField(max_length=200)
	photo = models.ImageField(upload_to='products_photo/', blank=True, null=True)
	quantity = models.PositiveIntegerField(default=0)
	price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

	def __str__(self):
		return f"{self.name} ({self.quantity}) - {self.price}"

