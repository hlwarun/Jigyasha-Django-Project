from django.db import models

# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=20)
    information = models.CharField(max_length=200)
    image = models.ImageField(upload_to='team')

    def __str__(self):
        return self.name
