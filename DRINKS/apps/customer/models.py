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
