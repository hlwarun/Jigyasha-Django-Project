from django.db import models

# Create your models here.

class ContactU(models.Model):
    country = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    street = models.CharField(max_length=20)
    telephone = models.CharField(max_length=20)
    service_days = models.CharField(max_length=20)
    service_time = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return "Current Address of our Company"
