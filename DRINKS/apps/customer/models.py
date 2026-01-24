from django.db import models

class Customer(models.Model):

    GENDER_CHOICE = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(unique=True)
    phone = models.IntegerField(blank=False, null=False)
    gender = models.CharField(max_length=10, blank=True, choices=GENDER_CHOICE)
    
    def __str__(self):
        return self.name

class CustomerProfile(models.Model):

    customer = models.OneToOneField(
        Customer, 
        on_delete = models.CASCADE,
        related_name = 'profile',
    )

    address = models.TextField(blank=True, null=True)
    debt = models.DecimalField(max_digits=10, decimal_places=2, default=0)